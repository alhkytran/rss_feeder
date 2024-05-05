import feedparser
import requests
import enviar
import hoy
from datetime import datetime

formato = "%a, %d %b %Y %H:%M:%S %z"
def check_fecha (fecha):
    with open("fecha_anterior.txt","r") as fechita:
        aux=fechita.readlines()
    fechanterior=aux[0].split("\n")[0]
    global formato
    dia1 = datetime.strptime(fecha, formato)
    dia2 = datetime.strptime(fechanterior, formato)
    if dia2 < dia1:
        return True
    else:
        return False

def check_feed():
    archivo=open("rss_file.txt","r")
    RSS_FEEDS=[]
    for i in archivo:
        RSS_FEEDS.append(i.split("\n")[0])
        new_entries = []
        for feed_url in RSS_FEEDS:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                dia= entry.published
                compara=check_fecha(dia)
                if compara:
                   new_entries.append(entry)
    
    if new_entries:
        for entry in new_entries:
            message = f"{entry.title}\n{entry.link}"
            #print(message)
            enviar.envia(message)
    archivo.close()
if __name__ == '__main__':
    check_feed()
    hoy.hoy()
    
