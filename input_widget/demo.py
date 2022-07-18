import numpy as np

def initialize_parameters(layer_dims):
    def xavier_init(size):
        # 输入向量的长度，也就是某层神经元个数
        in_dim = size[0]
        xavier_stddev = 1. / np.sqrt(in_dim / 2.)
        return np.random_normal(shape=size, stddev=xavier_stddev)

    L = len(layer_dims)
    parameters = {}
    for l in range(1, L):
        # 随即生成权重
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) / np.sqrt(layer_dims[l - 1])
        # 生成偏置
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters

def Linear_active_forward(pre_A, W, b, activation):
    """
    pre_A--上一层的输出
    W,b-- 当前层的w和b
    activation--激活函数的类型
    return:
    A--激活函数的输出
    cache--记录线性层和激活层的缓存,有效的今后后向传播
    """
    ###calculate the linear output
    Z = np.dot(W,pre_A) + b
    linear_cache = (pre_A, W, b)
    ###calculate the output of activation function

    def relu(x):
        """relu函数"""
        temp = np.zeros_like(x)
        if_bigger_zero = (x > temp)
        return x * if_bigger_zero

    if activation == 'relu':
        A = relu(Z)
        activation_cache = Z
    if activation == 'sigmoid':
        A = 1 / (1 + np.exp(-Z))
        activation_cache = Z

    cache = (linear_cache, activation_cache)

    return A, cache

def forward(X, parameters):
    """
    X--data
    parameters--每一层的参数
    return:
    AL-- 最后一层的输出，激活函数的输出
    caches--列表中，记录每一层的缓存情况
    """

    caches = []
    A = X
    L = len(parameters) // 2
    for l in range(1, L):
        pre_A = A
        ### Linear->Relu forward
        A, cache = Linear_active_forward(pre_A, parameters['W' + str(l)], parameters['b' + str(l)], "relu")
        caches.append(cache)

    ### Linear->Sigmoid forward
    AL, cache = Linear_active_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], "sigmoid")
    caches.append(cache)
    return AL, caches


def cost_function(AL, Y):
    """
    AL--the predicted probability
    Y--true lable
    return:
    cost--a number
    """
    m = Y.shape[1]
    cost = -np.sum(np.multiply(np.log(AL), Y) + np.multiply(np.log(1 - AL), 1 - Y)) / m

    cost = np.squeeze(cost)

    return cost


def linear_backward(dZ, cache):
    """
    参数：
         dZ - 相对于（当前第l层的）线性输出的成本梯度
         cache - 来自当前层前向传播的值的元组（A_prev，W，b）

    返回：
         dA_prev - 相对于激活（前一层l-1）的成本梯度，与A_prev维度相同
         dW - 相对于W（当前层l）的成本梯度，与W的维度相同
         db - 相对于b（当前层l）的成本梯度，与b维度相同
    """
    A_prev, W, b = cache
    m = A_prev.shape[1]
    dW = np.dot(dZ, A_prev.T) / m
    db = np.sum(dZ, axis=1, keepdims=True) / m
    dA_prev = np.dot(W.T, dZ)

    assert (dA_prev.shape == A_prev.shape)
    assert (dW.shape == W.shape)
    assert (db.shape == b.shape)

    return dA_prev, dW, db


def linear_backward(dZ, cache):
    """
    dZ -- Gradient of the cost with respect to the linear output (of current layer l)
    cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer

    Returns:
    dA_pre -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW -- Gradient of the cost with respect to W (current layer l),same shape as W
    db -- Gradient of the cost with respect to b (current layer l), same shape as b
    """
    pre_A, W, b = cache
    m = pre_A.shape[1]
    dW = np.dot(dZ, pre_A.T) / m
    db = np.sum(dZ, axis=1, keepdims=True) / m
    dA_prev = np.dot(W.T, dZ)

    assert (dA_prev.shape == pre_A.shape)
    assert (dW.shape == W.shape)
    assert (db.shape == b.shape)
    ###calculate dW,db,dA_pre

    return pre_A, dW, db

def sigmoid_backward(dA,activation_cache):
    '''
    dA--Gradient of the cost with respect to the activation (of the current layer l)
    activation_cache--linear output of the current layer l
    return:
    dZ--Gradient of the cost with respect to the linear output (of current layer l)
    '''
    ###compute gradient dZ
    return dZ

def relu_backward(dA,activation_cache):
    '''
    dA--Gradient of the cost with respect to the activation (of the current layer l)
    activation_cache--linear output of the current layer l
    return:
    dZ--Gradient of the cost with respect to the linear output (of current layer l)
    '''
    ###compute gradient dZ
    Z = activation_cache
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    return dZ


def linear_active_backward(dA, cache, activation):
    """
    dA--Gradient of the cost with respect to the activation (of the current layer l)
    cache--tuple of values (linear_cache, activation_cache)
    Returns:
    dA_pre -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW -- Gradient of the cost with respect to W (current layer l),same shape as W
    db -- Gradient of the cost with respect to b (current layer l), same shape as b
    """
    linear_cache, activation_cache = cache
    if activation == 'relu':
        ###calculate dZ,dA_pre, dW, db
        dZ = relu_backward(dA, activation_cache)
        dA_pre, dW, db = linear_backward(dZ, linear_cache)
    if activation == 'sigmoid':
        ###calculate dZ,dA_pre, dW, db
        dZ = sigmoid_backward(dA, activation_cache)
        dA_pre, dW, db = linear_backward(dZ, linear_cache)
    return dA_pre, dW, db


