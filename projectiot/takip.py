# -*- coding: cp1254 -*-
from Tkinter import *
import pymongo
import RPi.GPIO as GPIO
import dht11
import time
import os
from datetime import datetime
from threading import Thread
import subprocess
import urllib

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 14)
API_KEY = "53GO6CS5HSOUWN0U"

def sorgula():
    master.destroy()
    import sorgulama

say=0

def sensoroku():
    try:
        global say
        while True:
            result = instance.read()
            if result.is_valid():
                simdi=datetime.now()
                tarih = simdi.strftime("%d/%m/%Y")
                zaman=simdi.strftime("%H:%M:%S")
                tarih_saatgiris.delete(0,'end')
                tarih_saatgiris.insert(0,tarih+" "+zaman)
                sicaklik=result.temperature
                sicaklikgiris.delete(0,'end')
                sicaklikgiris.insert(0,sicaklik)
                nem=result.humidity
                nemgiris.delete(0,'end')
                nemgiris.insert(0,nem)
                mycol2=mydb["dht11"]
                dht11dict = { "date": tarih, "time":zaman, "temp":sicaklik, "hum":nem}
                mycol2.insert_one(dht11dict)
                client = urllib.urlopen("https://api.thingspeak.com/update?api_key={}&field1={}&field2={}". format(API_KEY, sicaklik, nem))
                
                if say==0:
                    p=subprocess.Popen(["python","grafik.py"])
                    r=subprocess.Popen(["chromium-browser","grafikler.html"])
                    time.sleep(1)
                say=1
            time.sleep(2)
    except:
        pass

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iotDB"]
mycol2=mydb["dht11"]

master=Tk()
master.title("Sicaklikk nem takibi")
giris=Canvas(master, height=500, width=900)
giris.pack()

frame_ust=Frame(master, bg="light blue")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt1=Frame(master, bg="light blue")
frame_alt1.place(relx=0.1, rely=0.21, relwidth=0.8, relheight=0.6)

stn=Label(frame_ust, text="Sicaklik Nem Takibi",bg="#add8e6",font="Verdena 20 bold")
stn.pack(padx=10,pady=10)

tarih_saat=Label(frame_alt1, text="Tarih Ve Saat :",bg="#add8e6",font="Verdena 12 bold")
tarih_saat.pack(padx=10,pady=10, anchor=NW)

sicaklik=Label(frame_alt1, text="Sicaklik :",bg="#add8e6",font="Verdena 12 bold")
sicaklik.pack(padx=10,pady=10, anchor=NW)

nem=Label(frame_alt1, text="Nem :",bg="#add8e6",font="Verdena 12 bold")
nem.pack(padx=10,pady=10, anchor=NW)

tarih_saatgiris=Entry(frame_alt1)
tarih_saatgiris.place(x=150,y=11)

nemgiris=Entry(frame_alt1)
nemgiris.place(x=150,y=106)

sicaklikgiris=Entry(frame_alt1)
sicaklikgiris.place(x=150,y=56)

sorgulama_islem=Button(frame_alt1, text="Sorgulama islemleri", fg="black", command=sorgula)
sorgulama_islem.place(x=150,y=150)

sensor=Thread(target=sensoroku)
sensor.deamon = True
sensor.start()

master.mainloop()
