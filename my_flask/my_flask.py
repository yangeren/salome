from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import abort
import requests

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'Hello World!'
def index():
    user_agent = request.headers.get('User-Agent')
    header = {
        'user_agent': 'android'
    }
    return '<p>Your browser is %s</p>' % user_agent, 400, header
    # return '<h1>Bad Request</h1>', 400

@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello, %s!</h1>' % name

    return render_template('index.html',name=name)




@app.route('/user/<id>')
def load_user(id):
    pass

def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>hello, %s</h1>' % user.name


@app.route('/make_response')
def test_make_response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def test_redirect():
    return redirect('http://www.baidu.com')

@app.route('/srp')
def srp():
    url = 'http://api2.souyue.mobi/d3api2/webdata/search.result.groovy?keyword=%E4%B8%AD%E5%9B%BD%E8%BF%90%E5%8A%A8&vc=3.3'
    res = requests.get(url).json()

    data = [
        'list1',
        'list2',
        'list3',
        'list4',
        'list5'
    ]
    print res['head']['nav']
    title = 'this is srpword'
    return render_template('srp.html', text = res, title = title)




if __name__ == '__main__':
    app.run(debug=True)
