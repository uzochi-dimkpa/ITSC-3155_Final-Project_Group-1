# assert b'Opt-in to recieve email notifications of new DuoLing posts for your languages' in res.data

def test_signing_up_user(test_app):
    res = test_app.post('/register', data={
        'username': 'AAA',
        'password': 'BBB',
        'first_name': 'A',
        'last_name': 'B'
    }, follow_redirects = True)

    assert res.status_code == 200
    assert b'DuoLing' in res.data
    assert b'Frequent Questions' in res.data
    assert b'All Questions' in res.data
    assert b'Vote' in res.data and b'View' in res.data


def test_signing_up_user_2(test_app):
    res = test_app.post('/register', data={
        'username': 'CCC',
        'password': 'DDD',
        'first_name': 'C',
        'last_name': 'D'
    }, follow_redirects = True)

    assert res.status_code == 200
    assert b'Username' not in res.data
    assert b'Password' not in res.data
    assert b'SignUp' not in res.data
    assert b'First Name' not in res.data and b'Last Name' not in res.data


def test_logging_in_user(test_app):
    res = test_app.post('/login', data={
        'username': 'AAA',
        'password': 'BBB'
    }, follow_redirects=True)

    assert res.status_code == 200
    assert b'DuoLing' in res.data
    assert b'Frequent Questions' in res.data
    assert b'All Questions' in res.data
    assert b'Vote' in res.data and b'View' in res.data


def test_logging_in_user_2(test_app):
    test_app.get('/logout', follow_redirects=True)

    res = test_app.post('/login', data={
        'username': 'CCC',
        'password': 'DDD'
    }, follow_redirects=True)

    assert res.status_code == 200
    assert b'Username' not in res.data
    assert b'Password' not in res.data
    assert b'New User?' not in res.data
    assert b'Log In' not in res.data and b'Sign Up!' not in res.data


def test_logging_in_user_3(test_app):
    test_app.get('/logout', follow_redirects=False)

    res = test_app.post('/login', data={
        'username': 'EEE',
        'password': 'FFF'
    }, follow_redirects=True)

    assert res.status_code == 200
    assert res.status_code != 500
    # assert b'DuoLing' not in res.data
    # assert b'Frequent Questions' not in res.data
    # assert b'All Questions' not in res.data
    # assert b'Vote' not in res.data and b'View' not in res.data