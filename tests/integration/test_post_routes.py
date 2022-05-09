def test_get_all_posts(test_app):
    res = test_app.get('/', follow_redirects = True)

    assert res.status_code == 200
    assert b'DuoLing' in res.data
    assert b'Frequent Questions' in res.data
    assert b'All Questions' in res.data
    assert b'Vote' in res.data and b'View' in res.data

    assert b'What is DuoLing?' in res.data
    assert b'How do I become fluent in another language?' in res.data
    assert b'Do I have to pay to use DuoLing?' in res.data


def test_get_single_post(test_app):
    test_app.post('/register', data={
        'username': 'AAA',
        'password': 'BBB',
        'first_name': 'A',
        'last_name': 'B',
        'bio': 'My name is A B!'
    }, follow_redirects = True)

    test_app.post('/logout', follow_redirects=True)

    test_app.post('/register', data={
        'username': 'CCC',
        'password': 'DDD',
        'first_name': 'C',
        'last_name': 'D',
        'bio': 'My name is C D!'
    }, follow_redirects = True)

    test_app.post('/logout', follow_redirects=True)

    test_app.post('/login', data={
        'username': 'AAA',
        'password': 'BBB'
    }, follow_redirects=True)

    test_app.post(f'/post/create/{1}', data={
        'title': 'Oooooooooooh-',
        'body': 'Tee hee hee...'
    }, follow_redirects = True)

    test_app.post(f'/post/create/{1}', data={
        'title': 'Guess',
        'body': 'Who?',
    }, follow_redirects=True)

    res = test_app.get(f'/post/{2}', follow_redirects = True)

    assert res.status_code == 200
    assert b'Posted by' in res.data
    assert b"Other People's Replies:" in res.data


def test_get_update_post(test_app):
    res = test_app.get(f'/post/{1}/update', follow_redirects = True)

    assert res.status_code == 200
    assert b'Say something!' in res.data
    assert b'Edit your post here' in res.data and b'Edit details about your post!' in res.data
    assert b'details' in res.data
    assert b'Oooooooooooh-' in res.data
    assert b'Tee hee hee...' in res.data


def test_commit_update_post(test_app):
    res = test_app.post(f'/post/{2}', data = {
        'title': '???',
        'body': '!!!'
    }, follow_redirects = True)


    assert res.status_code == 200
    assert b'???' in res.data and b'!!!' in res.data
    assert b'Posted by' in res.data
    assert b"Other People's Replies:" in res.data


def test_delete_post(test_app):
    test_app.post(f'/post/create/{1}', data={
        'title': 'Gotcha!',
        'body': '>:]',
    }, follow_redirects=True)

    res = test_app.post(f'post/{2}/delete', follow_redirects = True)

    assert res.status_code == 200
    assert b'DuoLing' in res.data


def test_start_new_post(test_app):
    res = test_app.get('/post/new', follow_redirects = True)

    assert res.status_code == 200
    assert b'Ask a Question!' in res.data
    assert b'Enter your Question here' in res.data
    assert b'Enter details about your question!' in res.data