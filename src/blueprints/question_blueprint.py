from flask import Blueprint, abort, redirect, render_template, request
from src.models import Question, db

router = Blueprint('question_router', __name__, url_prefix='/question')
