# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def welcome():
#     return "Hello World"


# @app.route("/check")
# def Check():
#     return "Check is it working i think now working"   


from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Now it is workings  "