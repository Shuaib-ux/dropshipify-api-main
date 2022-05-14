# Welcome to world of dropshipify. its an api nothing cool

## For endpoints go [here](endpoints.MD)

## For tasks and api to do go [here](Todo.md)
## Environment set ups

Create Virtual environment in python
### Mac
```
$ python3 -m venv venv
```
### Windows
```
$ py -3 -m venv venv
```
## To install all require libraries run
```
$ pip3 install -r requirements.txt 
```
## To Add newly installed libraries
```
$ pip freeze >requirements.txt
$ python3 -m pip freeze > requirements.txt
```

## Activate virtual environment:
### Windows
```
$ venv\Scripts\activate

```
### Mac 
```
source venv/bin/activate
``` 
## Sometimes flask is confused and doesn't know what it wants, so tell it
```
$ export FLASK_APP=app.py
```

## Commands to handle database migrations
```
$ flask db init    

$ flask db migrate -m 'add status'
$ flask db upgrade
```


