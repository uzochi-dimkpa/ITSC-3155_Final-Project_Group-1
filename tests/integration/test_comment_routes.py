# Any test that require an existing user possibly does not work because there is no user
# under which to make comments, so every time the comment routes are run, they don't
# actually go anywhere because they require a user to make them.
# 
# Although the 't_user' table should exist (which allows for the creation and storing of
# new users), we have no CRUD routes that actually makes new users, so whenever a comment
# is made and it looks for the user's id with which to identify itself, it finds none
# and thus fails to create a new entry in the 't_comment' table
# 
# When we are able to create users using CRUD routes,
# we can create new and functional tests
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# 
# test_app.post(f'/post/{3}/create', data={
    #     'comment_text': 'I DON'T KNOW WHAT SIDE I'M ON!!!'
    # }, follow_redirects = True)

    # res = test_app.get(f'/post/{2}', follow_redirects = True)

    # res = test_app.get('/', follow_redirects = True)

    # assert b'What is DuoLing?' in res.data
    # assert b'How do I become fluent in another language?' in res.data
    # assert b'Do I have to pay to use DuoLing?' in res.dataYou have...a moment to run


def test_create_new_comment(test_app):
    test_app.post('/register', data={
        'username': 'AAA',
        'password': 'BBB',
        'first_name': 'A',
        'last_name': 'B',
        'bio': 'My name is A B!'
    }, follow_redirects = True)

    test_app.get('/logout', follow_redirects=True)

    test_app.post('/register', data={
        'username': 'CCC',
        'password': 'DDD',
        'first_name': 'C',
        'last_name': 'D',
        'bio': 'My name is C D!'
    }, follow_redirects = True)

    test_app.get('/logout', follow_redirects=True)

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

    test_app.post('/logout', follow_redirects=True)

    test_app.post('/login', data={
        'username': 'CCC',
        'password': 'DDD'
    }, follow_redirects=True)

    test_app.post(f'post/{2}/{2}/comment', data = {
        'comment_text': 'You have...a moment to run' 
    }, follow_redirects = True)

    test_app.post(f'/post/{2}/{2}/comment', data = {
        'comment_text': 'I think- i ThInK iM In tRoUbLe-'
    }, follow_redirects=True)

    res = test_app.post(f'post/{2}/{1}/comment', data = {
        'comment_text': 'Oh no...' 
    }, follow_redirects = True)

    assert res.status_code == 200
    assert b'Oooooooooooh-' in res.data
    assert b'Tee hee hee...' in res.data
    assert b"Other People's Replies" in res.data
    assert b'Oh no...' in res.data

    res = test_app.get(f'/post/{2}', follow_redirects = True)

    assert res.status_code == 200
    assert b'You:' in res.data


def test_get_update_comment(test_app):
    res = test_app.get(f'/post/{2}/{1}/edit', follow_redirects = True)
    
    assert res.status_code == 200
    assert b'You have...a moment to run' in res.data


def test_commit_update_comment(test_app):
    test_app.post(f'/post/{2}/{1}/update', data = {
        'comment_text': 'WHY DID I-'
    }, follow_redirects=True)

    res = test_app.post(f'/post/{2}/{1}/update', data = {
        'comment_text': 'waIT, WHAT ABOUT MEEEEEEEEEEEEEEEEEEEE-'
    }, follow_redirects=True)

    assert res.status_code == 200
    assert b'WHY DID I-' not in res.data
    assert b'waIT, WHAT ABOUT MEEEEEEEEEEEEEEEEEEEE-' in res.data
    assert b'Oooooooooooh-' not in res.data and b'Tee hee hee...' not in res.data
    assert b'Oh no...' not in res.data
    assert b'Guess' in res.data and b'Who?' in res.data


def test_delete_comment(test_app):
    res = test_app.get(f'/post/{2}', follow_redirects = True)

    assert res.status_code == 200
    assert b'I think- i ThInK iM In tRoUbLe-' in res.data

    res = test_app.get(f'/post/{2}/{2}/delete', follow_redirects = True)

    assert res.status_code == 200
    assert b'I think- i ThInK iM In tRoUbLe-' not in res.data
