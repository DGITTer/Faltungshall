from datetime import datetime

epoch = datetime(1970,1,1)

d1 = datetime.utcnow()
t1 = (d1 - epoch).total_seconds()

aufnahme_spectrum = aufnahme.make_spectrum()
ym_spektrum = ym_antwort.make_spectrum()
ym_faltung_spektrum = aufnahme_spectrum * ym_spektrum
ym_faltung_welle = ym_faltung_spektrum.make_wave()

d2 = datetime.utcnow()
t2 = (d2 - epoch).total_seconds()

result = t2- t1
print(result)

d1 = datetime.utcnow()
t1 = (d1 - epoch).total_seconds()

ym_faltung_welle = aufnahme.convolve(ym_antwort)

d2 = datetime.utcnow()
t2 = (d2 - epoch).total_seconds()

result = t2- t1
print(result)