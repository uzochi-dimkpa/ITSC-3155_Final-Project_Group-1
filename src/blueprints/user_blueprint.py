from flask import Blueprint, abort, redirect, render_template, request
from src.models import User, db

router = Blueprint('user_router', __name__, url_prefix='/user')