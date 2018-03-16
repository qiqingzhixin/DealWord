'''文本分类问题
TF_IDF：
TF:Term Frequency.衡量一个term在文档中出现的有多频繁
TF(t)=(t出现在文档中的次数)/(文档中的term总数)
IDF :inverse Document frequency.衡量一个term有多重要
有些词出现的很多，但是明显不是很有用，比如is the and 之类的
IDF(t)=log_e(文档总数/含有t的文档总数).
TF-IDF=TF*IDF 这样是为了把特殊性给体现出来'''