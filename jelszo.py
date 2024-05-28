# min 8 karakter
# kisbetű, nagybetű, szám, spec.kar
# 1 mo. with random
import random
betuk = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]
jelek = ['!', '?', '#', '<', '>', ',', '.']
szamok = [str(i) for i in range(10)]

betuk_db, jelek_db, szamok_db =4,2,2

jelszo = []

for i in range (betuk_db):
    jelszo.append(random.choice(betuk))
for i in range (jelek_db):
    jelszo.append(random.choice(jelek))
for i in range (szamok_db):
    jelszo.append(random.choice(szamok))

random.shuffle(jelszo)
print(*jelszo,sep='') # izgi es uj