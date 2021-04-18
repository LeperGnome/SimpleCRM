# SimpleCRM

Really simple crm built as a test project.

## To run:
1. create postgresql db + user
2. `$ pip install -r requirements.txt`   
2. `$ cat SimpleCRM/setting/local.template.py > SimpleCRM/settings/local.py`
3. update settings with your data
4. run server `$ gunicorn SimpleCRM.wsgi:application --bind 0.0.0.0:8000`
5. checkout api reference at `http://localhost:8000/swagger`

## Tests
no tests =(