from flask import Flask,redirect,url_for,request
import uuid
app=Flask(__name__)
# @app.route('/marks/<int:score>')
# def marks(score): 
#     return f"marks={score}"

# @app.route('/')
# def home():
#     return redirect(url_for('marks',score=67))



# @app.route('/marks/<float:score>')
# def marks(score): 
#     return f"marks={score}"

# @app.route('/')
# def home():
#     return redirect(url_for('marks',score=67))


# @app.route('/user/<uuid:user_id>')
# def user(user_id): 
#     return f"marks={user_id}"

# @app.route('/')
# def home():
#     uid=uuid.uuid4()
#     return redirect(url_for('user',user_id=uid))

# @app.route('/',methods=['GET'])
# def home():
#     k=int(input())
#     if k==1:
#         return redirect(url_for('student'))
    

# @app.route('/student')
# def student():
#     arr=['PFS','JFS','DA']
#     return arr


@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form.get('name')
    return f"Welcome{name}"

# @app.route('/')
# def home():
#     return redirect(url_for('submit',name = 'Raju'))

if __name__ == '__main__':
    app.run(debug=True)

