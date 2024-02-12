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

  `git clone git@github.com:backendkolawole/node-taskmanager-api.git`

- Install packages

  `npm install`

- Create a .env file in the root directory

  - Set up `MONGO_URI` variable equal to the DB connection string
  - Set up `PORT` variable
  - Set up `JWT_SECET` variable



## Endpoints

**GET /task**

Call this endpoint to get all tasks

- Possible responses

```
200 (OK)

{
    "tasks": []
}


401 (Unauthorized)

Unauthorized

```

**GET /tasks/:id**

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


401 Unauthorized

Unauthorized


404 (Not Found)

{
    "msg": "No task with id: 65c9f0aa2ffa276952e09bb9"
}

```


## Contact
