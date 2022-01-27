# blue-code-be-test
Blue Code Back End Test

### Api Paths

- (GET) localhost:5000/ => running swagger
- (GET) localhost:5000/sh/ => list the most frequent paths limited to 100
- (POST) localhost:5000/sh/ => create new shorter path
- (GET)  localhost:5000/sh/<shorter> => redirect to original path

### Database 

To build the database first you have to run the following command to initialize it:

```sh
flask db init
```

Then you need to create the migrations

```sh
flask db migrate -m shorter
```

After running the above commands, now you have to apply the migration to the database.

```sh
flask db upgrade
```

### Install Requirements

#### Project dependencies

```sh
pip install -r requirements.txt
```

### Run the Project 

```
python wsgi.py run 
```


### Run the Tests

```
python wsgi.py test
```