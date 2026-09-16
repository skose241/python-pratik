"""
ogrenciler=[
    {"ad":"Ali","puan":60,"durum":None},
    {"ad":"Veli","puan":80,"durum":None},
    {"ad":"Zeynep","puan":40,"durum":None}
]

for ogrenci in ogrenciler:
    if ogrenci["puan"]>=50:
        ogrenci["durum"]=True
    else:
        ogrenci["durum"]=False


    if ogrenci["durum"]==True:
        print(ogrenci["ad"])
"""



"""
liste=[
    {"ad":"elma","fiyat":15.20,"stok":True},
    {"ad":"armut","fiyat":13.60,"stok":False},
    {"ad":"kiraz","fiyat":10,"stok":True},
    {"ad":"çilek","fiyat":17.80,"stok":True},
    {"ad":"karpuz","fiyat":20.30,"stok":False}
]

tutar=0
for alisveris in liste:
    if alisveris["stok"]==True:
        tutar+=alisveris["fiyat"]

print(tutar)
"""



"""
ogrenciler=[
    {"ad":"Ali","notlar":[70,85,60]},
    {"ad":"Veli","notlar":[40,55,35]},
    {"ad":"Zeynep","notlar":[90,75,80]}
]

for ogrenci in ogrenciler:
    ogrenci["toplam"]=0
    i=0

    for puan in ogrenci["notlar"]:
        ogrenci["toplam"]+=puan
        i+=1

    ogrenci["ortalama"]=ogrenci["toplam"]/i

    if ogrenci["ortalama"]>60:
        print(ogrenci["ad"])
"""



"""
secilen_dersler=["matematik","fizik","matematik","kimya","fizik","biyoloji","kimya"]

dersler=set(secilen_dersler)

print(len(dersler))
"""



def ortalama_hesaplama(notlar):
    return sum(notlar)/len(notlar)

ogrenciler=[
    {"ad":"Ali","notlar":[70, 85, 60]},
    {"ad":"Veli","notlar":[40, 55, 35]},
    {"ad":"Zeynep","notlar":[90, 75, 80]}
]

with open("ogrenciler.txt","w",encoding="utf-8") as dosya:
    for ogrenci in ogrenciler:
        ortalama=ortalama_hesaplama(ogrenci["notlar"])

        dosya.write(ogrenci["ad"]+" "+str(ortalama)+"\n")

with open("ogrenciler.txt","r",encoding="utf-8") as dosya:
    for satir in dosya:
        kelime=satir.strip().split()

        print("Ad:",kelime[0])
        print("Ortalama:",kelime[1])
        