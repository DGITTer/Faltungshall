#!/usr/bin/env python
# -*- coding: utf-8 -*-from WaveFile import WaveFile

from WaveFile import *
#from scipy import signal

class Paths(object):
    
    __path = str
    __ym1path = str
    __ym2path = str
    __mh1path = str
    __mh2path = str
    __aufnahme = str

    def __init__(self, path):
        self.__path = path
        self.__ym1path = path + 'minster1_000_ortf_48k.wav'
        self.__ym2path = path + 'minster1_bformat_48k.wav'
        self.__mh1path = path + 'mh3_000_ortf_48k.wav'
        self.__mh2path = path + 'mh3_000_bformat_48k.wav'
        self.__aufnahme = path + 'sprachaufnahme.wav'

    def getYM1(self):
        return self.__ym1path

    def getYM2(self):
        return self.__ym2path

    def getMH1(self):
        return self.__mh1path

    def getMH2(self):
        return self.__mh2path

    def getAufnahme(self):
        return self.__aufnahme

# Damit man nicht alle Paths für jeden PC neu angeben muss
# YM1 = 'minster1_000_ortf_48k.wav'
# YM2 = 'minster1_bformat_48k.wav'
# MH1 = 'mh3_000_ortf_48k.wav'
# MH2 = 'mh3_000_bformat_48k.wav'
# Aufnahme = 'sprachaufnahme.wav'

paths = Paths('Samples\\')

YM1 = WaveFile(paths.getYM1())
YM2 = WaveFile(paths.getYM2())
MH1 = WaveFile(paths.getMH1())
MH2 = WaveFile(paths.getMH2())
Aufnahme = WaveFile(paths.getAufnahme())

#YM1.printAttributes()
## h = convolve(Aufnahme.getChannel(), YM1.getChannel(), mode='same')
#g = signal.fftconvolve(Aufnahme.getChannel(), YM1.getChannel(), mode='same') / sum(YM1.getChannel())
## print(h)
#print("Framerates: Aufnahme, Sample", Aufnahme.getFramerate(), YM1.getFramerate())
#print(Aufnahme.getFramerate())
#print(YM1.getFramerate())
## writewav24("Samples/output.wav", YM1.getFramerate(), h)
#writewav24("Samples/output.wav", YM1.getFramerate(), YM1.getChannel())
#writewav24("Samples/output2.wav", YM1.getFramerate(), g)
## Aufnahme.printAttributes()
##var = Aufnahme.getFS() * YM1.getFS()
##print(var.__len__())
##Aufnahme.plot()

Aufnahme.printAttributes()
#

#YM1.plot()

#MH1.plot()
#MH2.plotFrequencySpectre()




