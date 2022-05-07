from src.models import User
from app import bcrypt

def test_user_model():
    u = User(username='A_B', user_password=bcrypt.generate_password_hash('C_D').decode('utf-8'), first_name='A', last_name='B', bio='Lorem', num_friends=0)

    assert u.username == 'A_B'
    # Check password
    assert bcrypt.check_password_hash(u.user_password, 'C_D') is True
    assert u.first_name == 'A' and u.last_name == 'B'
    assert u.bio == 'Lorem' and u.num_friends == 0


def test_user_model_2():
    u = User(username='I_J', user_password=bcrypt.generate_password_hash('K_L').decode('utf-8'), first_name='I', last_name='J', bio='Ipsum', num_friends=44)

    assert u.username != ''
    # Check password
    assert bcrypt.check_password_hash(u.user_password, 'L_K') is not True
    assert u.first_name != 'J' and u.last_name != 'I'
    assert len(u.bio) >= 0 and u.bio != ''
    assert u.num_friends >= 0 and u.num_friends < 9999


def test_user_model_3():
    u = User(username='Food', user_password=bcrypt.generate_password_hash('Water').decode('utf-8'), first_name='Soda', last_name='Can', bio='!!!', num_friends=2)

    assert type(u.username) == str
    assert type(u.user_password) != int and len(u.user_password) > 0
    assert type(u.first_name) != bytes and type(u.last_name) != dict
    assert type(u.bio) != bool and type(u.num_friends) != float