from http import HTTPStatus


def test_read_root_deve_retornar_OK_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_username',
            'password': 'password',
            'email': 'test@test.com',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test_username',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test_username',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'password',
            'username': 'test_userUpdated',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'test_userUpdated',
        'email': 'test@test.com',
        'id': 1,
    }
