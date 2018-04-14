from flask import Flask, render_template, flash, redirect
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/actors')
def show_actors():
    user = {'username': 'Эльдар Рязанов'}
    actors = [
        {
            'name': 'John Smith',
            'genre': 'Drama actor'
        },
        {
            'name': 'Anna Blake',
            'genre': 'Drama actor'
        },
        {
            'name': 'Susann Khils',
            'genre': 'Comedy actor'
        }
    ]
    return render_template('actors.html', title='Actors', user=user, actors=actors)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
