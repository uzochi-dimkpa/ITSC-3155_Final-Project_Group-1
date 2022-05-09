from flask import Blueprint, abort, redirect, render_template, request
from src.models import User, Post, Relationship, db

router = Blueprint('user_router', __name__, url_prefix='/user')

@router.get('/<user_id>')
def user_profile_from_id(user_id):
    user = User.query.get_or_404(user_id)
    user_posts = Post.query.filter(Post.user_id == user_id).all()
    return render_template('profile.html', user = user, posts = user_posts)
