from src.models import Post
import sqlalchemy.sql.functions
from sqlalchemy.sql import func

def test_post_model():
    current_date_time = func.now()
    p = Post(title='Twenty', body='Two', user_id=1, created_at=current_date_time, updated_at=current_date_time)

    assert p.title == 'Twenty' and p.body == 'Two'
    assert p.user_id == 1
    assert p.created_at == current_date_time and str(p.updated_at) == str(current_date_time)


def test_post_model_2():
    current_date_time = func.now()
    p = Post(title='Icicles & Glacier', body='Aurora Borealis', user_id=82, created_at=current_date_time, updated_at=current_date_time)

    assert p.title != 'Twenty' and p.body != 'Two'
    assert p.user_id != 410
    assert len(str(p.created_at)) >= len(str(current_date_time)) and p.updated_at != func.now()


def test_post_model_3():
    current_date_time = func.now()
    p = Post(title='Eggs', body='Bacon', user_id=5, created_at=current_date_time, updated_at=current_date_time)

    assert len(p.title) > 0 and type(p.body) != int
    assert p.user_id > 0
    assert type(p.created_at) == sqlalchemy.sql.functions.now and p.updated_at != '2020-10-30 3:21:55'