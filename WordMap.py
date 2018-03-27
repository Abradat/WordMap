# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
from hazm import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import glob
import operator
import arabic_reshaper
from bidi.algorithm import get_display

class WorldMap():


    junks = ['و', '؛', '/', '.', '?', '؟', '!', '!', '[', ']', '،', 'از', 'به', 'که', 'در', 'تا', 'با', 'رو', 'بی', 'هر', 'چی', 'ایم', 'این', '', '', ]
    def __init__(self):
        self.normalizer =  Normalizer()

        #Pop Artists
        self.babakJDict = {}
        self.babakText = ""

        self.mohsenYDict = {}
        self.mohsenText = ""

        self.popDict = {}
        self.popText = ""

        #Rap Artists
        self.bahramDict = {}
        self.bahramText = ""

        self.hichkasDict = {}
        self.hichkasText = ""

        self.khalvatDict = {}
        self.khalvatText = ""

        self.qufDict = {}
        self.qufText = ""

        self.sorenaDict = {}
        self.sorenaText = ""

        self.rapDict = {}
        self.rapText = ""

        #Common, Diff
        self.commonDict = {}
        self.commonText = ""
        self.diffDict = {}
        self.diffText = ""


    def babakWorldMap(self):
        print "entered babak word map\n"
        path = "lyrics/pop/Babak Jahanbakhsh/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.babakText += ' ' + word
                        self.popText += ' ' + word

                        if word in self.babakJDict :
                            self.babakJDict[word] += 1
                            self.popDict[word] += 1
                        else :
                            self.babakJDict[word] = 1
                            self.popDict[word] = 1


        print "done\n\n"

    def mohsenWorldMap(self):
        print "entered mohsen word map\n"
        path = "lyrics/pop/Mohsen Yeganeh/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.mohsenText += ' ' + word
                        self.popText += ' ' + word

                        if word in self.mohsenYDict :
                            self.mohsenYDict[word] += 1
                            self.popDict[word] += 1
                        else :
                            self.mohsenYDict[word] = 1
                            self.popDict[word] = 1


        print "done\n\n"



    # Rappers Begin

    def hichkasWorldMap(self):
        print "entered hichkas word map\n"
        path = "lyrics/rap/Hichkas/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.hichkasText += ' ' + word
                        self.rapText += ' ' + word

                        if word in self.hichkasDict :
                            self.hichkasDict[word] += 1
                            self.rapDict[word] += 1
                        else :
                            self.hichkasDict[word] = 1
                            self.rapDict[word] = 1

        print "\n\n\n going to write to file"

        sortedHichkas = sorted(self.hichkasDict.items(), key=operator.itemgetter(1))

        print "done\n\n"

    def bahramWorldMap(self):
        print "entered bahram word map\n"
        path = "lyrics/rap/Bahram/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.bahramText += ' ' + word
                        self.rapText += ' ' + word

                        if word in self.bahramDict :
                            self.bahramDict[word] += 1
                            self.rapDict[word] += 1
                        else :
                            self.bahramDict[word] = 1
                            self.rapDict[word] = 1


        print "done\n\n"

    def khalvatWorldMap(self):
        print "entered khalvat word map\n"
        path = "lyrics/rap/Khalvat/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.khalvatText += ' ' + word
                        self.rapText += ' ' + word

                        if word in self.khalvatDict :
                            self.khalvatDict[word] += 1
                            self.rapDict[word] += 1
                        else :
                            self.khalvatDict[word] = 1
                            self.rapDict[word] = 1

        print "\n\n\n going to write to file"

        print "done\n\n"

    def qufWorldMap(self):
        print "entered quf word map\n"
        path = "lyrics/rap/Quf/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.qufText += ' ' + word
                        self.rapText += ' ' + word

                        if word in self.qufDict :
                            self.qufDict[word] += 1
                            self.rapDict[word] += 1
                        else :
                            self.qufDict[word] = 1
                            self.rapDict[word] = 1

        print "\n\n\n going to write to file"

        print "done\n\n"

    def sorenaWorldMap(self):
        print "entered sorena word map\n"
        path = "lyrics/rap/Sorena/*.txt"

        for filename in glob.glob(path):
            with io.open(filename, 'r', encoding="utf-8") as f:
                lyrics = f.readlines()
                text = ""

                for lyric in lyrics:
                    text += lyric

                text = self.normalizer.normalize(text)
                words = word_tokenize(text)

                for word in words :
                    if word not in self.junks:
                        self.sorenaText += ' ' + word
                        self.rapText += ' ' + word

                        if word in self.sorenaDict :
                            self.sorenaDict[word] += 1
                            self.rapDict[word] += 1
                        else :
                            self.sorenaDict[word] = 1
                            self.rapDict[word] = 1


        print "done\n\n"

    def commonDicts(self):
        for rapItem in self.rapDict :
            if( rapItem in self.popDict) :
                self.commonDict[rapItem] = min(self.rapDict[rapItem], self.popDict[rapItem])
                self.commonText += min(self.rapDict[rapItem], self.popDict[rapItem]) * (' ' + rapItem)

    def diffDicts(self):
        for rapItem in self.rapDict:
            if(rapItem in self.popDict and self.rapDict[rapItem] >= self.popDict[rapItem]):
                count = self.rapDict[rapItem] - self.popDict[rapItem]
            else :
                count = self.rapDict[rapItem]

            self.diffDict[rapItem] = count
            self.diffText += count * (' ' + rapItem)

        for popItem in self.popDict:
            if(popItem in self.rapDict and self.popDict[popItem] >= self.rapDict[popItem]):
                count = self.popDict[popItem] - self.rapDict[popItem]
            else:
                count = self.popDict[popItem]
            self.diffDict[popItem] = count
            self.diffText += count * (' ' + popItem)

    def sortDicts(self):
        print "Going to sort dictionaries\n"
        self.sortedBabak = sorted(self.babakJDict.items(), key=operator.itemgetter(1))
        self.sortedMohsen = sorted(self.mohsenYDict.items(), key=operator.itemgetter(1))
        self.sortedPop = sorted(self.popDict.items(), key=operator.itemgetter(1))

        self.sortedHichkas = sorted(self.hichkasDict.items(), key=operator.itemgetter(1))
        self.sortedBahram = sorted(self.bahramDict.items(), key=operator.itemgetter(1))
        self.sortedKhalvat = sorted(self.khalvatDict.items(), key=operator.itemgetter(1))
        self.sortedQuf = sorted(self.qufDict.items(), key=operator.itemgetter(1))
        self.sortedSorena = sorted(self.sorenaDict.items(), key=operator.itemgetter(1))
        self.sortedRap = sorted(self.rapDict.items(), key=operator.itemgetter(1))

        self.sortedCommon = sorted(self.commonDict.items(), key=operator.itemgetter(1))
        self.sortedDiff = sorted(self.diffDict.items(), key=operator.itemgetter(1))

        print "done\n\n"

    def reshaper(self):
        self.popText = arabic_reshaper.reshape(self.popText)
        self.popText = get_display(self.popText)

        self.rapText = arabic_reshaper.reshape(self.rapText)
        self.rapText = get_display(self.rapText)

        self.babakText = arabic_reshaper.reshape(self.babakText)
        self.babakText = get_display(self.babakText)

        self.mohsenText = arabic_reshaper.reshape(self.mohsenText)
        self.mohsenText = get_display(self.mohsenText)

        self.hichkasText = arabic_reshaper.reshape(self.hichkasText)
        self.hichkasText = get_display(self.hichkasText)

        self.bahramText = arabic_reshaper.reshape(self.bahramText)
        self.bahramText = get_display(self.bahramText)

        self.khalvatText = arabic_reshaper.reshape(self.khalvatText)
        self.khalvatText = get_display(self.khalvatText)

        self.qufText = arabic_reshaper.reshape(self.qufText)
        self.qufText = get_display(self.qufText)

        self.sorenaText = arabic_reshaper.reshape(self.sorenaText)
        self.sorenaText = get_display(self.sorenaText)

        self.commonText = arabic_reshaper.reshape(self.commonText)
        self.commonText = get_display(self.commonText)


        self.diffText = arabic_reshaper.reshape(self.diffText)
        self.diffText = get_display(self.diffText)

    def wordCloudShow(self, num):
        if(num == 1):
            babakWorldCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            babakWorldCloud.generate(self.babakText)
            plt.imshow(babakWorldCloud)
            plt.axis("off")
            plt.show()

        elif(num == 2):
            mohsenWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            mohsenWordCloud.generate(self.mohsenText)
            plt.imshow(mohsenWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 3):
            popWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            popWordCloud.generate(self.popText)
            plt.imshow(popWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 4):
            hichkasWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            hichkasWordCloud.generate(self.hichkasText)
            plt.imshow(hichkasWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 5):
            bahramWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            bahramWordCloud.generate(self.bahramText)
            plt.imshow(bahramWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 6):
            khalvatWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            khalvatWordCloud.generate(self.khalvatText)
            plt.imshow(khalvatWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 7):
            qufWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            qufWordCloud.generate(self.qufText)
            plt.imshow(qufWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 8):
            sorenaWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            sorenaWordCloud.generate(self.sorenaText)
            plt.imshow(sorenaWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 9):
            rapWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            rapWordCloud.generate(self.rapText)
            plt.imshow(rapWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 10):
            commonWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            commonWordCloud.generate(self.commonText)
            plt.imshow(commonWordCloud)
            plt.axis("off")
            plt.show()

        elif(num == 11):
            diffWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
            diffWordCloud.generate(self.diffText)
            plt.imshow(diffWordCloud)
            plt.axis("off")
            plt.show()

    def handler(self):
        self.babakWorldMap()
        self.mohsenWorldMap()
        self.hichkasWorldMap()
        self.bahramWorldMap()
        self.khalvatWorldMap()
        self.qufWorldMap()
        self.sorenaWorldMap()

        self.commonDicts()
        self.diffDicts()

        self.sortDicts()

        self.reshaper()
        self.wordCloudShow(11)





        #for key in self.sortedCommon:
        #    print (key[0] + "is : " + str(key[1]) + "\n")



a = WorldMap()
a.handler()

