from flask import Flask, abort, request, jsonify
app = Flask(__name__)

user = []

@app.route("/")
def hello():
    return 'hello world!'

@app.route("/user/",methods=['GET'])
def get_all_user():
    return jsonify(user)

@app.route("/user/<user_name>",methods=['GET'])
def get_one_user(user_name):
    answer = "what's your name? %s"%user_name
    return jsonify(answer)

if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    #app.run(debug=True)
    app.run()
