from caesar import rotate_string
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/add" method="post">
        <label>
         Rotate by:   
            <input type="text" name="rot" value="0"/>
            <input type="textarea" name="text" style ="width:540px; height:120px;"/>
            
        </label>
        <input type="submit"/>
    </form>
    </body>
</html>
"""


@app.route("/")

def index():
    return form 
app.run()

@app.route("/")

def encrypt(text, rot):
    enc_message = rotate_string(text, rot)
    return enc_message
app.run()
    

