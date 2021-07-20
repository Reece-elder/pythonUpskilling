# Import the request method to use requests other than GET
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

# Saying /post can be sent with GET or POST
@app.route('/post', methods=['GET', 'POST'])
def post():
    # the variable 'string' is equal to the request method
    string = request.method
    # if request.method == 'POST':
    #     string = "Post"
    # else:
    #     string = "Get"
    return f'This is a {string} request'

# dynamic urls - /<query name> allows you to send strings as paramaters
# Pass in the name of the query into the function and it can be returned
@app.route('/user/<name>')
def user(name):
    return f'This is username {name}'

# If searching by something other strings do <data_type:paramater name> when searching
@app.route('/product/<int:id>')
def product(id):
    return f'This is product number {id}'

@app.route('/squared/<int:num>')
def squared(num):
    return f'{num} squared is {num * num}'

if __name__ == "__main__":
    app.run(debug=True)