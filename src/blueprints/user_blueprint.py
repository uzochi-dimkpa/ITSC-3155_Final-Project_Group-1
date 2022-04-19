from flask import Blueprint, abort, redirect, render_template, request
from src.models import User, Relationship, db

router = Blueprint('user_router', __name__, url_prefix='/user')

@router.get('')
def user_profile():
    return render_template('profile.html') #- , user = user_id, friends = all_friends

# @router.get('/<user_id>') #- /{{ user.user_id }}
# def user_profile(user_id):
#     user = User.query.get_or_404(user_id)
#     user_friends = Relationship.query.filter_by(user_id_one = user_id, relate_type = 'friends').all()
#     return render_template('profile.html', user = user, user_friends = user_friends)