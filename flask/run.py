import os
import json
from flask import Flask, render_template    # The capital F indicates that that's a class name. Firstly we import our Flask class.

app = Flask(__name__)       # We then creat an instance of this and stor is our variable is called app. (Convention).
                            
@app.route('/')             # The root decorator binds the index() function to itself so that whenever that root is called, the function is called.
def index():                # This function is also called a view
    return render_template("index.html")

@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}

    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)


@app.route('/about')
def about():
    data = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)        # The additional argument here 'page_title' is a variable name chosen.
                                                                    # You can add as many additional arguments as you like
@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

"""
The first argument of our Flask class is the name of the application module, our package. 
Since were just using a single module we can use __name__ which is a built in python variable. 
Flask needs this so it knows where to look for templates and static files.
Then we use the app.route decorator to tell Flask what URL should trigger the function called index. In Python a decorator starts with an @ 
sign (pie notation). A decorator is a way of wrapping functions. All functions are onjectd and can be passed around.
Just as in JavaScript all functions are objects and can be passed around. So when we try to browse to the root directory, indicated by the 
"/", then Flask triggers the index function.
"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

"""
The were going to reference this built in variable and say that if __name__ = __main__ then were going to run our app with the following 
arguments: The host is going to be set to os.environ.get("IP"). This is an internal environment variable that Cloud9 has set, and we're 
using the os module from the standard library to get that environment variable for us.
It's the same with PORT, but this time we're casting it as an int, because it needs to be an integer. 
We're also then putting debug=true because that will allow us to debug our code easier. 
__main__ is the name of the default module in Python. It's the first one that we run, so if this has not been imported - which it won't be 
it's going to be run directly - then we want to run our app using these arguments that we're passing in here. 

"""