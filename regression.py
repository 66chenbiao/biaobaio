#coding:utf8

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

def loadDataSet(filename):
    """
        函数说明:加载数据
        parameters:
            fileName - 文件名
        returns:
         xArr - x数据集
         yArr - y数据集
    """

    numFeat = len(open(filename).readline().split('\t'))
    xArr = []
    yArr = []

    #打开文件名
    fr = open(filename)

    #遍历数据
    for line in fr.readlines():
        #临时列表
        lineArr = []
        curLine = line.strip().split('\t')

        #将遍历出来的内容存入临时列表中
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
    return xArr, yArr

#求解回归系数
def standRegres(xArr, yArr):
    """
    函数说明:计算回归系数w
    parameters:
        xArr - x数据集
        yArr - y数据集
    returns:
        ws - 回归系数
    """
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print('矩阵为奇异矩阵,不能求逆')
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


def plotDataSet():
    """
    函数说明:绘制数据集
    parameters:
        无
    returns:
        无
    """
    #加载数据集
    xArr, yArr = loadDataSet('ex0.txt')

    #数据个数
    n = len(xArr)

    #样本点
    xcord = []
    ycord = []
    for i in range(n):
        xcord.append(xArr[i][1])
        ycord.append(yArr[i])
    fig = plt.figure()
    #添加subplot
    ax = fig.add_subplot(111)
    #绘制样本点
    ax.scatter(xcord, ycord, s = 20, c='blue', alpha=0.8)
    plt.title('DataSet')
    plt.xlabel('x')
    plt.show()

def plotRegression():
    """
    函数说明:绘制回归曲线和数据点
    parameters:
        无
    returns:
        无
    """
    #加载数据集
    xArr, yArr = loadDataSet('ex0.txt')

    #计算回归系数
    ws = standRegres(xArr, yArr)

    #创建xMat,yMat矩阵
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)

    # 深度拷贝xMat矩阵
    xcopy = xMat.copy()

    #排序
    xcopy.sort(0)

    #计算对应的y值
    yHat = xcopy * ws

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xcopy[:,1], yHat, c = 'red')

    #绘制回归线
    ax.scatter(xMat[:,1].flatten().A[0], yMat.flatten().A[0], s=20, c='blue', alpha=.5)

    #设置标题
    plt.title('DataSet')

    plt.xlabel('x')
    plt.show()

def plotwlrRegression():
    """
    函数说明:绘制多条局部加权回归曲线
    parameters:
        无
    returns:
        无
    """
    font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)
    xArr, yArr = loadDataSet('ex0.txt')
    yHat_1 = 0
    pass

def lwlr(testPoint, xArr, yArr, k = 1.0):
    pass

def lwlrTest(testArr, xArr, yArr, k=1.0):
    """
    函数说明:局部加权线性回归测试
    parameters:
        testArr - 测试数据集
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    returns:
        ws - 回归系数
    """
    m = np.shape(testArr)[0]
    yHat = np.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
