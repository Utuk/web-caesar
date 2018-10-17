from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
         form{{
             background-color: #eee;
             padding: 20px;
             margin 0 auto;
             width: 540px;
             font: 16px sans-serif;
             border-radius: 10px
         }}
         textarea {{
             margin: 10px 0;
             width: 540px;
             height: 120;
         }}
        </style>
    </head>
    <body>
        <form action="/" method="post"> 
            <label>
                Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <label>
                <textarea name="text">{0}</textarea>
            </label>
            <input type="submit" />
        </form>
    </body>
</html>

"""

#@app.route("/")
#def index(): 
    #return form

#@app.route("/", methods=['POST'])
#def index_post(): 
    #text_element = request.form['text']
    #rot_element = request.form['rot']
    #return #form.format('')

@app.route("/")
def index(): 
    return form.format('')

#def index_post(): 
    #text_element = request.form['text']
    #rot_element = request.form['rot']
    #return form.format('')
@app.route("/", methods=['GET', 'POST'])
def encrypt():

    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)
    encrypt_message = rotate_string(text, rot)
    
    return form.format(encrypt_message)

app.run()

#@app.route("/", methods=['POST']) #change method to GET for get request
#def hello():
    #first_name = request.form['first_name'] #change request to this when using GET = request.args.get('first-name')
    #return '<h1> Hello, ' + first_name + '</h1>'