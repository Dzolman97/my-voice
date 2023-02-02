from flask import Blueprint, render_template, request, flash, redirect, url_for
import os

auth = Blueprint('auth', __name__)



@auth.route('/', methods=['GET', 'POST'])
def construction_is_here():

   # Get the secret phrase from the POST form and check against ENV secret phrase.
   if request.method == 'POST':
      phrase_submission = request.form.get('phrase')
      secret_phrase = os.environ['SECRET_PHRASE']
      secret_phrase = f"{secret_phrase}"
      print(secret_phrase)

      if phrase_submission != secret_phrase:
         flash("Incorrect Secret Phrase, try again.")
         return render_template("construction.html")
      
      if phrase_submission == secret_phrase:
         return redirect(url_for('views.home'))
   
   else:
      return render_template("construction.html")