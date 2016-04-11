from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

PI2 = 2 * np.pi

np.set_printoptions(precision=3, suppress=True)


###


response = thinkdsp.read_wave('./Samples/minster1_000_ortf_48k_44100.wav')

start = 0.12
response = response.segment(start=start)
response.shift(-start)

response.normalize()
response.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])


###


response.make_audio()



###



transfer = response.make_spectrum()
transfer.plot()
thinkplot.config(xlabel='Frequency (Hz)', ylabel='Amplitude')



###



violin = thinkdsp.read_wave('./Samples/aufnahme3_44100.wav')

start = 0.11
violin = violin.segment(start=start)
violin.shift(-start)

violin.truncate(len(response))
violin.normalize()
violin.plot()
thinkplot.config(xlabel='Time (s)', ylim=[-1.05, 1.05])



###



violin.make_audio()



###




spectrum = violin.make_spectrum()




###




len(spectrum.hs), len(transfer.hs)



###



output = (spectrum * transfer).make_wave()
output.normalize()



###



violin.plot()



###



output.plot()



###



output.make_audio()

output.write('test.wav')