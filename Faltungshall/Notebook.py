from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

#PI2 = 2 * np.pi

np.set_printoptions(precision=3, suppress=True)


dirac = thinkdsp.read_wave('./Samples/dirac.wav')
#dirac.normalize()
n = 480000 - dirac.__len__()
dirac.zero_pad(dirac.__len__() + n)
dirac.make_audio()
d_spektrum = dirac.make_spectrum()
print("test: " + str(dirac.__len__()))


ym_antwort = thinkdsp.read_wave('./Samples/minster1_000_ortf_48k.wav')
ym_antwort.make_audio()


#ym_antwort.normalize()
#ym_antwort.truncate(48000*2)
#ym_antwort.zero_pad(480000)
ym_antwort.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])
np.set_printoptions(threshold=100)

#ym_antwort.zero_pad(ym_antwort.__len__() + 48000)
print(ym_antwort.__len__())
print(ym_antwort.duration)
print(ym_antwort.ys)
ym_antwort.make_audio()


ym_spektrum = ym_antwort.make_spectrum()
print(ym_spektrum.hs.__len__())
print(ym_spektrum.fs.__len__())
#print(ym_spektrum.hs)
ym_spektrum.plot()
thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')


mh_antwort = thinkdsp.read_wave('./Samples/mh3_000_ortf_48k.wav')
#mh_antwort.normalize()
n = 480000 - mh_antwort.__len__()
mh_antwort.zero_pad(mh_antwort.__len__() + n)
mh_antwort.make_audio()



mh_spektrum = mh_antwort.make_spectrum()



aufnahme = thinkdsp.read_wave('./Samples/aufnahme3.wav')

aufnahme.make_audio()



#aufnahme.normalize()
print(480000 - aufnahme.__len__())
n = 480000 - aufnahme.__len__()
#aufnahme.zero_pad(aufnahme.__len__() + n)
aufnahme.truncate(480000)
print(aufnahme.__len__())
print(aufnahme.duration)



aufnahme.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])



aufnahme_spectrum = aufnahme.make_spectrum()
aufnahme_spectrum.plot()
thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')



ym_faltung_spektrum = aufnahme_spectrum * ym_spektrum
ym_faltung_spektrum.plot()
thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')



ym_faltung_welle = ym_faltung_spektrum.make_wave()
#ym_faltung_welle.normalize()
ym_faltung_welle.write('YM_Ergebnis.wav')
ym_faltung_welle.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])



ym_faltung_welle.make_audio()



mh_faltung_spektrum = aufnahme_spectrum * mh_spektrum
mh_faltung_welle = mh_faltung_spektrum.make_wave()
#mh_faltung_welle.normalize()
mh_faltung_welle.write('MH_Ergebnis.wav')
mh_faltung_welle.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])



mh_faltung_welle.make_audio()





d_faltung_spektrum = aufnahme_spectrum * d_spektrum
d_faltung_welle = d_faltung_spektrum.make_wave()
#d_faltung_welle.normalize()
d_faltung_welle.write('D_Ergebnis.wav')
#d_faltung_welle.plot()
#thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])

#d_faltung_welle = aufnahme.convolve(dirac)
#print(d_faltung_welle.__len__())
#d_faltung_welle.write('D_Ergebnis.wav')










#########################################################################


##%matplotlib inline

#import numpy as np
#import matplotlib.pyplot as plt
#import wave
#from pylab import*
##from scipy.io import wavfile
##import WaveFile
##import wavio

##from __future__ import print_function, division

#import thinkdsp
#import thinkplot

#import numpy as np
#import pandas as pd

#import warnings
#warnings.filterwarnings('ignore')

#PI2 = 2 * np.pi

#np.set_printoptions(precision=3, suppress=True)
##%matplotlib inline

#response = thinkdsp.read_wave('./Samples/minster1_000_ortf_48k.wav')
#response.make_audio()
##start = 0.12
##response = response.segment(start=start)
##response.shift(-start)

#response.normalize()
##response.zero_pad(response.__len__() + 48000)
#response.plot()
#thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])
#np.set_printoptions(threshold=100)

##response.zero_pad(response.__len__() + 48000)
#print(response.__len__())
#print(response.duration)
#print(response.ys)

#response.make_audio()

#transfer = response.make_spectrum()
#transfer.plot()
#thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')

#aufnahme = thinkdsp.read_wave('./Samples/sprachaufnahme.wav')

#aufnahme.make_audio()

#aufnahme.normalize()
## print(480000 - aufnahme.__len__())
## n = 480000 - aufnahme.__len__()
## aufnahme.zero_pad(aufnahme.__len__() + n)
#print(aufnahme.__len__())
#print(aufnahme.duration)
#aufnahme.plot()
#thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])

#aufnahme_spectrum = aufnahme.make_spectrum()
#aufnahme_spectrum.plot()
#thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')

#aufnahme_spectrum = aufnahme.make_spectrum()
#aufnahme_spectrum.plot()
#thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')

## result2.normalize()
#result2 = result.make_wave()
#result2.make_audio()
#result2.write('Ergebnis.wav')