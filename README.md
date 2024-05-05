Script que revisa los canales rss de un archivo y te notifica por bot de telegram de nuevas noticias, almacenando en una base datos las noticias notificadas para no duplicar
**Creacion de la base de datos**
```mysql
create database rss_feed;
use rss_feed;
create table rss (id INT NOT NULL AUTO_INCREMENT, url VARCHAR(1000),PRIMARY KEY (id));
```

**Requerimientos**
pip install feedparser requests telebot json mysql-connector

**revisar los datos del config.json**
