# -- encoding:utf-8 --
import warnings
from surprise import Dataset
from surprise import evaluate
from surprise import KNNBaseline, KNNBasic

warnings.filterwarnings('ignore')

# 1. 读取数据
# 方式一：直接使用surprise框架提供的内置API读取movielens的数据
# name: 指定加载什么数据，可选值: 'ml-100k', 'ml-1m', and 'jester'
# 该API默认会将数据下载到路径"~/.surprise_data"
data = Dataset.load_builtin(name='ml-100k')

# 2. 做一个交叉验证的数据划分
data.split(5)


# 3. 模型对象的构建
bsl_options = {
    'method': 'als',  # 给定求解方式，可选值：als和sgd
    'n_epochs': 10,  # 迭代次数
    'reg_i': 20,  # 正则化系数，
    'reg_u': 10  # 正则化系数，
}
"""
k=40: 给定预测时候的邻居样本的数目
min_k=1：在产生预测值的时候，只要要求有多少个临近用户/物品
sim_options={} : 给定相似度矩阵的计算方式
"""
sim_options = {
    'name': 'pearson_baseline',  # 指定相似度的计算法方式，可选值:pearson\msd\cosine\pearson_baseline
    'user_based': True  # 指定是基于用户的协同过滤，还是基于物品的协同过滤
}
algo = KNNBaseline(k=40, min_k=1, sim_options=sim_options, bsl_options=bsl_options)
# algo = KNNBasic(sim_options=sim_options)

# 4. 模型效果评估
#均方误差(MSE)  平均绝对误差(MAE)  一致序列对比率评分(FCP)
evaluate(algo=algo, data=data, measures=['rmse', 'mae', 'fcp'])
