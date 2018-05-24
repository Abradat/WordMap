# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
from hazm import *
import glob
import math
import operator


class Mallet():


    junks = ['و', '؛', '/', '.', '?', '؟', '!', '!', '[', ']', '،', 'از', 'به', 'که', 'در', 'تا', 'با', 'رو', 'بی', 'هر', 'چی', 'ایم', 'این', '', '', ]
    def __init__(self):
        self.normalizer =  Normalizer()
        self.features = []
        self.final = []
        self.counter = 0
        self.rapCounter = 0




    def featureHandler(self):
        with open('features.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print (line)
                self.features.append(line.strip())

    def popHandler(self):
        self.counter = 0
        popPaths = ["../lyrics/train/pop/Babak Jahanbakhsh/*.txt", "../lyrics/train/pop/Mohsen Yeganeh/*.txt"]

        for path in popPaths :
            for filename in glob.glob(path):
                with io.open(filename, 'r', encoding="utf-8") as f:
                    lyrics = f.readlines()
                    text = ""

                    for lyric in lyrics:
                        text += lyric

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    line = str(self.counter) + ' ' + 'pop '
                    self.counter += 1

                    for word in words:
                        if word not in self.junks and word in self.features:
                            line += word + ' '
                    self.final.append(line)
        #print (self.final)

    def rapHandler(self):
        self.counter = 0
        rapPaths = [
            "../lyrics/train/rap/Hichkas/*.txt",
            "../lyrics/train/rap/Bahram/*.txt",
            "../lyrics/train/rap/Khalvat/*.txt",
            "../lyrics/train/rap/Quf/*.txt",
            "../lyrics/train/rap/Sorena/*.txt"
        ]

        for path in rapPaths:
            for filename in glob.glob(path):
                with io.open(filename, 'r', encoding="utf-8") as f:
                    lyrics = f.readlines()
                    text = ""

                    for lyric in lyrics:
                        text += lyric

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    line = str(self.counter) + ' ' + 'rap '
                    self.counter += 1

                    for word in words:
                        if word not in self.junks and word in self.features:
                            line += word + ' '
                    self.final.append(line)


    def malletHandler(self):
        with open('mallet.txt', 'w', encoding='utf-8') as f:
            for cnt in range(int(len(self.final) / 2)):
                f.write(self.final[cnt] + '\n')
                f.write(self.final[cnt + (int(len(self.final) / 2))] + '\n')




    def handler(self):
        self.featureHandler()
        self.popHandler()
        self.rapHandler()
        self.malletHandler()
        #print (self.rapCounter)
        #print (self.final)
        #print (self.features)
        #self.trainFileHandler()


a = Mallet()
a.handler()

