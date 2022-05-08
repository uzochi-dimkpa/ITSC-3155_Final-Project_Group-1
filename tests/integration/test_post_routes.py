# from src.models import User, Post

# user_id = 1
# logged_in_user = User.query.get(user_id)

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


# Any test that require an existing user possibly does not work because there is no user
# under which to make posts, so every time the post routes are run, they don't
# actually go anywhere because they require a user to make them.
# 
# Although the 't_user' table should exist (which allows for the creation and storing of
# new users), we have no CRUD routes that actually makes new users, so whenever a post
# is made and it looks for the user's id with which to identify itself, it finds none
# and thus fails to create a new entry in the 't_post' table
# 
# When we are able to create users using CRUD routes,
# we can update these currently commented tests
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# def test_get_single_posts(test_app):
#     test_app.post(f'/post/{3}/create', data={
#         'title': 'Oooooooooooh-',
#         'body': 'Gotcha!'
#     }, follow_redirects = True)
# 
#     test_app.post(f'/post/{3}/create', data={
#         'title': 'Oh no...',
#         'body': 'WHY DID I-'
#     }, follow_redirects = True)
# 
#     res = test_app.get(f'/post/{2}', follow_redirects = True)
# 
#     assert res.status_code == 200
#     assert b'Reply' in res.data
#     assert b"Other People's Replies:" in res.data
# 
# 
# def test_get_update_post(test_app):
#     res = test_app.get(f'/post/{1}/update', follow_redirects = True)
# 
#     assert res.status_code == 200
# 
# 
# def test_commit_update_post(test_app):
#     res = test_app.post(f'/post/{1}', follow_redirects = True)
# 
#     assert res.status_code == 200
# 
# 
# def test_delete_post(test_app):
#     res = test_app.delete(f'post/{4}/delete', follow_redirects = True)
# 
#     assert res.status_code == 200
# 
# 
# def test_get_new_post(test_app):
#     res = test_app.get('/post/new', follow_redirects = True)
# 


# def test_get_new_post(test_app):
#     res = test_app.get('/post/new', follow_redirects = True)

#     assert res.status_code == 200
#     assert b'Ask a Question!' in res.data
#     assert b'Enter your Question here' in res.data
#     assert b'Enter details about your question!' in res.data