import pytest
from app.main import create_app, db
from app.models.User import User
from flask import session

@pytest.fixture(scope='session')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(name='testuser').first():
            user = User(name='testuser', password='testpass')
            db.session.add(user)
            db.session.commit()

    with app.test_client() as client:
        yield client

def login_test_user(client):
    return client.post('/login', data={
        'name': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)

def logout_test_user(client):
    return client.get('/logout', follow_redirects=True)

def test_index_logged_in(test_client):
    login_response = login_test_user(test_client)
    assert login_response.status_code == 200
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Logout' in response.data

def test_logout_user(test_client):
    logout_response = logout_test_user(test_client)
    assert logout_response.status_code == 200
    assert b'Login' in logout_response.data
