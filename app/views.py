from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Nick' }
    posts = [ #fake array of posts
        {
            'author': { 'nickname': 'Jimmy' },
            'body': 'I\'m studying for step1!'
        },
        {
            'author': { 'nickname': 'Jo' },
            'body': 'Did anyone else watch True Detective?'
        }
    ]
    return render_template("index.html",
                           title = 'HOME',
                           user = user,
                           posts = posts)
