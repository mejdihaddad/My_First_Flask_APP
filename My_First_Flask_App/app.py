from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def user():
    userName=request.args.get('userName')
    userNameUpper=userName.upper()
    return (userNameUpper)


if __name__ == '__main__':
    app.run(debug=True)