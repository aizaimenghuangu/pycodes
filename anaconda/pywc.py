# coding:utf-8

from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
import os
import random
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


class wordcloud(object):
    """docstring for wordcloud"""

    def __init__(self):
        self.text = " "
        self.stopwords = {}
        self.seglist = []
        self.filepathlist = []
        self.bgpic = None
        self.fontpath = None
        self.wc = None
        pass

    def importStopWord(self, filename=""):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                self.stopwords[line.strip()] = 1

    def processChinese(self, text):
        seg_generator = jieba.cut(text)  # 使用结巴分词，也可以不使用
        self.seglist = [i for i in seg_generator if i not in self.stopwords]
        self.seglist = [i for i in self.seglist if i != u' ']
        self.seglist = r' '.join(self.seglist)

    def importTextpath(self, path):
        for root, directories, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        self.text = self.text + line

    def importTextfile(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                self.text = self.text + line

    def setBackgroudPic(self, bgfilename):
        self.bgpic = imread(bgfilename)

    def setFont(self, fontname):
        self.fontpath = fontname

    def createWordCloud(self):
        self.wc = WordCloud(font_path=self.fontpath,  # 设置字体
                            width=1600,  # 宽度
                            height=1600,  # 高度
                            background_color="gray",  # 背景颜色
                            max_words=2000,  # 词云显示的最大词数
                            mask=self.bgpic,  # 设置背景图片
                            max_font_size=100,  # 字体最大值
                            # min_font_size=10,  # 字体最小值
                            random_state=40,
                            relative_scaling=0
                            )
        # print(self.text)
        self.wc.generate(self.text)

        # 从背景图片生成颜色值
        image_colors = ImageColorGenerator(self.bgpic)
        print(image_colors)

        plt.figure()
        # 以下代码显示图片
        #plt.imshow(self.wc.recolor(color_func=self.grey_color_func, random_state=3))
        plt.imshow(self.wc)
        plt.axis("off")
        plt.show()

    def grey_color_func(self, word, font_size, position, orientation, random_state=None, **kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

    # 保存图片
    def savepicname(self, picname="logo11.png"):
        img = self.wc.to_image()
        img.save(picname)

if __name__ == '__main__':
    wc = wordcloud()
    wc.importStopWord("stopword.txt")
    wc.importTextpath('G:\\Ww\\Studio\\NodeStudio\\blog\\source\\_posts')
    # wc.importTextfile('23.txt')
    wc.setBackgroudPic("logo.png")
    wc.setFont("DroidSansFallbackFull.ttf")
    wc.createWordCloud()
    wc.savepicname()
