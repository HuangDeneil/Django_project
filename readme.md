### This is the Web service of Pathogen database searching & management
---
### The framework is  `Django`
#### Need to install list:

Program | version
-|-
pip            | 20.0.3
python         | 3.8
Django         | 3.0
mysqlclient    | 2.0.1
MySQL          | 15.1
PyMySQL        | 0.10.0

<br><br>

## Before started turn on web service need to Edit seeting: `setting.py`

---

### ip setting:

`setting.py`

```python
ALLOWED_HOSTS = ['XXX.XXX.XXX.XXX', 'XXX.XXX.XXX.XXX', ...]
```



#### We change the defualt database from sqlite to `MySQL`

Its means need to edited `setting.py` in the first time before start 
web service.


```python
DATABASES = {
       "default": {
       "ENGINE": "django.db.backends.mysql",
       "NAME": "django_project",
       "USER": "account",
       "PASSWORD": "password",
       "HOST": "localhost",
       "PORT": "3307",
       'OPTIONS': {
       'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
       },
   }    
}

```

<br>


### Start web service:

```python
python manage.py runserver 0.0.0.0:8000
```

#### ps. This command is write into `web_online.sh`
####  `sh web_online.sh` can start web service automatic   





<br><br>

#### Chinese output

`setting.py`<b>:

```python
LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'
```


