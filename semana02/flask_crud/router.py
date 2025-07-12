from flask import Blueprint, request
from resources.user_resource import UserResource

user_router = Blueprint('user_router', __name__, url_prefix='/api/user')


@user_router.get('/list') # /api/user/list
def listUsers():
    user_resource = UserResource()
    return user_resource.list()

@user_router.post('/create') # /api/user/create
def createUser():
    json = request.get_json()
    user_resource = UserResource()
    return user_resource.create(json)

@user_router.put('/<int:id>/update') # /api/user/<int:id>/update
def updateUser(id):
    json = request.get_json()
    user_resource = UserResource()
    return user_resource.update(id, json)

@user_router.delete('/<int:id>/delete') # /api/user/<int:id>/delete
def deleteUser(id):
    user_resource = UserResource()
    return user_resource.delete(id)