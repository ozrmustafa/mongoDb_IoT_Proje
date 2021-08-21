#Bu kod veritabani ve tablolarinin olusturulmasi icin sadece bir kereye mahsus calistirilmalidir.

import pymongo
from datetime import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/") #mongodb istemcisi
mydb = myclient["iotDB"] #veritabani 

#kullanici olusturma
mycol1=mydb["users"] #kullanici tablosu gibi
usersdict = { "user": "admin", "password": "1234" }
mycol1.insert_one(usersdict)

#sensor verileri saklama
simdi=datetime.now()
tarih = simdi.strftime("%d/%m/%Y")
zaman=simdi.strftime("%H:%M:%S")
mycol2=mydb["dht11"] #sensor tablosu gibi
dht11dict = { "date": tarih, "time":zaman, "temp":0, "hum":0}
mycol2.insert_one(dht11dict)

