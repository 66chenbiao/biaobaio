# -- encoding:utf-8 --

from surprise import Dataset, Reader
from surprise import KNNBasic, KNNWithMeans, KNNBaseline

# 1. 读取数据
#用户id、商品id、评分、时间戳
# 方式一：直接使用surprise框架提供的内置API读取movielens的数据
# name: 指定加载什么数据，可选值: 'ml-100k', 'ml-1m', and 'jester'
# 该API默认会将数据下载到路径"~/.surprise_data"
data = Dataset.load_builtin(name='ml-100k')


# 2. 数据处理(是将数据处理成能够输入到算法中的形式)
# 因为读取的数据是一行一行的用户物品评分数据，也就是我们常说的MovieLens格式的数据，但是算法要求输出的是用户物品评分矩阵数据，所以这里需要将数据做一个转换的操作
# 在这个API中会将用户id、物品id做一个转换映射，因为实际的id有可能不是连续的。
trainset = data.build_full_trainset()

# 3. 模型对象的构建
bsl_options = {
    'method': 'als',  # 给定求解方式，可选值：als和sgd
    'n_epochs': 10,  # 迭代次数
    'reg_i': 20,  # 求解bi的时候的正则化系数
    'reg_u': 10  # 求解bu的时候的正则化系数
}
bsl_options = {
    'method': 'sgd',  # 给定求解方式，可选值：als和sgd
    'n_epochs': 10,  # 迭代次数
    'reg': 0.02,  # 求解参数过程中的正则化系数
    'learning_rate': 0.1  # 参数更新的学习率
}
"""
	k=40: 给定预测时候的邻居样本的数目
	min_k=1：在产生预测值的时候，只要要求有多少个临近用户/物品
	sim_options={} : 给定相似度矩阵的计算方式
"""
sim_options = {
    'name': 'pearson',  # 指定相似度的计算法方式，可选值:pearson\msd\cosine\pearson_baseline
    'user_based': True  # 指定是基于用户的协同过滤，还是基于物品的协同过滤
}
algo = KNNBaseline(k=40, min_k=1, sim_options=sim_options)

# 4. 模型训练
algo.fit(trainset)

# 5. 模型效果评估
# TODO: surprise框架中需要单独的去设置这个效果评估的代码

# 6. 模型存储/持久化/模型预测
# 使用预测的时候必须使用predict方法，predict方法底层会调用estimate这个API产生预测值
# predict API输出的用户id和物品id必须是字符串的形式
uid = "196"
iid = "242"
pred = algo.predict(uid, iid)
print("用户{}对于物品{}的评分为:{}".format(uid, iid, pred.est))
