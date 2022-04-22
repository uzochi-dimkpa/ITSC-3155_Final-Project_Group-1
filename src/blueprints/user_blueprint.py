from flask import Blueprint, abort, redirect, render_template, request
from src.models import User, Post, Relationship, db

router = Blueprint('user_router', __name__, url_prefix='/user')

@router.get('')
def user_profile():
    # TEMPORARY
    user_id = 1
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user = user) #- , user = user_id, friends = all_friends

@router.get('/<user_id>')
def user_profile_from_id(user_id):
    user = User.query.get_or_404(user_id)
    user_posts = Post.query.filter(Post.user_id == user_id).all()
    return render_template('profile.html', user = user, posts = user_posts)

# @router.get('/<user_id>') #- /{{ user.user_id }}
# def user_profile(user_id):
#     user = User.query.get_or_404(user_id)
#     user_friends = Relationship.query.filter_by(user_id_one = user_id, relate_type = 'friends').all()
#     return render_template('profile.html', user = user, user_friends = user_friends)
