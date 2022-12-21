from flask import Flask, render_template, request, url_for, flash, redirect
from pyrsistent import get_in
from recipe_scraper import get_basic_info, get_ingredients, get_instructions
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    title = ''
    total_time = 0.0
    ingredients = []
    instructions = []
    if request.method == 'POST':
        URL = request.form['URL']
        if not URL:
            flash('Recipe URL is required!')
        else:
            basic_info = get_basic_info(URL)
            title = basic_info[0]
            total_time = basic_info[1]
            ingredients = get_ingredients(URL)
            instructions = get_instructions(URL)
    return render_template('index.html', title=title, total_time=total_time, ingredients=ingredients, instructions=instructions)
