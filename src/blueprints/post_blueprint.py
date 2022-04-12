from flask import Blueprint, abort, redirect, render_template, request
from src.models import Post, Tag, db

router = Blueprint('post_router', __name__, url_prefix='/post')

@router.post('')
def create_post():
    body = request.form.get('body', '')
    user_id = request.form.get('user_id', '')
    created_at = request.form.get('created_at', '')
    updated_at = request.form.get('updated_at', '')

    if body == '' or user_id == '' :
        abort(400)

    create_post = Post(body=body, user_id=user_id, created_at=created_at, updated_at=updated_at)
    db.session.add(create_post)
    db.session.commit()

    return redirect(f'/books/{create_post.post_id}')

@router.get('/<post>')
def get_user_post(post_id):
    user_post = Post.query.get_or_404(post_id)
    all_english = Tag.query.filter_by(post_id_one = post_id, tag_name = 'english').all()
    return render_template('profile.html', post = post_id, english = all_english)