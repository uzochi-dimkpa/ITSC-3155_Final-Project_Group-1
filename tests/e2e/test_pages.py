def test_index_page(test_app):
    res = test_app.get('/', follow_redirects = True)

    assert res.status_code == 200
    assert b'<h1 id="DuoLing_header">DuoLing</h1>' in res.data
    assert b'<article class="Side_window">' in res.data
    assert b'<table id="main_table">' in res.data
    assert b'<table id="nested_table">' in res.data


def test_login_page(test_app):
    res = test_app.get('/login', follow_redirects = True)

    assert res.status_code == 200
    # assert b'<form action="/login" method="post">' in res.data
    # assert b'<label for="username"><h4>Username</h4></label>' in res.data
    # assert b'<label for="password"><h4>Password</h4></label>' in res.data
    # assert b'<button type="button" id="loginbutton" class="btn btn-primary">Login</button>' in res.data
    # assert b'<h2>New User?</h2>' in res.data
    # assert b'<button type="button" class="btn btn-primary">SignUp</button>' in res.data


def test_signup_page(test_app):
    res = test_app.get('/signup', follow_redirects = True)

    assert res.status_code == 200
    # assert b'<form action="register" method="post">' in res.data
    # assert b'<label for="username"><h4>Username</h4></label>' in res.data
    # assert b'<label for="email"><h4>Email</h4></label>' in res.data
    # assert b'<label for="password"><h4>Password</h4></label>' in res.data
    # assert b'<input style="width: 26px; height: 23px;" class="form-check-input" type="checkbox" value="" id="formCheckDefault">' in res.data
    # assert b'<label style="margin-left: 30px;" class="form-check-label" for="formCheckDefault"><h5>Opt-in to recieve email notifications of new DuoLing posts for your languages</h5></label>' in res.data
    # assert b'<button type="button" id="signupbutton" class="btn btn-primary">SignUp</button>' in res.data


def test_about_page(test_app):
    res = test_app.get('/about', follow_redirects = True)

    assert res.status_code == 200
    assert b'<h2>Who We Are</h2>' in res.data
    assert b'<p class="about-body">' in res.data
    assert b'<h2>Our Goals</h2>' in res.data
    assert b'<h2>Contact Us!</h2>' in res.data
    assert b'<p>Phone: (555) 555-0000</p>' in res.data
    assert b'<p>Email: info@duolingmail.com</p>' in res.data


def test_faq_page(test_app):
    res = test_app.get('/faq', follow_redirects = True)

    assert res.status_code == 200
    assert b'<h1>Frequently Asked Questions (FAQ)</h1>' in res.data
    assert b'<td>What is DuoLing?</td>' in res.data
    assert b'<th scope="row">A</th>' in res.data
    assert b'<td>DuoLing is a forum where users can upload & answer questions, comment on posts,' in res.data
    assert b'<td>How does one become fluent in another language?</td>' in res.data
    assert b'<td>Practice, practice, practice!</td>' in res.data
    assert b'<td>Do I have to pay to use DuoLing?</td>' in res.data
    assert b"<td>It's free! We welcome users of all ages 8+ (with parental guidance for those under 16)</td>" in res.data


# Any test that require an existing user possibly does not work because there is no user
# under which to make posts, so every time the post routes are run, they don't
# actually go anywhere because they require a user to make them.
# 
# Although the 't_user' table should exist (which allows for the creation and storing of
# new users), we have no CRUD routes that actually makes new users, so whenever a post
# is made and it looks for the user's id with which to identify itself, it finds none
# and thus fails to create a new entry in the 't_post' table
# 
# This same issue likewise applies to any routes looking for comments & users (profile page)
# 
# When we are able to create users using CRUD routes,
# we can update these currently commented tests
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# def test_update_post_page(test_app):
#     res = test_app.get(f'/post/{1}/update', follow_redirects = True)
# 
#     assert res.status_code == 200
# 
# 
# def test_create_post_page(test_app):
#     res = test_app.get('/post/new', follow_redirects = True)
# 
#     assert res.status_code == 200
#     assert b'<h1 id="ask-question">Ask a Question!</h1>' in res.data
#     assert b'<form class="container=fluid form" action="/post/' in res.data
#     assert b'<label for="title">Enter your Question here</label>' in res.data
#     assert b'<label for="body">Enter details about your question!</label>' in res.data
#     assert b'<textarea class="form-control" id="body"name=\'body\' rows="4" wrap="soft" required></textarea>' in res.data
#     assert b'<button type="submit" class="btn button-post">Post</button>' in res.data