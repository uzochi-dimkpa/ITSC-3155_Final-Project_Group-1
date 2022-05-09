from flask import Blueprint, abort, redirect, render_template, request
from src.models import Comment, Post, User, db
from src.blueprints.post_blueprint import router as post_router
from sqlalchemy import update, delete