def backward(AL, Y, caches):
    """
    AL -- probability vector, output of the forward propagation (forward())
    Y -- true label
    caches -- list of caches containing: every cache of linear_activation_forward() with "relu" and the cache of linear_activation_forward() with "sigmoid"
    Returns:
    grads -- A dictionary with the gradients
    grads["dA" + str(l)] = ...
    grads["dW" + str(l)] = ...
    grads["db" + str(l)] = ...
    """
    grads = {}
    L = len(caches)  # the number of layers
    Y = Y.reshape(AL.shape)
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    ###compute the parameter gradients of the output layer (Linear->sigmoid)
    current_cache = caches[L - 1]
    grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = linear_active_backward(dAL, current_cache,
                                                                                              "sigmoid")

    ### calculate the parameter gradients(dA,dW,db) of the remaining layers(linear->relu)
    for l in reversed(range(L - 1)):
        ###your code
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_active_backward(grads["dA" + str(l + 2)], current_cache, "relu")
        grads["dA" + str(l + 1)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp
    return grads

def update_parameters(parameters,grads,learning_rate):
    L = len(parameters) // 2 #整除
    for l in range(L):
        parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
        parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
    return parameters


def predict(X, parameters):
    """
    X--data
    parameters: updated parameters
    return:
    pred: a binary vector [1,X.shape[1]]
    """

    m = X.shape[1]
    n = len(parameters) // 2  # 神经网络的层数
    pred = np.zeros((1, m))

    # 根据参数前向传播
    probas, caches = forward(X, parameters)

    for i in range(0, probas.shape[1]):
        if probas[0, i] > 0.5:
            pred[0, i] = 1
        else:
            pred[0, i] = 0

    print("准确度为: " + str(float(np.sum((pred == y)) / m)))
    return pred


def model(X, Y, layer_dims, learning_rate, num_iterations):
    np.random.seed(1)
    costs = []
    ### Parameters initialization.
    ###your code
    parameters = initialize_parameters(layer_dims)
    # Loop (gradient descent)
    for i in range(0, num_iterations):
        ### Forward propagation: INPUT->[LINEAR -> RELU]*(L-1) -> LINEAR ->SIGMOID.
        ### your code
        AL, caches = forward(X, parameters)

        ### Compute cost.
        current_cost = cost_function(AL, Y)
        costs.append(current_cost)
        ### Backward propagation.
        ###your code
        grads = backward(AL, Y, caches)

        ### Update parameters.
        ### your code
        paramet = update_parameters(parameters, grads, learning_rate)

        if print_cost and i % 300 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    return parameters, costs


def predict(X, parameters):
    """
    X--data
    parameters: updated parameters
    return:
    pred: a binary vector [1,X.shape[1]]
    """

    m = X.shape[1]
    n = len(parameters) // 2  # 神经网络的层数
    pred = np.zeros((1, m))

    # 根据参数前向传播
    probas, caches = forward(X, parameters)

    for i in range(0, probas.shape[1]):
        if probas[0, i] > 0.5:
            pred[0, i] = 1
        else:
            pred[0, i] = 0

    print("准确度为: " + str(float(np.sum((pred == y)) / m)))
    return pred


def model(X, Y, layer_dims, learning_rate, num_iterations):
    np.random.seed(1)
    costs = []
    ### Parameters initialization.
    ###your code
    parameters = initialize_parameters(layer_dims)
    # Loop (gradient descent)
    for i in range(0, num_iterations):
        ### Forward propagation: INPUT->[LINEAR -> RELU]*(L-1) -> LINEAR ->SIGMOID.
        ### your code
        AL, caches = forward(X, parameters)

        ### Compute cost.
        current_cost = cost_function(AL, Y)
        costs.append(current_cost)
        ### Backward propagation.
        ###your code
        grads = backward(AL, Y, caches)

        ### Update parameters.
        ### your code
        paramet = update_parameters(parameters, grads, learning_rate)

        if print_cost and i % 300 == 0:
            print("Cost after iteration %i: %f" % (i, costs))

    return parameters, costs


def load_data():
    train_dataset = h5py.File('./train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('./test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


##preproccessing code
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage

# matplotlib inline
plt.rcParams['figure.figsize'] = (5.0, 4.0)  # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
np.random.seed(1)
train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
# Reshape the training and test examples
train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T
# Standardize data to have feature values between 0 and 1.
train_x = train_x_flatten / 255.
test_x = test_x_flatten / 255.

layer_dims = [12288, 20, 7, 5, 1]####you can change the dim of hidden layer, or the number of hidden layers
learning_rate=0.05
num_iterations=10000
parameters=model(train_x,train_y,layer_dims,learning_rate,num_iterations)
pred=predict(test_x,test_y)
print(pred)
###calculate accuracy
#accuracy =
###plot the cost
###your code

