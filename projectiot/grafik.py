import Tkinter as tk
import pymongo
from threading import Thread
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iotDB"]
mycol2=mydb["dht11"]

root = tk.Tk()
root.title("Son 5 Sicaklik")
c_width = 400
c_height = 350
c = tk.Canvas(root, width=c_width, height=c_height, bg= 'white')
c.pack()

def sensoroku():
    try:        
        while True:            
            data=[]
            c.delete("all")
            kList=mycol2.find().limit(5).sort('_id',-1)
            for kayit in kList:
                data.append(int(kayit['temp']))   
         
            y_stretch = 5
            y_gap = 10
            x_stretch = 10
            x_width = 40
            x_gap = 10

            for x, y in enumerate(data):
                x0 = x * x_stretch + x * x_width + x_gap
                y0 = c_height - (y * y_stretch + y_gap)
                x1 = x * x_stretch + x * x_width + x_width + x_gap
                y1 = c_height - y_gap
                c.create_rectangle(x0, y0, x1, y1, fill="red")
                c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
            time.sleep(2)
    except:
        pass

sensor=Thread(target=sensoroku)
sensor.deamon = True
sensor.start()

root.mainloop()
