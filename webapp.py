from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('q1t.html')

@app.route("/response")
def render_response():
    r1 = request.args['r1'] 
    if r1 == 'Chatty':
        reply = "Wow, that's my name too!"
    else:
        reply = "That's a very nice name. My name is Chatty."
    return render_template('response.html', response = reply)
    
    

    return render_template('q2t.html')


@app.route("/response")
def render_response():
    r2 = request.args['r2'] 
    if r2 == 'Yes':
        reply = "I like rain too."
    else:
        reply = "I love rain!"
    return render_template('response.html', response = reply)


    return render_template('q3t.html')

@app.route("/response")
def render_response():
    r3 = request.args['r3'] 
    if r3 == 'Spring':
        reply = "Spring is also my favorite season"
    else:
        reply = "My favorite season is Spring."
    return render_template('response.html', response = reply)


@app.route("/response")
def render_response():
    r4 = request.args['r4'] 
    if r4 == 'Flight':
        reply = "I would choose that one too. I would love the freedom."
    else:
        reply = "Cool! I would choose flight because I would to be free to explore the world."
    return render_template('response.html', response = reply)


if __name__=="__main__":
    app.run(debug=False, port=54321)
