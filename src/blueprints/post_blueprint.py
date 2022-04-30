from flask import Blueprint, abort, redirect, render_template, request
from src.models import User, Post, Comment, Tag, db
from sqlalchemy import update, delete
from sqlalchemy.sql import func

router = Blueprint('post_router', __name__, url_prefix='/post')

# @router.get('/new')
# def create_post_form():
#     return render_template('create-post.html')

# @router.post('')
# def create_post():
#     title = request.form.get('title', '')
#     body = request.form.get('body', '')
#     user_id = request.form.get('user_id', '')
#     created_at = func.now() #- request.form.get('created_at', '')
#     updated_at = None #- request.form.get('updated_at', '')

#     if title == '' or body == '' or user_id == '':
#         print(f'title: "{title}"\nbody: "{body}"\nuser_id: {user_id}')
#         return redirect(f'/post/new')

#     new_post = Post(title=title, body=body, user_id=user_id, created_at=created_at, updated_at=updated_at)
#     db.session.add(new_post)
#     db.session.commit()

#     return redirect(f'/post/{new_post.post_id}')

# @router.get('/<post_id>') #- , methods = ['GET']
# def get_user_post(post_id):
#     user_post = Post.query.get_or_404(post_id)
#     post_comments = Comment.query.filter(Comment.post_id == post_id).all()

#     # Debug
#     # print(post_comments)

#     # all_english_posts = Tag.query.filter_by(post_id_one = post_id, tag_name = 'english').all()
#     return render_template('post-example.html', post = user_post, comments = post_comments) #- , new_comment = None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@router.get('/new')
def create_post_form():
    return render_template('create-post.html')

@router.post('/create')
def create_post():
    title = request.form.get('title','')
    body = request.form.get('body','')
    #user_id = request.form.get('user_id', '')
    #tag = request.form.get('tags', '')
    created_at = func.now() #- request.form.get('created_at', '')
    #- request.form.get('updated_at', '')

    if title == '' or body == '': #or user_id == '':
        abort(400)

    new_post = Post(title=title, body=body, user_id=1, created_at=created_at, updated_at=None)
    
    # Debug
    print(new_post.body)
    
    db.session.add(new_post)
    db.session.commit()

    post_comments = Comment.query.filter(Comment.post_id == new_post.post_id).all()
    return render_template('post-example.html', post=new_post, comments=post_comments)

    #return redirect(f'/{new_post.post_id}')

@router.get('/<post_id>')
def get_user_post(post_id):
    user_post = Post.query.get_or_404(post_id)
    post_comments = Comment.query.filter(Comment.post_id == post_id).all()

    # Debug
    # print(post_comments)

    # all_english_posts = Tag.query.filter_by(post_id_one = post_id, tag_name = 'english').all()
    return render_template('post-example.html', post = user_post, comments = post_comments) #- , english_posts = all_english_posts

@router.get('/<post_id>/update')
def get_update_post_form(post_id):
    post_title = Post.query.get(post_id).title
    post_body = Post.query.get(post_id).body
    post_comments = Comment.query.filter(Comment.post_id == post_id).all()
    return render_template('update-post.html', post_id = post_id, title = post_title, body = post_body, comments = post_comments)

@router.post('/<post_id>')
def update_user_post(post_id):
    title = request.form.get('title', '')
    body = request.form.get('body', '')
    # new_body = Post.update().where(Post.post_id== post_id).values(body = body,title = title)

    if title == '' or body == '':
        print(f'\n\n\ntitle: {title}\nbody: "{body}"\n\n\n')
        return redirect(f'/post/{post_id}/update')
        # abort(400)

    post_to_update = Post.query.get(post_id) #- .first()
    post_to_update.title = title; post_to_update.body = body
    db.session.commit()
    post_comments = Comment.query.filter(Comment.post_id == post_to_update.post_id).all()
    return render_template('post-example.html', post = post_to_update, comments = post_comments) #- f'/post/{post_id}'

