from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define variables to pass to the template
    title = 'My Page'
    message = 'Welcome !'

    # Render the template with the variables
    return render_template('frontpage.html', title=title, message=message)

if __name__ == '__main__':
    app.run()
