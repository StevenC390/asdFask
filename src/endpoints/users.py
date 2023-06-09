from flask import Blueprint, request
from http import HTTPStatus
users = Blueprint("users",
                     __name__,
                     url_prefix="/api/v1/users")
# Data for example purposes
user_data = [
    {"id": 1, "name": "Papitas", "price": 1000, "expiration": "2020-01-12"},
    {"id": 2, "name": "Gomitas", "price": 2000, "expiration": "2020-02-22"},
    {"id": 3, "name": "Frunas", "price": 3000, "expiration": "2022-03-11"},
    {"id": 4, "name": "Juguito", "price": 4000, "expiration": "2022-03-18"},
    {"id": 5, "name": "Galletas", "price": 5000, "expiration": "2025-04-15"},
]


def read_all():
    return {"data": user_data}, HTTPStatus.OK



@users.get("/<int:id>")
def read_one(id):
    for user in user_data:
        if user['id'] == id:
            return {"data": user}, HTTPStatus.OK
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@users.post("/")
def create():
    post_data = request.get_json()
    user = {
    "id": len(user_data) + 1,
    "name": post_data.get('name', 'No Name'),
    "price": post_data.get('price', 0),
    "expiration": post_data.get('expiration', None)
    }
    user_data.append(user)
    return {"data": user}, HTTPStatus.CREATED


@users.put('/<int:id>')
@users.patch('/<int:id>')
def update(id):
    post_data = request.get_json()
    for i in range(len(user_data)):
        if user_data[i]['id'] == id:
            user_data[i] = {
            "id": id,
            "name": post_data.get('name'),
            "price": post_data.get('price'),
            "expiration": post_data.get('expiration')
            }
        return {"data": user_data[i]}, HTTPStatus.OK
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@users.delete("/<int:id>")
def delete(id):
    for i in range(len(user_data)):
        if user_data[i]['id'] == id:
            del user_data[i]
            return {"data": ""}, HTTPStatus.NO_CONTENT
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@users.get("/<int:id>/providers")
def read_one_providers(id):
    return "Reading a provider ... soon"
