# -*- coding: cp1254 -*-
from Tkinter import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iotDB"]
mycol2=mydb["dht11"]

def listele():
    Lb1.delete(0,'end')
    kList=mycol2.find({},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)
      
def tarihgoster():
    tarih=tarih_veri.get()
    Lb1.delete(0,'end')
    kList=mycol2.find({"date":tarih},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)

def sicaklikbuyuk():
    sicaklik=int(sicaklik_veri.get())
    Lb1.delete(0,'end')
    kList=mycol2.find({"temp":{'$gt':sicaklik}},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)

def sicaklikkucuk():
    sicaklik=int(sicaklik_veri.get())
    Lb1.delete(0,'end')
    kList=mycol2.find({"temp":{'$lt':sicaklik}},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)

def nembuyuk():
    nem=int(nem_veri.get())
    Lb1.delete(0,'end')
    kList=mycol2.find({"hum":{'$gt':nem}},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)

def nemkucuk():
    nem=int(nem_veri.get())
    Lb1.delete(0,'end')
    kList=mycol2.find({"hum":{'$lt':nem}},{"_id": 0, "date": 1, "time": 1, "temp":1, "hum":1})
    for kayit in kList:
        mergeKayit=str(kayit["date"])+" "+str(kayit["time"])+" -> "+"Sicaklik:"+str(kayit["temp"])+"C"+" "+"Nem:"+str(kayit["hum"])+"%"
        Lb1.insert('end',mergeKayit)

master=Tk()
master.title("Sorgulama Islemleri")
si=Canvas(master, height=600, width=800)
si.pack()

frame_ust=Frame(master, bg="light blue")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.15)

frame_alt=Frame(master, bg="light blue")
frame_alt.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.7)

si1=Label(frame_ust, text="Sorgulama islemleri",bg="light blue", font="Verdena 20 bold")
si1.pack()

tarih=Label(frame_alt,text="Tarih :",bg="#add8e6",font="Verdena 10 bold")
tarih.pack(padx=10, pady=10, anchor=NW)

tarih_veri=Entry(frame_alt)
tarih_veri.place(x=80, y=10)

goster_btn=Button(frame_alt, text="Goster", command=tarihgoster)
goster_btn.place(x=255,y=10)

sicaklik=Label(frame_alt,text="Sicaklik :",bg="#add8e6",font="Verdena 10 bold")
sicaklik.pack(padx=10, pady=10, anchor=NW)

sicaklik_veri=Entry(frame_alt)
sicaklik_veri.place(x=80, y=50)

sicaklik_buyukolani_goster=Button(frame_alt, text="Buyuk Olani Goster", command=sicaklikbuyuk)
sicaklik_buyukolani_goster.place(x=255,y=50)

sicaklik_kucukolani_goster=Button(frame_alt, text="Kucuk Olani Goster", command=sicaklikkucuk)
sicaklik_kucukolani_goster.place(x=425,y=50)

nem=Label(frame_alt,text="Nem :",bg="#add8e6",font="Verdena 10 bold")
nem.pack(padx=10, pady=10, anchor=NW)

nem_veri=Entry(frame_alt)
nem_veri.place(x=80, y=90)

nem_buyukolani_goster=Button(frame_alt, text="Buyuk Olani Goster", command=nembuyuk)
nem_buyukolani_goster.place(x=255,y=90)

nem_kucukolani_goster=Button(frame_alt, text="Kucuk Olani Goster", command=nemkucuk)
nem_kucukolani_goster.place(x=425,y=90)

Lb1=Listbox(frame_alt, width=65)
Lb1.place(x=10, y=160)

listele=Button(frame_alt, text="Tumunu Listele", command=listele)
listele.place(x=10,y=130)

master.mainloop()
