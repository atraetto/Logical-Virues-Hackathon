from flask import current_app as app, render_template
@app.route('/')
def hello():
    # return "Hello World!"
    return render_template('index.html')
