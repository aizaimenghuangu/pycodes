#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Using custom colors
====================
Using the recolor method and custom coloring functions.
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import jieba
import os

from wordcloud import WordCloud, STOPWORDS


font = os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)


mask = np.array(Image.open(path.join(d, "tx.png")))


text = open('23.txt', 'r', encoding='UTF-8').read()

# preprocessing the text a little bit
text = text.replace(u"程心说", u"程心")
text = text.replace(u"程心和", u"程心")
text = text.replace(u"程心问", u"程心")

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wordlist_after_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

wc = WordCloud(font_path=font, max_words=2000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(wl_space_split)
# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
wc.to_file("a_new_hope.png")
plt.axis("off")
plt.figure()
plt.title(u"三体-词频统计".encode('utf-8'))
plt.imshow(default_colors)
plt.axis("off")
plt.show()
