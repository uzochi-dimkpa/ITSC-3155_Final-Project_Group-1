from flask import Blueprint, abort, redirect, render_template, request
from src.models import Profile, db

router = Blueprint('profile_router', __name__, url_prefix='/profile')