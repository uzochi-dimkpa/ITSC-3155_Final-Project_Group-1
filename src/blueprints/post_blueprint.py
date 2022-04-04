from flask import Blueprint, abort, redirect, render_template, request
from src.models import Post, db

router = Blueprint('post_router', __name__, url_prefix='/post')
