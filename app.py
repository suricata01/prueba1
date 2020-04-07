from flask import Flask,render_template          
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template("index.html")
if __name__ == "__main__":        # on running python app.py
    app.run()