# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
from hazm import *
import glob
import math
import operator


class Smooth():


    junks = ['و', '؛', '/', '.', '?', '؟', '!', '!', '[', ']', '،', 'از', 'به', 'که', 'در', 'تا', 'با', 'رو', 'بی', 'هر', 'چی', 'ایم', 'این', '', '', ]
    def __init__(self):
        self.normalizer =  Normalizer()

        self.popDict = {}
        self.popText = ""
        self.wordProbPop = {}

        self.rapDict = {}
        self.rapText = ""
        self.wordProbRap = {}

        self.totalDict = {}
        self.featureImpact = {}

        self.totalTokens = 0
        self.rapTokens = 0
        self.popTokens = 0

        self.rapMeasure = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
        self.popMeasure = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}



    def pop(self):
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

                    for word in words:
                        if word not in self.junks:
                            self.popText += ' ' + word
                            self.totalTokens += 1
                            self.popTokens += 1

                            if word in self.popDict:
                                self.popDict[word] += 1
                            else:
                                self.popDict[word] = 1

                            if word in self.totalDict :
                                self.totalDict[word] += 1
                            else :
                                self.totalDict[word] = 1

    def rap(self):
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

                    for word in words:
                        if word not in self.junks:
                            self.rapText += ' ' + word
                            self.totalTokens += 1
                            self.rapTokens += 1

                            if word in self.rapDict:
                                self.rapDict[word] += 1
                            else:
                                self.rapDict[word] = 1

                            if word in self.totalDict:
                                self.totalDict[word] += 1
                            else:
                                self.totalDict[word] = 1


    def dictHandler(self):
        for item in self.totalDict :
            if(item in self.popDict):
                self.wordProbPop[item] = math.log((self.popDict[item] + 1) * 1.0 / (len(self.popDict) + self.totalTokens), 10)
            else :
                self.wordProbPop[item] = math.log(1.0 / (len(self.popDict) + self.totalTokens), 10)

            if(item in self.rapDict):
                self.wordProbRap[item] = math.log((self.rapDict[item] + 1) * 1.0 / (len(self.rapDict) + self.totalTokens), 10)
            else :
                self.wordProbRap[item] = math.log(1.0 / (len(self.rapDict) + self.totalTokens), 10)

    def testHandler(self):

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

                    #print(self.rapTokens , self.popTokens, self.totalTokens)
                    rap = math.log(self.rapTokens / self.totalTokens)
                    pop = math.log(self.popTokens / self.totalTokens)

                    for lyric in lyrics:
                        text += lyric

                    text = self.normalizer.normalize(text)
                    words = word_tokenize(text)

                    for word in words :
                        if(word not in self.junks and word in self.totalDict):
                            rap += self.wordProbRap[word]
                            pop += self.wordProbPop[word]
                            self.featureImpact[word] = abs(self.wordProbPop[word] - self.wordProbRap[word])

                    if(rap > pop):
                        if('rap' in filename) :
                            self.rapMeasure['tp'] += 1
                            self.popMeasure['tn'] += 1
                        else :
                            self.rapMeasure['fp'] += 1
                            self.popMeasure['fn'] += 1
                    else :

                        if('rap' in filename):
                            self.rapMeasure['fn'] += 1
                            self.popMeasure['fp'] += 1
                        else :
                            self.rapMeasure['tn'] += 1
                            self.popMeasure['tp'] += 1
                    #print (sorted(self.featureImpact.items(), key= operator.itemgetter(1))[0:10])

        print
        print ('Rap Precision : ', self.rapMeasure['tp'] / (self.rapMeasure['tp'] + self.rapMeasure['fp']))
        print ('Rap Recall : ', self.rapMeasure['tp'] / (self.rapMeasure['tp'] + self.rapMeasure['tn']))

        print ('Pop Precision : ', self.popMeasure['tp'] / (self.popMeasure['tp'] + self.popMeasure['fp']))
        print ('Pop Recall : ', self.popMeasure['tp'] / (self.popMeasure['tp'] + self.popMeasure['tn']))

        with open('features.txt', 'w', encoding='utf-8') as f:
            for word in self.featureImpact:
                f.write(word + '\n')

    def handler(self):
        self.pop()
        self.rap()
        self.dictHandler()
        self.testHandler()


a = Smooth()
a.handler()

