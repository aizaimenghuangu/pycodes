#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import os
font = os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
text_from_file_with_apath = open('23.txt', 'r', encoding='UTF-8').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

wordcloud = WordCloud(
    font_path=font, max_font_size=40).generate(wl_space_split)


plt.imshow(wordcloud)
plt.axis(u"off")
plt.show()


#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text = open(u"santi.txt").read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
