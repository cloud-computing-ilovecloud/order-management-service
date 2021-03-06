from flask import Flask, render_template
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/')
def hello_world():
    return render_template("helloWorld.html")

@app.route('/service_info')
def service_info():
    return "service info text!"

if __name__ == "__main__":
    app.run(debug=True)