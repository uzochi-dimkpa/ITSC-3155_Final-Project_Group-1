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