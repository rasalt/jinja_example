from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
now_time = datetime.now()

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
  return value.strftime(format)

@app.route("/")

def template_test():
  return render_template('template.html', my_string="Ruchika", my_list=[1,2,3,4,5])

@app.route("/home")
def home():
    return render_template('template.html',
                           my_string="I'm the home page",
                           my_list=[0,1,2,3,4,5],
                           curr_time=datetime.now())

@app.route("/about")
def about():
    return render_template('template.html',
                            my_string="I'm the about page",
                            my_list=[0,1,2,3,4,5],
                           curr_time=datetime.now())                            

@app.route("/contact")
def contact():
    return render_template('template.html',
                           my_string="I'm the contact page",
                           my_list=[0,1,2,3,4,5],
                           curr_time=datetime.now())
if __name__ == "__main__":
  app.run(debug = True, host="0.0.0.0", port= 8080)