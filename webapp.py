from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_main():
    return render_template('Inputs.html')

@app.route("/response1")
def render_response1():
    response1 = request.args['r1'] 
    if response1 == 'Chatty':
        reply = "That's my name, too!"
    else:
        reply = "That's a very nice name. My name is Chatty."
    return render_template('Responses.html', r1 = reply)

@app.route("/response2")
def render_response2():
    response1 = request.args['r2'] 
    if response1 == 'Yes':
        reply = "I like the rain too."
    else:
        reply = "I love the rain!"
    return render_template('Responses.html', r2 = reply)

@app.route("/response3")
def render_response3():
    response1 = request.args['r3'] 
    if response1 == 'Spring':
        reply = "Spring is my favorite season to."
    else:
        reply = "My favorite season is Spring."
    return render_template('Responses.html', r3 = reply)

@app.route("/response4")
def render_response4():
    response1 = request.args['r4'] 
    if response1 == 'Chatty':
        reply = "That's my name, too!"
    else:
        reply = "That's a very nice name. My name is Chatty."
    return render_template('Responses.html', r4 = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
