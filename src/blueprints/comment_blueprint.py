from flask import Blueprint, abort, redirect, render_template, request
from src.models import Comment, db

router = Blueprint('comment_router', __name__, url_prefix='/comment')
