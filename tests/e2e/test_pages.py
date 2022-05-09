def test_index_page(test_app):
    res = test_app.get('/', follow_redirects = True)

    assert res.status_code == 200
    assert b'<h1 id="DuoLing_header">DuoLing</h1>' in res.data
    assert b'<article class="Side_window">' in res.data
    assert b'<table id="main_table">' in res.data
    assert b'<table id="nested_table">' in res.data


def test_login_page(test_app):
    res = test_app.get('/loginpage', follow_redirects = True)

    assert res.status_code == 200
    assert b'<form action="/login" method="post">' in res.data
    assert b'<label for="username"><h4>Username</h4></label>' in res.data
    assert b'<label for="password"><h4>Password</h4></label>' in res.data
    assert b'<input type="password" id="password" name="password">' in res.data
    assert b'<button type="submit" id="loginbutton" class="btn btn-primary">Log In</button>' in res.data
    assert b'<h2>New User?</h2>' in res.data
    assert b'<button type="button" id="signupbutton" class="btn btn-primary">Sign Up!</button>' in res.data


def test_signup_page(test_app):
    res = test_app.get('/signup', follow_redirects = True)

    assert res.status_code == 200
    assert b'<h1>SignUp</h1>' in res.data
    assert b'form action="/register" method="post">' in res.data
    assert b'<label for="username"><h4>Username</h4></label>' in res.data
    assert b'<label for="password"><h4>Password</h4></label>' in res.data
    assert b'<label for="first_name"><h4>First Name</h4></label>' in res.data
    assert b'<label for="last_name"><h4>Last Name</h4></label>' in res.data
    assert b'<label for="bio"><h4>Bio</h4></label>' in res.data
    assert b'<button type="submit" id="signupbutton" class="btn btn-primary">Sign Up</button>' in res.data
    assert b'<input style="width: 26px; height: 23px;" class="form-check-input" type="checkbox" value="" id="formCheckDefault">' in res.data
    assert b'<h5>Opt-in to recieve email notifications of new DuoLing posts for your languages</h5>' in res.data


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