from flask import Flask,render_template

app = Flask(__name__)

posts =[{
          'topic':'hello1',
          'author' :'Sandip Mishra',
          'title' :'New Post',
          },
            {
              'topic':'hello2',
              'author' : 'Sandip Mishra',
              'title':'New Post2',
             }]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html',posts=posts,title='Home')
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
