from flask import Flask, request

print(__name__)
app = Flask(__name__)

@app.route("/email", methods=['POST'])
def receber_email():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True)