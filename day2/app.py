from flask import Flask,url_for,redirect

app=Flask(__name__)
# url_for
# url_for() is used to generate URLs dynamically in Flask.
# avoids harcoding(entering redicect links manually)
# @app.route('/')
# def home():
#     return "Home page"

# @app.route('/about') 
# def about():
#     return url_for('home')


# dynamic routing
'''
URL-> http://127.0.0.1:5000
The dynamic routing means passing values through url,flask allows URLs  to acccept variable
'''

# name="tarun"
# @app.route('/')
# def home():
#     return redirect(url_for('student'))

# @app.route('/student/')
# def student():
#     return f"welcome"


@app.route('/profile/<username>')
def profile(username):
    return f"welcome {username}"

@app.route('/')
def home():
    return redirect(url_for('profile',username = 'Kartheek'))
if __name__ == '__main__':
    app.run(debug=True)



if __name__=='__main__':
    app.run(debug=True)