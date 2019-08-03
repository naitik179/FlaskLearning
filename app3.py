from flask import Flask,render_template,session,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,SubmitField,TextField,TextAreaField,DateTimeField,SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)


app.config['SECRET_KEY']='naitik'

class InfoForm(FlaskForm):
    breed=StringField('What field are you ?',validators=[DataRequired()])
    neutered=BooleanField('Puppy Neutered ?')
    mood=RadioField('Please Choose your mood ',choices=[('mood_one','Happy'),('mood_two','Excited')])
    foodchoice=SelectField('Pick your favourite food : ',choices=[('ri','Rice'),('chi','Chinese'),('pun','Punjabi Naan')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form=InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['foodchoice']=form.foodchoice.data
        session['feedback']=form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index4.html',form=form)

@app.route('/thankyou')
def thankyou():
   return render_template('thankyou.html')

if __name__ == '__main__':
  app.run(debug=True)
 