# ThuoclaoPing

``A ThuocLaoPing written in Python (Work-In-Progress)``
 
Environment 
-----------
python3.6
```sh
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:jonathonf/python-3.6
Press [ENTER] to continue or ctrl-c to cancel adding it
apt-get update
apt-get install python3.6
```

Install
-------

Clone source code and install dependences:

```
apt update && apt install -y python3-pip fping redis-server mysql-server-5.7 mysql-client-core-5.7 libmysqlclient-dev
git clone https://github.com/locvx1234/ThuoclaoPing
mkdir /code
cp -r ThuoclaoPing/* /code
cd /code
pip3 install -r requirements.txt
```
If you see a error log:

```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/locale.py", line 531, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
```

then you run:

```sh
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
```

Mysql:

Start mysql-server

```
systemctl restart mysql.service
```
Create database `thuoclao`

```sh
mysql -u root -p
> CREATE DATABASE thuoclao;
> exit
```

Edit `DATABASES` value from line 90 to line 94 and comment line 86 to 89 in the `/code/thuoclao/thuoclao/settings.py` file

Then import database

```
mysql -u<username> -p thuoclao < docker-entrypoint-initdb.d/thuoclao_init.sql
```

Influx DB: 

Add repo Influxdb

```sh
vi /etc/apt/sources.list.d/influxdb.list
deb https://repos.influxdata.com/ubuntu bionic stable
```
Add key

```
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```
Install InfluxDB

```sh
apt-get update -y
apt-get install influxdb -y
systemctl start influxdb
systemctl enable influxdb
```

Create DB user command `influx`

```sh
influx
> CREATE DATABASE thuoclao
> CREATE USER "admin" WITH PASSWORD 'admin' WITH ALL PRIVILEGES
> exit 
```

Turn on mode password

```
sed -i 's/# auth-enabled = false/auth-enabled = true/g'  /etc/influxdb/influxdb.conf
```

Restart Influxdb

```
systemctl restart influxdb
```

Then edit DATABASE_INFLUX value from line 156 to 160  in `/code/thuoclao/thuoclao/settings.py` file

Supervisor:

```
apt install -y supervisor
cp /code/supervisor/supervisord.conf /etc/supervisor/conf.d/
supervisorctl reload
supervisorctl start all
```

Nginx: 

Edit file `/code/nginx/nginx.conf`

Change `web` by `ip-server`

```
apt install -y nginx
ufw allow 'Nginx HTTP'
cp /code/nginx/nginx.conf /etc/nginx/conf.d/
sed -i 's/include \/etc\/nginx\/sites-enabled/#include \/etc\/nginx\/sites-enabled/g' /etc/nginx/nginx.conf
systemctl restart nginx
systemctl enable nginx
```

Docker
------

```
$ git clone https://github.com/locvx1234/ThuoclaoPing
$ cd ThuoclaoPing
$ ./rebuild_docker.sh
```

Then, access `http://ip-docker-host`

User : `admin`

Password : `strongpass@@`

Bejoy !


