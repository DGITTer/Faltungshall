from WaveFile import WaveFile
import threading

class Paths(object):
    
    __path = str
    __ym1path = str
    __ym2path = str
    __mh1path = str
    __mh2path = str

    def __init__(self, path):
        self.__path = path
        self.__ym1path = path + 'minster1_000_ortf_48k.wav'
        self.__ym2path = path + 'minster1_bformat_48k.wav'
        self.__mh1path = path + 'mh3_000_ortf_48k.wav'
        self.__mh2path = path + 'mh3_000_bformat_48k.wav'

    def getYM1(self):
        return self.__ym1path

    def getYM2(self):
        return self.__ym2path

    def getMH1(self):
        return self.__mh1path

    def getMH2(self):
        return self.__mh2path

# Damit man nicht alle Paths für jeden PC neu angeben muss
paths = Paths('C:\\Users\\david\\Source\\Repos\\Faltungshall\\Faltungshall\\Samples\\')

YM1 = WaveFile(paths.getYM1())
YM2 = WaveFile(paths.getYM2())
MH1 = WaveFile(paths.getMH1())
MH2 = WaveFile(paths.getMH2())

YM1.plot()

#MH1.plot()
#MH2.plotFrequencySpectre()




