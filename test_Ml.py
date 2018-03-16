'''
贝叶斯情感分析
1.自己定义标签，特殊形式
2.
'''
from nltk.classify import NaiveBayesClassifier
# 训练集
s1='this is a good book'
s2='this is a awesome book'
s3='this is a bad book'
s4='this is a terrible book'


#把一个句子变成一个词列表
#英文的处理方法
def preprocessEnglish(s):
    return {word: True for word in s.lower().split()}
#中文的处理方法
def preprocessChinese(s):
    return s
#把训练集做成标准形式
training_data=[[preprocessEnglish(s1),'pos'],
               [preprocessEnglish(s2),'pos'],
               [preprocessEnglish(s3),'neg'],
               [preprocessEnglish(s4),'neg']]
#喂给model吃
model=NaiveBayesClassifier.train(training_data)

#打印出结果
print(model.classify(preprocessEnglish('this is a good book')))