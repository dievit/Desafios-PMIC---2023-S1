from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/artefatos_scrum')
def artefatos():
    return render_template('artefatos.html')

@app.route('/time_scrum')
def time_scrum():
    return render_template('timescrum.html')

@app.route('/scrum')
def scrum():
    return render_template('scrum.html')

@app.route('/probacklog')
def probacklog():
    return render_template('probacklog.html')

@app.route('/sprintbacklog')
def spbacklog():
    return render_template('sprintbacklog.html')

@app.route('/burndown')
def burndown():
    return render_template('burndown.html')

if __name__=='__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True)
