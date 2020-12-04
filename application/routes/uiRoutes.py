from flask import current_app as app, render_template, url_for


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/<maskIndicator>')
def result(maskIndicator):

    if maskIndicator == '1':
        print("Mask detected, door unlocked")
        door_filename = url_for('static', filename='images/door-open.jpg')
    else:
        print("No mask detected, door locked")
        door_filename = url_for('static', filename='images/door-closed.jpg')

    return render_template('result.html', door_image=door_filename)
