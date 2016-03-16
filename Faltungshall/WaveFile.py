from matplotlib import pylab
import numpy as np
from Helper import *
from pylab import *
from builtins import Exception

class WaveFile(object):
    
    __path = str
    __fr = int # Frame Rate
    __sw = int # Sample Width
    __a = np.array # Array
    __ch = np.array # channel
    __fs = np.array

    def getFS(self):
        return self.__fs
    
    def __init__(self, path):   
        self.__path = path;   
        try:
            self.__fr, self.__sw, self.__a = readwav(self.__path)
        except :
            print('Lesen der Datei: "' + self.__path + '" schlug fehl!') 
            quit()
        self.__ch = self.__a[:,0]
        self.__fs = np.fft.fft(self.__ch)
          
    def plot(self):
        self.__ch = self.__a[:,0]
        self.__ch = self.__ch / (2. ** (self.__sw * 8 - 1)) # 3 Byte * 8 Bit - 1 (weil bereich -2^23 - (2^23)-1)
        timeArray = np.linspace(0, len(self.__ch) / self.__fr, num = len(self.__ch))
        plt.plot(timeArray, self.__ch)
        plt.ylabel('Amplitude')
        plt.xlabel('Time (s)')
        plt.title(self.__path)
        plt.show()

    def print(self):
        print("Filename: " + self.__path)
        print("FrameRate: " + str(self.__fr))
        print("Sample width in bytes: " + str(self.__sw))
        print("Array: " + str(self.__a))  
        print("Laenge des Samples (a.shape[0] / fr): " + str((self.__a.shape[0] / self.__fr)))
        print("Abtastrate (a.shape[0]): " + str(self.__a.shape[0]))
        print("Channels (a.shape[1]): " + str(self.__a.shape[1]))

    def fft(self):
        print("Länge des Channels: " + str(self.__ch).__len__())
        print("Frequenz Spektrum" + str(self.__fs))
        print("Länge des Frequenz Spektrums" + self.__fs.__len__())

    def plotFrequencySpectre(self):
        lenCh = self.__ch.__len__()
        nUniquePts = np.ceil((lenCh+1)/2.0)
        p = self.__fs[0:nUniquePts]
        p = abs(p)

        p = p / float(lenCh) # scale by the number of points so that
        # the magnitude does not depend on the length 
        # of the signal or on its sampling frequency  
        p = p**2  # square it to get the power 

        # multiply by two (see technical document for details)
        # odd nfft excludes Nyquist point
        if lenCh % 2 > 0: # we've got odd number of points fft
            p[1:len(p)] = p[1:len(p)] * 2
        else:
            p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

        freqArray = np.arange(0, nUniquePts, 1.0) * (self.__fr / lenCh);
        #plot(freqArray/1000, 10*log10(p), color='k')
        #xlabel('Frequency (kHz)')
        #ylabel('Power (dB)')
        #freqArray = np.linspace(0, len(self.__ch) / self.__fr, num = len(self.__ch))
        plt.plot(freqArray, self.__fs)
        plt.show()


