from flask import Flask, render_template, send_file

###
# - DONT FORGET TO RUN THESE
###
# virtualenv env
# source env/bin/activate
# pip install flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route('/pdf')
def display_pdf():
    return render_template('pdf.html')


@app.route('/batters')
def batters():
    return render_template('batters.html')

@app.route('/pitchers')
def pitchers():
    return render_template('pitchers.html')

if __name__ == '__main__':
    app.run(debug=True)