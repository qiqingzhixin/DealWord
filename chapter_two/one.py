'''
词编码
向量分布的相似性
自然语言处理在后面有一个强大的字典
建立字典的问题：
1.不能分辨细节的差别
2.需要大量的人为劳动
3.主观的
4.无法发现新词
5.难以精准计算词之间的相似度


语料库->字典
词权重的计算方式
1.TF-IDF
2.binary weighting:出现为1 不出现为0 [1,1,1,1,1,0,0,0,1,1,1]

Bi-gram和N-gram
Bi-gram
John likes to watch movies Mary likes too. 分为
John likes,likes to, to watch,watch movies ,....,likes too

分布式表示
用一个词附近的其他词来表达该词

共现矩阵（concurrence matrix）

SVD降维

NNLM(Neural Network Language model)
直接从语言模型出发，将模型最优化过程转化为求词向量表示的过程

NNLM:结构模型讲解

CBOW（连续词袋)
通过上下文推断出一个单词
我喜欢**机器学习
推断出**为学习
'''