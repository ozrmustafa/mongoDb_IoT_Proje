# -*- coding: cp1254 -*-
from Tkinter import *
import tkMessageBox
import pymongo
import subprocess

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iotDB"]
mycol1=mydb["users"]

master=Tk()
master.title("Kullanici Girisi")
giris=Canvas(master, height=300, width=500)
giris.pack()

frame_ust=Frame(master, bg="light blue")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt=Frame(master, bg="light blue")
frame_alt.place(relx=0.1,rely=0.21, relwidth=0.8, relheight=0.6)

ust_baslik=Label(frame_ust, bg="#add8e6", text="Kullanici Girisi", font="Verdana 15 bold")
ust_baslik.pack()

kullanici_adi=Label(frame_alt, bg="#add8e6", text="Kullanici Adi :", font="Verdana 10 bold")
kullanici_adi.pack(padx=10, pady=10, anchor=NW)

sifre=Label(frame_alt, bg="#add8e6", text="Sifre :", font="Verdana 10 bold")
sifre.pack(padx=10, pady=10, anchor=NW)

kullanici_text=Entry()
kullanici_text.place(x=170,y=75)

sifre_text=Entry()
sifre_text.place(x=170,y=110)

def girisyap():
    giris=False
    parola=sifre_text.get()
    kadi=kullanici_text.get()
    myquery1={'$and':[{"user":kadi}, {"password":parola}]}
    kList=mycol1.find(myquery1)             
    for kayit in kList:
        print(len(kayit))
        if len(kayit)>0:
            giris=True
            tkMessageBox.showinfo("Bilgi", "Giris basarili")
            master.destroy()
            p=subprocess.Popen(["python","takip.py"])          
    if giris==False:
        tkMessageBox.showinfo("Uyari", "Giris basarisiz")

def kullaniciVarMi():
    varMi=False
    kadi=kullanici_text.get()
    myquery1={"user":kadi}
    kList=mycol1.find(myquery1)             
    for kayit in kList:
        print(len(kayit))
        if len(kayit)>0:
            varMi=True
            return varMi        
    return False

def kullaniciekle():
    if not kullaniciVarMi():
        parola=sifre_text.get()
        kadi=kullanici_text.get()
        yenikayit={"user":kadi, "password":parola}
        mycol1.insert_one(yenikayit)
        tkMessageBox.showinfo("Bilgi", "Kayit basarili")
        sifre_text.delete(0,'end')
        kullanici_text.delete(0,'end')
    else:
        tkMessageBox.showinfo("Uyari", "Kullanici kayitli.\ntekrar kaydedilemez.")
        
def parolaguncelle():
    parola=sifre_text.get()
    kadi=kullanici_text.get()
    myquery={"user":kadi}
    yenideger={'$set':{"password":parola}}
    mycol1.update_one(myquery,yenideger)
    tkMessageBox.showinfo("Bilgi", "Parola guncellendi")
    sifre_text.delete(0,'end')
    kullanici_text.delete(0,'end')

def kullanicisil():
    kadi=kullanici_text.get()
    myquery={"user":kadi}
    mycol1.delete_one(myquery)
    tkMessageBox.showinfo("Bilgi", "Kullanici silindi")
    kullanici_text.delete(0,'end')

girisbtn=Button(frame_alt, text="Giris", fg="black", command=girisyap)
girisbtn.place(x=120,y=90)

kullanicieklebtn=Button(frame_alt, text="Kullanici Ekle", command=kullaniciekle)
kullanicieklebtn.place(x=20,y=150)

parolaguncellebtn=Button(frame_alt, text="Parola Guncelle", command=parolaguncelle)
parolaguncellebtn.place(x=145,y=150)

kullanicisilbtn=Button(frame_alt, text="Kullanici Sil", command=kullanicisil)
kullanicisilbtn.place(x=285,y=150)

master.mainloop()
