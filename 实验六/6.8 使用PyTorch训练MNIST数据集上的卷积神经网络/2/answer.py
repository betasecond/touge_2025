from __future__ import print_function
import argparse
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR

# --- 增加调试与自动搜寻功能 ---
def find_dataset_root(start_dir='/data/workspace/myshixun'):
    """
    在 start_dir 下递归搜索 MNIST 数据集，返回正确的 root 路径。
    """
    print(f"正在 {start_dir} 下搜索 MNIST 数据集...")
    
    target_processed = 'training.pt'
    target_raw = 'train-images-idx3-ubyte.gz'
    
    for root, dirs, files in os.walk(start_dir):
        # 1. 检查是否存在 processed 数据
        if target_processed in files and 'processed' in root:
            # root 是 .../MNIST/processed
            mnist_dir = os.path.dirname(root) # .../MNIST
            dataset_root = os.path.dirname(mnist_dir) # .../
            print(f"  -> 发现处理好的数据在: {root}")
            return dataset_root, False # download=False

        # 2. 检查是否存在 raw 数据
        for f in files:
            if target_raw in f or 'train-images-idx3-ubyte' in f:
                if 'raw' in root:
                    mnist_dir = os.path.dirname(root)
                    dataset_root = os.path.dirname(mnist_dir)
                    print(f"  -> 发现原始压缩包在: {root}")
                    return dataset_root, True

    print("  -> 未自动找到标准结构的 MNIST 数据集。")
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    return os.path.abspath(fallback), True


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(64 * 14 * 14, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
            if args.dry_run:
                break


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    test_acc = 100. * correct / len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        test_acc))
    if test_acc > 95:
        print("success!")


def main():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=1, metavar='N',
                        help='number of epochs to train (default: 1)')
    parser.add_argument('--lr', type=float, default=0.1, metavar='LR',
                        help='learning rate (default: 0.1)')
    parser.add_argument('--gamma', type=float, default=0.7, metavar='M',
                        help='Learning rate step gamma (default: 0.7)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='quickly check a single pass')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save-model', action='store_true', default=False,
                        help='For Saving the current Model')
    args = parser.parse_args()
    use_cuda = not args.no_cuda and torch.cuda.is_available()

    torch.manual_seed(args.seed)

    device = torch.device("cuda" if use_cuda else "cpu")

    train_kwargs = {'batch_size': args.batch_size}
    test_kwargs = {'batch_size': args.test_batch_size}
    if use_cuda:
        cuda_kwargs = {'num_workers': 1, 'pin_memory': True, 'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    # 1. 自动寻找路径
    data_path, should_download = find_dataset_root('/data/workspace/myshixun')
    print(f"策略: root={data_path}, download={should_download}")

    # 2. 双重加载策略
    try:
        # 尝试方案 A: 现代 PyTorch 风格 (root 指向 MNIST 的父目录)
        print(f"尝试加载 (Modern Style): {data_path}")
        dataset1 = datasets.MNIST(data_path, train=True, download=should_download, transform=transform)
        dataset2 = datasets.MNIST(data_path, train=False, download=should_download, transform=transform)
        print("成功加载数据集 (Modern Style)")
    
    except RuntimeError as e:
        print(f"方案 A 失败: {e}")
        
        # 尝试方案 B: 旧版兼容风格 (root 直接指向 MNIST 文件夹)
        # 如果当前环境是旧版 torchvision，它不会自动拼接 '/MNIST'，所以我们要手动拼上去
        old_style_path = os.path.join(data_path, 'MNIST')
        print(f"尝试加载 (Old Style): {old_style_path}")
        
        try:
            dataset1 = datasets.MNIST(old_style_path, train=True, download=should_download, transform=transform)
            dataset2 = datasets.MNIST(old_style_path, train=False, download=should_download, transform=transform)
            print("成功加载数据集 (Old Style)")
        except RuntimeError as e2:
            print("方案 B 也失败了。请检查文件权限或完整性。")
            raise e2  # 抛出异常

    train_loader = torch.utils.data.DataLoader(dataset1, **train_kwargs)
    test_loader = torch.utils.data.DataLoader(dataset2, **test_kwargs)

    model = Net().to(device)
    optimizer = optim.Adadelta(model.parameters(), lr=args.lr)

    scheduler = StepLR(optimizer, step_size=1, gamma=args.gamma)
    for epoch in range(1, args.epochs + 1):
        train(args, model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
        scheduler.step()

    if args.save_model:
        torch.save(model.state_dict(), "mnist_cnn.pt")


if __name__ == '__main__':
    main()