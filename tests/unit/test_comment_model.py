from src.models import Comment
import sqlalchemy.sql.functions
from sqlalchemy.sql import func

def test_comment_model():
    current_date_time = func.now()
    c = Comment(comment_text='Tomatoes & potatoes!', user_id=11, post_id=22, created_at=current_date_time, updated_at=current_date_time)

    assert c.comment_text == 'Tomatoes & potatoes!'
    assert c.user_id == 11 and c.post_id == 22
    assert c.created_at == current_date_time and str(c.updated_at) == str(current_date_time)


def test_comment_model_2():
    current_date_time = func.now()
    c = Comment(comment_text='I put my flower pots in the dishwasher!', user_id=491, post_id=3128, created_at=current_date_time, updated_at=current_date_time)

    assert c.comment_text != 'Lemon' and type(c.comment_text) == str
    assert c.user_id != 410 and c.post_id > 0
    assert len(str(c.created_at)) >= len(str(current_date_time)) and c.updated_at != func.now()


def test_comment_model_3():
    current_date_time = func.now()
    c = Comment(comment_text='This sentence is false?', user_id=1, post_id=77, created_at=current_date_time, updated_at=current_date_time)

    assert len(c.comment_text) > 0
    assert c.user_id > 0 and c.post_id > 2
    assert type(c.created_at) == sqlalchemy.sql.functions.now and c.updated_at != '2020-10-30 3:21:5'