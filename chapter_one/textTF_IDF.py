'''文本分类问题
TF_IDF：
TF:Term Frequency.衡量一个term在文档中出现的有多频繁
TF(t)=(t出现在文档中的次数)/(文档中的term总数)
IDF :inverse Document frequency.衡量一个term有多重要
有些词出现的很多，但是明显不是很有用，比如is the and 之类的
IDF(t)=log_e(文档总数/含有t的文档总数).
TF-IDF=TF*IDF 这样是为了把特殊性给体现出来



NLTK实现TF-IDF'''

from nltk.text import TextCollection
from nltk import FreqDist
import nltk
#首先，把所有的文档放到TextCollocation类中，
#这个类会自动帮你断句，做统计，做计算
#一句话算一篇文档
corpus=TextCollection(['this is sentence one',
                       'this is sentence two',
                       'this is sentence three',])
#直接就能算出tfidf
#（term：一句话中的某个term，text：这句话）
print(corpus.tf_idf('this','this is sentene four'))

#同理，怎么得到一个标准大小的vector来表示所有的句子？

#对于每一个新句子
new_sentence='this si sentence five'
#遍历一遍所有的vocabulary中的词
#得到一个标准的单词向量
#1.单词的分割
tokens=nltk.word_tokenize(corpus)
#2.单词的统计
fdist=FreqDist(tokens)
#把频率最高的前50个单词拿出来
standard_freq_vector=fdist.most_common(50)

# for word in standard_vocab: