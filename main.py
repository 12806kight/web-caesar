from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
        <label for="rot">Rotate By:</label>
  		<input type="text" name="rot" id="rot" value="0">

        <label for="text"</label>
        <textarea id="text" name="text" rows="3" cols="40">{0}</textarea>

        <input type="submit" value="Submit">
           
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():

    rotate = request.form['rot']
    text = request.form['text']

    rot = int(rotate)

    return form.format(rotate_string(text, rot))
    
app.run()