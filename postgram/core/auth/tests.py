import pytest
from rest_framework import status
from core.fixtures.user import user
class TestAuthenticationViewSet:
    endpoint = '/api/auth/'
def test_login(self, client, user):
    data = {
            "email": user.email,
            "password": "test_password"
    }
    response = client.post(self.endpoint + "login/", data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['access']
    assert response.data['user']['id'] == user.public_id.hex
    assert response.data['user']['username'] == user.username
    assert response.data['user']['email'] == user.email
@pytest.mark.django_db
def test_register(self, client):
    data = {
"username": "johndoe",
"email": "johndoe@yopmail.com",
"password": "test_password",
"first_name": "John",
"last_name": "Doe"
    }
    response = client.post(self.endpoint + "register/", data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['user']['email'] == data['email']
    assert response.data['token']
def test_refresh(self, client, user):
    data = {
"email": user.email,
"password": "test_password"
    }
    response = client.post(self.endpoint + "login/", data)
    assert response.status_code == status.HTTP_200_OK
    data_refresh = {
"refresh": response.data['refresh']
}
    esponse = client.post(self.endpoint + "refresh/", data_refresh)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['access']
def test_list_anonymous(self, client, post):
    response = client.get(self.endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
def test_retrieve_anonymous(self, client, post):
    response = client.get(self.endpoint +
    str(post.public_id) + "/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == post.public_id.hex
    assert response.data['body'] == post.body
    assert response.data['author']['id'] == post.author.public_id.hex
    def test_create_anonymous(self, client, post):
        data = {
        "body": "Test Post Body",
"author": "test_user"
    }
        response = client.post(self.endpoint, data)
        assert response.status_code ==status.HTTP_401_UNAUTHORIZED
    def test_update_anonymous(self, client, post):
        data = {
"body": "Test Post Body",
"author": "test_user"
}
        response = client.put(self.endpoint +
        str(post.public_id) + "/", data)
        assert response.status_code ==      status.HTTP_401_UNAUTHORIZED
    def test_delete_anonymous(self, client, post):
        response = client.delete(self.endpoint +
        str(post.public_id) + "/")
        assert response.status_code ==status.HTTP_401_UNAUTHORIZED