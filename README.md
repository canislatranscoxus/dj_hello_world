# dj_hello_world

This is a Hello world app in Django python web development framework.
  
The current project and app is Just for play and test 
cloud environments, and web servers engines. 

This project does not include extra libraries or resources.
---

to run django app

`python3 manage.py runserver`

### Unit Test


on browser check these

127.0.0.1:8000/
127.0.0.1:8000/hello
127.0.0.1:8000/get_date_time

### Test on GCP Cloud Shell

first run django app, next click the message
127.0.0.1:8000/

it must go to some thing like this

https://8000-cs-185113205129-default.us-central1.cloudshell.dev/?authuser=0&environment_name=default/

also verify the pages:
* hello
* get_date_time


https://8000-cs-185113205129-default.us-central1.cloudshell.dev/hello/?authuser=0&environment_name=default/
https://8000-cs-185113205129-default.us-central1.cloudshell.dev/get_date_time/?authuser=0&environment_name=default/

---
## test on GCP App Engine

* create a gcp project
* enable App Engine API
* enable billing
* on cloud shell set project

`gcloud config set project <my_project_ID>`

* create App in App Engine dashboard GUI, 
  or in cloud shell

`gcloud app create`

deploy from console

`gcloud app deploy`

next, a link must appear. Something like this

https://prjdj01.uc.r.appspot.com/

---
## references

* Running Django on the App Engine standard environment
https://cloud.google.com/python/django/appengine

---
😃 😃 😃 😃 😃 😃 😃