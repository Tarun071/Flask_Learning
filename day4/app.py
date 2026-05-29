from flask import Flask , redirect,url_for,render_template

app=Flask(__name__)

# control statments
'''
1.Condition
{% if marks>50 %}
    <p>pass</p>
{% else %}
    <p>Fail</p>
{% end if %}

2.loop
{% for item in subjects %}
<p> {{item}}</p>
{% end for %}
'''
# Template Inheritance

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)