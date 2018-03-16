import nltk
from nltk.corpus import stopwords

'''
预处理的流程
1.分词：将每一个单词分开
2.打标签：标注每个单词的词性
3.归一化处理：将一些单词比如went 转化成go等形式
4.出去停止词：如果句子里停止词比较多会影响句意分析'''

# 分词
text = nltk.word_tokenize('what does the fox say')
print(text)
# 打标签
text_tag = nltk.pos_tag(text)
print(text_tag)
# 除去停止词
filtered_words = [word for word in text if word not in stopwords.words('english')]
print(filtered_words)
print(stopwords.words('english'))

'''
Frequency 统计器'''
