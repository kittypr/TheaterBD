from flask import Flask, render_template
from config import Config

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


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run()
