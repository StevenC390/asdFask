from flask import Blueprint, request
from http import HTTPStatus
houses = Blueprint("houses",
                     __name__,
                     url_prefix="/api/v1/houses")
# Data for example purposes
house_data = [
    {"id": 1, "name": "Papitas", "price": 1000, "expiration": "2020-01-12"},
    {"id": 2, "name": "Gomitas", "price": 2000, "expiration": "2020-02-22"},
    {"id": 3, "name": "Frunas", "price": 3000, "expiration": "2022-03-11"},
    {"id": 4, "name": "Juguito", "price": 4000, "expiration": "2022-03-18"},
    {"id": 5, "name": "Galletas", "price": 5000, "expiration": "2025-04-15"},
]


def read_all():
    return {"data": house_data}, HTTPStatus.OK



@houses.get("/<int:id>")
def read_one(id):
    for house in house_data:
        if house['id'] == id:
            return {"data": house}, HTTPStatus.OK
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@houses.post("/")
def create():
    post_data = request.get_json()
    house = {
    "id": len(house_data) + 1,
    "name": post_data.get('name', 'No Name'),
    "price": post_data.get('price', 0),
    "expiration": post_data.get('expiration', None)
    }
    house_data.append(house)
    return {"data": house}, HTTPStatus.CREATED


@houses.put('/<int:id>')
@houses.patch('/<int:id>')
def update(id):
    post_data = request.get_json()
    for i in range(len(house_data)):
        if house_data[i]['id'] == id:
            house_data[i] = {
            "id": id,
            "name": post_data.get('name'),
            "price": post_data.get('price'),
            "expiration": post_data.get('expiration')
            }
        return {"data": house_data[i]}, HTTPStatus.OK
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@houses.delete("/<int:id>")
def delete(id):
    for i in range(len(house_data)):
        if house_data[i]['id'] == id:
            del house_data[i]
            return {"data": ""}, HTTPStatus.NO_CONTENT
    return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND


@houses.get("/<int:id>/providers")
def read_one_providers(id):
    return "Reading a provider ... soon"
