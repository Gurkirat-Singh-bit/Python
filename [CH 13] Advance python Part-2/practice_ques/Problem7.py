# Problem 7) Explore the ‘Flask’ module and create a web server using Flask & Python. 

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def home():
    return "Hello, World!"

# Define a route for another page ("/about")
@app.route('/about')
def about():
    return "This is a simple Flask web server!"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

