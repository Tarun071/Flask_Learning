from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
atm_data = {
    "account_number": "123",
    "pin": "123",
    "balance": 10000
}
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    acc_no = request.form['account_number']
    pin = request.form['pin']
    if acc_no == atm_data["account_number"] and pin == atm_data["pin"]:
        return redirect(url_for('dashboard'))
    return "Invalid Credentials"

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    
    if request.method == 'POST':
        amount = int(request.form['withdraw'])
        atm_data['balance']-=amount
    #     return f"""
    #     <h1>{atm_data["balance"]-amount}</h1>
    # """
        return redirect(url_for('dashboard'))
    return render_template("withdraw.html")

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    
    if request.method == 'POST':
        amount = int(request.form['withdraw'])
        atm_data['balance']+=amount
        return redirect(url_for('dashboard'))
    return render_template("withdraw.html")
@app.route('/check_balance')
def check_balance():
    # if request.method=='POST':
        return f"""<h2> balance :
         <p> {atm_data["balance"]} </p> """
if __name__ == '__main__':
    app.run(debug=True)