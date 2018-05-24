# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
from hazm import *
import glob
import math
import operator


class Vopawb():


    junks = ['و', '؛', '/', '.', '?', '؟', '!', '!', '[', ']', '،', 'از', 'به', 'که', 'در', 'تا', 'با', 'رو', 'بی', 'هر', 'چی', 'ایم', 'این', '', '', ]
    def __init__(self):
        self.normalizer =  Normalizer()
        self.pop = []
        self.rap = []
        self.test = []



    def popHandler(self):
        popPaths = ["../lyrics/train/pop/Babak Jahanbakhsh/*.txt", "../lyrics/train/pop/Mohsen Yeganeh/*.txt"]

        for path in popPaths :
            for filename in glob.glob(path):
                with io.open(filename, 'r', encoding="utf-8") as f:
                    lyrics = f.readlines()
                    text = ""

                    for lyric in lyrics:
                        if('\n' in  lyric) :
                            text += lyric[0:-2] + ' '
                        else :
                            text += lyric

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    text = ''
                    for word in words:
                        if word not in self.junks:
                            text += ' ' + word
                    self.pop.append(text)

    def rapHandler(self):
        rapPaths = [
            "../lyrics/train/rap/Hichkas/*.txt",
            "../lyrics/train/rap/Bahram/*.txt",
            "../lyrics/train/rap/Khalvat/*.txt",
            "../lyrics/train/rap/Quf/*.txt",
            "../lyrics/train/rap/Sorena/*.txt"
        ]

        for path in rapPaths :
            for filename in glob.glob(path):
                with io.open(filename, 'r', encoding="utf-8") as f:
                    lyrics = f.readlines()
                    text = ""

                    for lyric in lyrics:
                        if('\n' in  lyric) :
                            text += lyric[0:-2] + ' '
                        else :
                            text += lyric

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    text = ''
                    for word in words:
                        if word not in self.junks:
                            text += ' ' + word
                    self.rap.append(text)


    def trainFileHandler(self):
        with open("train.txt", 'w') as f :
            for cnt in range(len(self.rap)):
                f.write("1 |" + self.rap[cnt] + '\n')
                f.write("-1 |" + self.pop[cnt] + '\n')
        paths = ["../lyrics/test/pop/Babak Jahanbakhsh/*.txt",
                 "../lyrics/test/pop/Mohsen Yeganeh/*.txt",
                 "../lyrics/test/rap/Hichkas/*.txt",
                 "../lyrics/test/rap/Bahram/*.txt",
                 "../lyrics/test/rap/Khalvat/*.txt",
                 "../lyrics/test/rap/Quf/*.txt",
                 "../lyrics/test/rap/Sorena/*.txt"
                 ]

        for path in paths :
            for filename in glob.glob(path):
                with io.open(filename, 'r', encoding="utf-8") as f:
                    lyrics = f.readlines()
                    text = ""


                    for cnt in lyrics:
                        if('\n' in cnt) :
                            text += cnt[0:-2] + ' '
                        else :
                            text += cnt

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    text = ""
                    for word in words :
                        if(word not in self.junks):
                            text += ' ' + word
                    self.test.append(text)
        #print (self.test)
        with open("test.txt", 'w') as f :
            for cnt in range(5):
                f.write('1 |' + self.test[cnt] + '\n')
                f.write('-1 |' + self.test[cnt + 5] + '\n')




    def handler(self):
        self.popHandler()
        self.rapHandler()
        self.trainFileHandler()


a = Vopawb()
a.handler()

