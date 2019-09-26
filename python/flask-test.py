from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Taiheon Choi',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Choi',
        'title': 'Blog post 2',
        'content': 'Second content',
        'date_posted': 'April 21, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)