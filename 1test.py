from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/blah')
def alex():
    return 'You are whipped'

if __name__ == '__main__':
    #app.debug = True
    #app.secret_key = "hime"
    app.run()



