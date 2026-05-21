from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Name Card</title>

  <style>
    body{
      margin:0;
      height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      b;
      font-family:Arial, sans-serif;
    }

    .card{
      width:300px;
      height:180px;
      background:blue;
      border-radius:15px;
      box-shadow:0 4px 10px rgba(0,0,0,0.2);

      display:flex;
      justify-content:center;
      align-items:center;
    }

    .name{
      font-size:32px;
      font-weight:bold;
      color:#333;
    }
  </style>
</head>
<body>

  <div class="card">
    <div class="name">Tarun</div>
  </div>

</body>
</html>"""

if __name__=='__main__':
    app.run(debug=True)