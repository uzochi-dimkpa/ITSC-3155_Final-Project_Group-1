from flask import Blueprint, abort, redirect, render_template, request
from src.models import Comment, Post, User, db
from src.blueprints.post_blueprint import router as post_router
from sqlalchemy import update, delete

# router = Blueprint('comment_router', __name__, url_prefix='/comment')
router = post_router

# <div class="form-group">
#     <label for="question">Question</label>
#     <textarea class="form-control" id="question" form="question" rows="3" name="question" wrap="soft" required></textarea>
#   </div>

# @router.get('/new')

# @router.post('/<post_id>') #- , methods = ['GET', 'POST']
# def create_comment(post_id):
#     # TODO: PLACEHODER; the following code will be replaced with code for user login
#     # session querying and for returning the user object to the '_layout.html' page
#     user_id = 1
#     logged_in_user = User.query.get(user_id)
    
#     # post_id = request.form.get('post_id', '')
#     post_id = post_id
#     # user_id = request.form.get('user_id', '')
#     comment_text = request.form.get('comment_text', '')
#     created_at = db.func.now()
#     updated_at = None

#     if user_id == '' or comment_text == '':
#         abort(400)

#     created_comment = Comment(post_id=post_id, user_id=logged_in_user.user_id, comment_text=comment_text, created_at=created_at, updated_at=updated_at)
#     db.session.add(create_comment)
#     db.session.commit()

#     return redirect(f'/post/{post_id}', new_comment = created_comment)



# def query_post_by_comment(comment):
#     return Post.query.filter(comment.post_id==Post.post_id)

# def query_user_by_comment(comment):
#     return User.query.filter(comment.user_id==User.user_id)



# # @router.get('/<post_id>/<comment_id>/edit')
# # def get_edit_comment_form(post_id, comment_id):
# #     return None

# @router.post("/<post_id>")
# def update_comment(post_id, comment_id):
#     # updated_comment = update(Comment).where(Comment.comment_id==comment_id).values(comment_text=body)
#     comment_text = request.form.get('comment_text', '')
#     user_id = User.query.get(Post.query.filter(post_id).user_id)
#     post_id = post_id
#     created_at = Comment.query.get(comment_id).created_at
#     updated_at = db.func.now()

#     updated_comment = Comment(comment_text=comment_text, user_id = user_id, post_id = -1, created_at = created_at, updated_at = updated_at)
#     db.session.commit()

#     return redirect(f'/post/{updated_comment.post_id}')

# @router.post('/<post_id>/<comment_id>/delete')
# def delete_comment(post_id, comment_id):
#     # deleted_comment = delete(Comment).where(Comment.comment_id==comment_id)
#     deleted_comment = Comment.query.get_or_404(comment_id)
#     db.session.delete(deleted_comment)
#     db.session.commit()

#     return redirect (f'/post/{post_id}')