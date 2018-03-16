'''
1.统计器使用
前期准备是得到一个向量的维数和有哪些单词
将单词进行统计，计算出一个向量
用向量的余弦定理来判断这个句子和其他句子的相似程度
'''
import nltk
from nltk import FreqDist

# 做一个词库
corpus = 'this is my sentence ' \
         'this is my life ' \
         'this is the day'
# 随便用tokenize一下
# 显然，正如上文提到，
# 这里可以根据需要做任何的preprocessing：
# stopwords，lenma，stenming，etc

tokens = nltk.word_tokenize(corpus)
print(tokens)
# 统计单词的次数
fdist = FreqDist(tokens)
print(fdist['is'])
# 我们把最常用的50个单词拿出来
standard_freq_vector = fdist.most_common(50)
size = len(standard_freq_vector)
print(standard_freq_vector)


# Func:按照出现频率大小，记录下每一个单词的位置
# 把每一个单词定一个位置
def position_lookup(v):
    res = {}
    counter = 0
    for word in v:
        # print(word)
        res[word[0]] = counter
        counter += 1
    return res


# 标准位置的对照表方便生成向量
standard_position_dict = position_lookup(standard_freq_vector)
print(standard_position_dict)

# 现在将一个句子转化成向量
sentence = 'this is cool'
# 新建一个跟我们的标准vector相同大小的向量
freq_vector = [0] * size
# 简单的preprocessing
test_tokens = nltk.word_tokenize(sentence)
# 对于这个新句子里的每一个单词
for word in test_tokens:
    try:
        # 如果在我们的词库里出现过
        # 那么就在位置上+1
        freq_vector[standard_position_dict[word]] += 1
    except KeyError:
        continue
# 这样就计算出该语句对应的向量
print(freq_vector)
