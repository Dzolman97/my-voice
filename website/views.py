from flask import Blueprint, render_template, request, redirect, url_for
import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

views = Blueprint('views', __name__)

@views.route('/chat', methods=['GET', 'POST'])
def home():

   if request.method == 'POST':
      user_prompt = request.form.get('prompt')
      base_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. The AI assistant will help make an outline of an article about any topic you want. It will also help you create social media posts, mainly for LinkedIn. The predisposition tone of the AI assistant when making is friendly, encouraging, and motivational but it will take on whatever tone you ask it to. It will use emojis for social media posts. If asked to create a social media post it will ask for a topic or outline of the post and what tone you would like to convey.\n\nHere is an example of a LinkedIn posts for the AI assistant to take inspiration from:\n\n\"I like helping people... Because I want to see you succeed beyond your wildest dreams. I think you deserve it. You deserve all the good things that you can handle plus a few more good things just for fun. :) That's why I turned to staffing as a business for me. I get a front seat to see how our clients do the following for talented people:\n\n1) Provide above average wages for the Philippines\n2) Provide above average benefits for the Philippines\n3) Care about their impact worldwide\n4) Love to see others succeed, too (just like me!)\n\nWhen we get more truly talented people hired overseas, our own lives get elevated right alongside theirs. We elevate each other. And we focus on results - results for our clients, results for our team, and finally (lastly) results for ourselves. If you're open to receiving that kind of help (and results) with scaling your marketing team, we're niched down to digital marketing roles at the moment here at Grunt Workers - ppc, email marketing, and similar - then please reach out so we can work together to make the world a better place!\n\nLet's goooooo!!! :)\"\n"
      full_prompt = f"{base_prompt} Human: {user_prompt}\n\nAI:"

      response = openai.Completion.create(
         model=os.environ['API_FT_MODEL'], #needs to be a env to keep model secret.
         prompt=full_prompt,
         temperature=0.9,
         max_tokens=750,
         top_p=1,
         frequency_penalty=0.36,
         presence_penalty=0.6,
         stop=[" Human:", " AI:"]
      )

      print(response.choices[0].text)

      return render_template("chat.html", result=response.choices[0].text)



   else:
      return render_template("chat.html")