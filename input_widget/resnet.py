# 导入神经网络计算需要的各种包
import torch
# 导入了一个模块中的一个函数
from torch import nn

# 定义一个残差块
class Residual(nn.Module):
    # 是否需要使用1X1的卷积层，主要是用来进行通道转换
    # 定义网络属性
    def __init__(self, input_channel, output_channel, use_1x1conv=False,
                 strides=1, label_=True):
        super().__init__()
        # 前向传播过程使用相乘还是相加操作的标志
        self.label = label_
        # 第一个卷积块
        self.conv1 = nn.Conv1d(input_channel, output_channel,
                               kernel_size=3, padding=1, stride=strides)
        # 第二个卷积块
        self.conv2 = nn.Conv1d(output_channel, output_channel,
                               kernel_size=3, padding=1, stride=strides)

        # 是否进行通道数变换
        if use_1x1conv:
            self.conv3 = nn.Conv1d(input_channel, output_channel,
                                   kernel_size=1, strides=strides)
        else:
            self.conv3 = None

        # 每一个卷积后的数据需要进行一次归一化
        self.bn1 = nn.BatchNorm1d(output_channel)
        self.bn2 = nn.BatchNorm1d(output_channel)
        self.relu = nn.ReLU(inplace=True)

    # 网络传播过程
    def forward(self, x):
        # 首先对输入进行卷积,卷积为类属性中定义的卷积
        # 输入进行卷积
        x_conv = self.conv1(x)
        # BN处理
        x_bn = self.bn1(x_conv)
        # 进行激活处理
        x1_output = self.relu(x_bn)
        # 进行第二次卷积
        x2_output = self.relu(self.bn2(self.conv2(x1_output)))

        # 如果通道数不一致，则需要调正通道数
        if self.conv3:
            x2_output = self.conv3(x)

        # 使用相加操作还是相乘操作
        if self.label:
            y = x * x2_output
        else:
            y = x + x2_output

        output = self.relu(y)
        return output

# 神经网络实例化，输入通道，输出通道分别为3,输入与输出一致
# 定义第一个残差块，该残差块使用对应位置相乘操作
# 通过label_变量控制，不输入的情况，默认为True，
net = Residual(3, 3, label_=True)

# 生成一个输入通道与输出通道不一致
# 输入通道与输出通道不一致的情况，需要使用1x1的卷积进行处理
# 步长使用2输入图像宽高缩小，通道数增加，（可以理解为宽高信息压缩，生成通道信息）
# 举例，未使用
#net = Residual(3, 6, use_1x1conv=True, strides=2)


# 生成一个二维张量，矩阵MxN
# 从区间[0, 1)的均匀分布中抽取的一组随机数
x = torch.rand(3, 6)
# 图像增加一个维度
x_in = x.unsqueeze(0)
#print(x.shape)
# print(x)
# 将输入放入第一个残差块
output1 = net(x_in)
#print(output1)

# 定义第二个残差块，该残差块使用对应位置相加
# 通过label_变量控制，
net2 = net = Residual(3, 3, label_=False)
# 将上一个输入放入到神经网络中
output2 = net2(output1)
# 最终输出，丢掉一个维度（类似于批量数据处理数据的batch，这里的batch都为1）
output = output2.squeeze(0)
print("输出数据：", output)





