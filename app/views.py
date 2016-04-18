from flask import render_template, request, session, flash, redirect, url_for, abort, jsonify, json, make_response, Response, url_for
from app import app
from .forms import LoginForm
import os

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":

        return str(request.headers)
