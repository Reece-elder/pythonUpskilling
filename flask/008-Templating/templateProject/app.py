from flask import Flask, render_template

app = Flask(__name__)

@app.route('/reece')
def ben():
    return render_template('reece.html')

@app.route('/about')
def harry():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)