import pytest
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker

fake = Faker()

@pytest.fixture
def client():
    client = APIClient()
    
    new_role = {
        'name': 'ADMIN',
    }
    role = client.post('/api/roles/', new_role, format='json')
    assert role.status_code == status.HTTP_200_OK

    new_user = {
        "password": "adminadmin",
        "name": fake.name(),
        "email": fake.email(),
        "status": True,
        "role": role.data['data']['id']
    }
    user = client.post('/api/auth/register/', new_user, format='json')
    assert user.status_code == status.HTTP_200_OK

    credentials = {
        'email': new_user['email'],
        'password': new_user['password']
    }
    login = client.post('/api/auth/login/', credentials, format='json')
    assert login.status_code == status.HTTP_200_OK

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {login.data['data']['access']}')
    return client

@pytest.mark.django_db
def test_roles_list(client):
    response = client.get('/api/roles/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['ok'] == True
    assert response.data['object'] == 'list_roles'
    assert isinstance(response.data['data'], list)

@pytest.mark.django_db
def test_barbers_list(client):
    response = client.get('/api/barbers/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['ok'] == True
    assert response.data['object'] == 'list_barbers'
    assert isinstance(response.data['data'], list)