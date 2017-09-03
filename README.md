# Local Weather

#### This repo is for a local weather app, which is an updated version of a project from freeCodeCamp's Front End Development Certification.


### Quick Start
Clone the repo:
```
git clone https://github.com/ianagpawa/weather2.0.git
```
### Install Dependencies
1. Install `google app engine (python)` and `gcloud` on your system.
2.  In the app folder location, create folder `lib`.
3.  Install the following third-party libraries with the following command:
```
pip install -t lib/ <library_name>
```
##### Libraries:
   `httplib2`
   `Requests`

4.  In the same location as the `app.yaml` file, create file `app_engine_config.py`
```
# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
```

5.  In the project folder, create file `client_secrets.json`, and add your Weather Underground API key, testing IP address, and testing geolocation coordinates values as follows:
```
{"UNDERGROUND": "XXXXXXXXXX", "TEST_IP": "XX.XXX.XXX.XXX", "TEST_GEO": "XX.XXXXXX, XX.XXXXXX"}
```


### Viewing the app locally

Run the following command while the terminal is in the project directory:
```
dev_appserver.py .
```
Then point your browser to `0.0.0.0:8080` to view the app.

### What's included
Within the project folder, you will find the following files:

```
weather2.0/
    ├── lib/ (NOT INCLUDED)
    ├── static/
    |       └── css/
    |            └── main.css
    ├── templates/
    |    └── main_page.html
    ├── .gitignore
    ├── app.yaml
    ├── appengine_config.py
    ├── Handler.py
    ├── main.py
    └── README.md
```

## Creator

**Ian Agpawa**


[Github](https://github.com/ianagpawa)

 agpawaji@gmail.com

#### Credits
Favicon provided by freefavicon.com

https://www.freefavicon.com/freefavicons/objects/iconinfo/code-break-152-246266.html
