import pandas  # 引入pandas包
from pandas import Series as sr, DataFrame as df  # 从pandas包引入Series与DataFrame格式
from collections import Counter as cr  # 引入Counter进行计数
import jieba.posseg as pseg  # 引入结巴分词词性标注

path = ''  # 读取文件路径
data1 = df.read_csv(path, sep=)  # sep后填文件间隔符，csv一般为'\t'
l = len(data1)
df1 = df(columns=['word', 'type'])
for i in range(l):
    words = pseg.cut(data1.ix[i][x])  # x填写要分词的内容所在列数-1
    for t in words:
        df2 = pd.DataFrame([t.word, t.flag], columns=data2.columns)
        df1.append(df2, ignore_index=True)
df3 = df1.groupby(['word', 'type']).count()
