from datetime import datetime
from dateutil import tz

def hoy ():
    formato = "%a, %d %b %Y %H:%M:%S %z"
    now = datetime.now()
    timezone = tz.gettz('Europe/Madrid')  # Ejemplo para obtener la zona horaria de India
    now = now.astimezone(timezone)
    formatted_date = now.strftime(formato)
    print(formatted_date)
    archivo=open("fecha_anterior.txt","w")
    archivo.write(formatted_date)
    archivo.close()

