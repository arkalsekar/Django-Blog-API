# Django + PostgreSQL Blog API

A Complete Blog API created using Python / Django as the Backend Language / Framework and PostgreSQL as the Database. PostgreSQL is highly efficient and is capable of managing Databases in Production.


## Requirements / Key Features

Here are the Features of the features of API.
</br>
1. Uses PostgreSQL as the Relational Database.
2. Performs all the CRUD Operations 
3. Along with the CRUD Operation it also also provides an endpoint for Searching.

## Endpoints 

- ``` / ``` - Gets a Glimpse of all the Endpoints.
- ``` /getAll ``` - Returns all the Blogs currently available in the Database.
- ``` /get/<id> ``` - Returns Specific Blog with an id provided in the id parameter.
- ``` /drop/<id> ``` - Deletes a Specific Blog using the id.
- ``` /search?<query> ``` - Returns the Post have a Specific Query.
- ``` /insert ``` - Inserts a new Post into the Database.


## Setting Up

Clone or Download the this repository and store it on your machine. 
```bash
git clone https://github.com/arkalsekar/Django-Blog-API.git
```

## Usage
Once Downloaded or Cloned the Repository, Run the following Commands

```bash
pip install -r requirements.txt
```
Once Installed all the requirements. Run the Following Commands.
```bash
python manage.py makemigrations
```
```bash
python manage.py sqlmigrate home 0001
```
```bash
python manage.py migrate
```

This is isin't necessary but with this you would be able to login to the website.

```bash
python manage.py createsuperuser
```

This command will finally run the server on localhost://8000
```bash
python manage.py runserver
```
Now head on to [localhost:8000](http://127.0.0.1:8000/) and access the site.


## Demo 
![Demo 1](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/get.PNG)

![Demo 2](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/getAll.PNG)

![Demo 3](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/drop.PNG)

![Demo 4](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/search.PNG)

![Demo 5](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/insert.PNG)

![Demo 6](https://raw.githubusercontent.com/arkalsekar/Django-Blog-API/main/Demo/insert2.PNG)

## License
[MIT](https://choosealicense.com/licenses/mit/)
