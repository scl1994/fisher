from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object("config")


@app.route('/')
def hello_world():
    # response = make_response("<html></html>", 200)
    # response.headers = {"content-type": "text/plain"}
    # return response
    return "<html></html>", 200, {"content-type": "text/plain"}


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], host="0.0.0.0")
