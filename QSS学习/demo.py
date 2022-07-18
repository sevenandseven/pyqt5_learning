import numpy as np
import matplotlib.pyplot as plt

m = 200
X = np.random.randn(2, m)  # 产生2*200 高斯分布 均值为0 方差为1

print(X.shape)

Y = (X[0, :] > 0) * (X[1, :] > 0) * 1.0 + (X[0, :] < 0) * (X[1, :] < 0)

# 可视化
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral)  #

import torch
import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F


# import pandas as pd
# x = pd.read_csv('X.csv',delimiter = ' ',header=None,names = list(np.arange(10)),dtype = np.float32)
# x.head()
# x = x.to_numpy() #转化为numpy 便于后续转化未Tensot

# y = pd.read_csv('y.csv',delimiter = ' ',header=None,names = list(np.arange(1)),dtype =np.float32)
# y.head()         #查看是否转化为想要的格式
# y = y.to_numpy()
# print(y.shape)


# In[8]:


import pandas as pd

xy = pd.read_csv('diabetes.csv', delimiter=',', dtype=np.float32)
# print(xy.head())
xy_numpy = xy.to_numpy()
x = xy_numpy[:, 0:-1]
y = xy_numpy[:, -1].reshape(-1, 1)

# In[9]:


y_frame = pd.DataFrame(y, columns=['A'])

# In[10]:


y_frame['A'].value_counts()

# In[11]:


xy.head()

# In[12]:


# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler #标准化 最后一步数字
# num_pipeline = Pipeline([
#   ('std_scaler',StandardScaler()),# 注意函数实例化 注意有括号
# ])


# In[13]:


# x_rr =num_pipeline.fit_transform(x)


# In[14]:


x_data = torch.Tensor(torch.from_numpy(x))  # 注意此处的Tensor 若由numpy转换过来 numpy的dtype须为np.float_n
y_data = torch.Tensor(torch.from_numpy(y))

# In[15]:


# print(x_data.shape)
# print(y_data.shape)


# In[16]:


# xy


# In[17]:


print(x_data.data.shape)
print(y_data.data.shape)


# # 类的定义

# In[18]:


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # 定义多层神经网络
        self.fc1 = torch.nn.Linear(8, 6)
        self.fc2 = torch.nn.Linear(6, 4)
        self.fc3 = torch.nn.Linear(4, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))  # 8->6
        x = F.dropout(x, p=0.5)  # dropout 1
        x = F.relu(self.fc2(x))  # -6->4
        x = F.dropout(x, p=0.5)  # dropout 2
        y_pred = torch.sigmoid(self.fc3(x))  # 4->1 ->sigmoid
        # warnings.warn("nn.functional.sigmoid is deprecated. Use torch.sigmoid instead."
        return y_pred

def weight_init(m):
    classname = m.__class__.__name__
    if classname.find('Linear') != -1:
        print("hi")
        m.weight.data = torch.randn(m.weight.data.size()[0], m.weight.data.size()[1])
        m.bias.data = torch.randn(m.bias.data.size()[0])

model = Model()

list(model.parameters())


# print(model.__class__.__name__.find('Linear')) #该函数需要用到apply


# In[24]:


# model.apply(weight_init)


# In[25]:


# list(model.parameters())


# # 定义损失函数及优化器

# In[42]:


criterion = torch.nn.BCELoss()  # 定义损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0, dampening=0,
                            weight_decay=0)  # weight_decay 表示使用L2正则化

# In[43]:


Loss = []
# l1_regularization, l2_regularization = torch.tensor(0), torch.tensor(0) #定义L1及L2正则化损失


# In[44]:


print(x.shape)

# In[45]:


for epoch in range(2000):
    y_pred = model(x_data)
    # 计算误差
    cross_loss = criterion(y_pred, y_data)

    l2_regularization = torch.tensor([0], dtype=torch.float32)  # 定义L1及L2正则化损失

    # for param in model.parameters():
    # l1_regularization += torch.norm(param, 1)
    # l2_regularization += torch.norm(param, 2)
    #
    # prin(loss.item())
    # loss = cross_loss + l1_regularization #L1 正则化
    loss = cross_loss + l2_regularization  # L2 正则化

    Loss.append(loss.item())
    # 每迭代1000次打印Lost并记录
    if epoch % 100 == 0:
        print('[%d, %5d] loss: %.3f' %
              (epoch + 1, 2000, loss.item()))
    # 梯度清零
    optimizer.zero_grad()
    # 反向传播
    loss.backward()
    # 更新梯度
    optimizer.step()

# In[46]:


mm = y_pred.detach().numpy()  # 将预测的tensor转化为numpy

# In[47]:


for i in range(len(y_pred)):
    if (y_pred[i] > 0.5):
        y_pred[i] = 1.0
    else:
        y_pred[i] = 0.0
# print(y_pred)
type(y_pred)

# In[48]:
(y_pred == y_data).sum().item() / len(y_data)  # torch.Tensor.sum()函数

