from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    if(name[-1]!='y'):
        return "<h1>Name is {} </h1>".format(name+"y")
    else:
        return "<h1>Name is {} </h1>".format(name[:-2]+"iful")

if __name__=='__main__':
    app.run(debug=True)
