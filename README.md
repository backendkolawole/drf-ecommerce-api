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
   
- Clone this repository

  `git clone git@github.com:backendkolawole/drf-ecommerce-api.git`

- Change current directory

  `cd drf-ecommerce-api`

- Create a virtual environment

  `python -m venv myvirtualenv`
  
- Activate virutal environment

  `myvirtualenv\Scripts\activate`

- Install all the packages listed in your requirements.txt file

  `pip install -r requirements.txt`

- In the same directory as settings.py, create a file called `.env`

  - Set up `SECRET_KEY` variable

> [!WARNING]
> `SECRET_KEY` is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.



## Endpoints

For the endpoints that follow, the base path is shown as `/api/v1`


**GET /products**

Call this endpoint to get all products

- Possible responses

```
200 (OK)

[
    {
        "id": 1,
        "company": "liddy",
        "name": "First Product",
        "price": 4,
        "rating": 4,
        "featured": false,
        "created": "2023-12-19"
    }
]


```
