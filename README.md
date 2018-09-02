# ThuoclaoPing

```
ThuoclaoPing - A product is made by HocChuDong team
ThuocLaoPing written in Python (Work-In-Progress)
```
Some of the screen pictures :)

- web browser

  <img src='https://i.imgur.com/ox8EzY8.png'>

- mobile

  <img src='https://i.imgur.com/UZuEEkZ.png'>

## Setup
- [1 Use Docker to setup the ThuocLaoPing](#docker)
- [2 Setup manual the ThuocLaoPing ](#manual)


### <a name="docker">1. Docker</a>
------

Install docker

The OSs: CentOS 7.3 64bit, Ubuntu 14.04 64bit, Ubuntu 16.04 64bit

```
curl -sSL https://get.docker.com/ | sudo sh
sudo usermod -aG docker `whoami`
systemctl start docker.service
systemctl enable docker.service
```
Setup the ThuocLaoPing

```
$ https://github.com/hocchudong/thuoclaoping.git
$ cd ThuoclaoPing
$ ./rebuild_docker.sh
```

Then, access `http://ip-docker-host`

User : `admin`

Password : `strongpass@@`

Bejoy !

### <a name="manual">2. Manual</a>
Environment 
-----------
python3.6
```sh
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:jonathonf/python-3.6
Press [ENTER] to continue or ctrl-c to cancel adding it
```

```sh
apt-get update
apt-get install python3.6
```

Install
-------

Clone source code and install dependences:

```
apt update && apt install -y python3-pip fping redis-server mysql-server-5.7 mysql-client-core-5.7 libmysqlclient-dev
git clone https://github.com/hocchudong/thuoclaoping.git
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

Then, access `http://ip-docker-host`

User : `admin`

Password : `strongpass@@`

Bejoy !


