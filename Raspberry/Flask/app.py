from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/auth")
def auth():
    return render_template('auth.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
