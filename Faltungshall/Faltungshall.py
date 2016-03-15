from WaveFile import WaveFile
import threading

ym1path = 'C:\\Users\\terihad\\documents\\visual studio 2015\\Projects\\Faltungshall\\Faltungshall\\Samples\\minster1_000_ortf_48k.wav'
ym2path = 'C:\\Users\\terihad\\documents\\visual studio 2015\\Projects\\Faltungshall\\Faltungshall\\Samples\\minster1_bformat_48k.wav'
mh1path = 'C:\\Users\\terihad\\documents\\visual studio 2015\\Projects\\Faltungshall\\Faltungshall\\Samples\\mh3_000_ortf_48k.wav'
mh2path = 'C:\\Users\\terihad\\documents\\visual studio 2015\\Projects\\Faltungshall\\Faltungshall\\Samples\\mh3_000_bformat_48k.wav'

YM1 = WaveFile(ym1path)
YM2 = WaveFile(ym2path)
MH1 = WaveFile(mh1path)
MH2 = WaveFile(mh2path)



#MH1.plot()
MH2.plotFrequencySpectre()




