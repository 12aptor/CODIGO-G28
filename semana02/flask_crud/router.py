from flask import Blueprint
from resources.user_resource import UserResource

user_router = Blueprint('user_router', __name__, url_prefix='/api/user')


@user_router.get('/list') # /api/user/list
def listUsers():
    user_resource = UserResource()
    return user_resource.list()

@user_router.post('/create') # /api/user/create
def createUser():
    user_resource = UserResource()
    return user_resource.create()

@user_router.put('/update') # /api/user/update
def updateUser():
    user_resource = UserResource()
    return user_resource.update()

@user_router.delete('/delete') # /api/user/delete
def deleteUser():
    user_resource = UserResource()
    return user_resource.delete()