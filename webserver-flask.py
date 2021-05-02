from flask import Flask, render_template, url_for, copy_current_request_context

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    Flask.run(app)