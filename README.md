# drf-ecommerce-api

`drf-ecommerce-api` is a REST API for an e-commerce store built using `Django REST framework`. It can be used with any shopping project needing JSON products. 

## Goal
The goal with `drf-ecommerce-api` is to provide a client user with e-commerce JSON data and allow users to filter products based on a model’s fields, displaying the form to let them do this.


## Features

``drf-ecommerce-api`` is built with `Django` and `Django REST framework`. It follows a RESTFul API design architecture and `drf-ecommerce-api` incorporates filtering capabilities using `django-filter`. 

`django-filter` is a generic, reusable application to alleviate writing some of the more mundane bits of view code.

## Usage

## ⚙️ Installation

- Open CMD
  
- Change directory to desktop

  `cd desktop`
   
- Clone repository

  `git clone git@github.com:backendkolawole/drf-ecommerce-api.git`

- Install all the packages listed in your requirements.txt file

  `pip install -r requirements.txt`

- In the same directory as settings.py, create a file called `.env`

  - Set up `SECRET_KEY` variable



## Endpoints

**GET /products**

Call this endpoint to get all products

- Possible responses

```
200 (OK)

{
    "products": []
}


```

**GET /products/:id**

Call this endpoint to get a task with a specific id

Possible responses

```
200 (OK)

{
    "task": {
        "_id": "65c9f0aa2ffa276952e09bb9",
        "name": "first task",
        "completed": true,
        "__v": 0
    }
}


404 (Not Found)

{
    "msg": "No task with id: 65c9f0aa2ffa276952e09bb9"
}

```


## Contact
