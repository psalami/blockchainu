from flask import Flask
from flask import request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    token = request.args.get('token', None)
    if not token:
        return redirect(url_for('token'))

    return render_template('content.html')

@app.route('/token')
def token():
    return render_template('token.html')


if __name__ == '__main__':
    app.run()
