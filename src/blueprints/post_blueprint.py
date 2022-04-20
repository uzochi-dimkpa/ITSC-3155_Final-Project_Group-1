from flask import Blueprint, abort, redirect, render_template, request
from src.models import Post, Comment, Tag, db

router = Blueprint('post_router', __name__, url_prefix='/post')

@router.get('/new')
def create_post_form():
    return render_template('create-post.html')

@router.post('')
def create_post():
    title = request.form.get('title', '')
    body = request.form.get('body', '')
    user_id = request.form.get('user_id', '')
    created_at = request.form.get('created_at', '')
    updated_at = request.form.get('updated_at', '')

    if title == '' or body == '' or user_id == '':
        abort(400)

    new_post = Post(title=title, body=body, user_id=user_id, created_at=created_at, updated_at=updated_at)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/{new_post.post_id}')

@router.get('/<post_id>')
def get_user_post(post_id):
    user_post = Post.query.get_or_404(post_id)
    post_comments = Comment.query.filter(Comment.post_id == post_id).all()

    # Debug
    # print(post_comments)

    # all_english_posts = Tag.query.filter_by(post_id_one = post_id, tag_name = 'english').all()
    return render_template('post-example.html', post = user_post, comments = post_comments) #- , english_posts = all_english_posts
