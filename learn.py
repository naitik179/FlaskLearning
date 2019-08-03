from flask import Flask,render_template,request

app=Flask(__name__)

app.route('/')
def index():
    return render_template('index1.html')

app.route('/signup')
def signup():
    return render_template('signup.html')


app.route('/thanks')
def thanks():
    name=request.args.get('name')
    return render_template('thanks.html',name=name)

if __name__=='__main__':
    app.run(debug=True)