from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    list=[1,2,3,4,5,6,7]
    return render_template('index.html',list=list)

if __name__=='__main__':
    app.run(debug=True)
