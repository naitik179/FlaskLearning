from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)


app.config['SECRET_KEY'] = 'naitik'

class Infoform(FlaskForm):
    breed=StringField("What Breed are you?\n")
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    breed=False

    form =Infoform()

    if form.validate_on_submit():
        breed=form.breed.data
        form.breed.data=''
    return render_template('index3.html',form=form,breed=breed)

if __name__ == '__main__':
  app.run(debug=True)
 