@router.post('/<post_id>/delete')
def delete_post(post_id):
    # <!-- <a href="/post/{{ post.post_id }}/delete">Delete</a> -->
    # deleted_post = delete(Post).where(Post.post_id==post_id)
    post_to_delete = Post.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(f'/')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# {% if body is defined and body is not none %}placeholder="{{ body }}"{% endif %}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





@router.route('/<post_id>/comment', methods = ['GET', 'POST']) #- 
def create_comment(post_id):
    # TODO: PLACEHODER; the following code will be replaced with code for user login
    # session querying and for returning the user object to the '_layout.html' page
    user_id = 1
    logged_in_user = User.query.get(user_id)

    user_post = Post.query.get_or_404(post_id)
    post_comments = Comment.query.filter(Comment.post_id == post_id).all()
    
    # post_id = request.form.get('post_id', '')
    post_id = post_id
    # user_id = request.form.get('user_id', '')
    comment_text = request.form.get('comment_text', '')
    created_at = func.now()
    updated_at = None

    if user_id == '' or comment_text == '':
        print(f'\n\n\nuser_id: {user_id}\ncomment_text: "{comment_text}"\n\n\n')
        return redirect(f'/post/{post_id}')

    created_comment = Comment(post_id=post_id, user_id=logged_in_user.user_id, comment_text=comment_text, created_at=created_at, updated_at=updated_at) #- 1
    db.session.add(created_comment)
    db.session.commit()

    return render_template('post-example.html', post = user_post, comments = post_comments, new_comment = created_comment) #- f'/post/{post_id}'


def query_post_by_comment(comment):
    return Post.query.filter(comment.post_id==Post.post_id)

def query_user_by_comment(comment):
    return User.query.filter(comment.user_id==User.user_id)


@router.get("/<post_id>/<comment_id>/edit")
def get_update_comment_form(post_id, comment_id):
    text = Comment.query.get(comment_id).comment_text
    return render_template('update-comment.html', post_id = post_id, comment_text = text, comment_id = comment_id)

@router.post("/<post_id>/<comment_id>/update") #- /<comment_id>/update #- /{{ comment_id }}/update
def update_comment(post_id, comment_id): #- , comment_id
    # updated_comment = update(Comment).where(Comment.comment_id==comment_id).values(comment_text=body)
    # updated_comment = Comment(comment_text=comment_text, user_id = user_id, post_id = post_id, created_at = created_at, updated_at = updated_at)
    # {% if new_comment.user_id == logged_in_user.user_id %}{% endif %}

    updated_comment_text = request.form.get('comment_text', '')
    user_id = User.query.get(Post.query.get(post_id).user_id)
    title = Post.query.get(post_id).title; body = Post.query.get(post_id).body
    # post_id = post_id
    # created_at = Comment.query.get(comment_id).created_at
    # updated_at = func.now()

    if updated_comment_text == '':
        print(f'\n\n\nuser_id: {user_id}\npost_id: {post_id}\ncomment_text: "{updated_comment_text}"\n\n\n')
        return redirect(f'/post/{post_id}/{comment_id}/edit')

    comment_to_update = Comment.query.get(comment_id)
    comment_to_update.comment_text = updated_comment_text
    db.session.commit()

    user_post = Post.query.get_or_404(post_id)
    all_post_comments = Comment.query.filter(Comment.post_id == post_id).all()

    return render_template('post-example.html', post = user_post, comments = all_post_comments, title = title, body = body) #- f'/post/{updated_comment.post_id}'

@router.get('/<post_id>/<comment_id>/delete')
def delete_comment(post_id, comment_id):
    # deleted_comment = delete(Comment).where(Comment.comment_id==comment_id)
    # <!-- <form id="new_user_comment" action="/post/{{ post.post_id }}/{{ new_comment.comment_id }}/delete" method="POST">
    #     <button form="new_user_comment" type="submit" class="btn btn-danger">Delete</button>
    # </form> -->
    # <!-- <form id="all_comments" action="/post/{{ post.post_id }}/{{ comment.comment_id }}/delete" method="POST">
    #         <button form="all_comments" type="submit" class="btn btn-danger">Delete</button>
    #     </form> -->

    
    comment_to_delete = Comment.query.get_or_404(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()

    return redirect (f'/post/{post_id}')