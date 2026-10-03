from flask import Flask

# Initialize the Flask application instance
app = Flask(__name__)

# Define a route for the home/root URL
@app.route("/")
def hello_world():
    # This message will be displayed in the browser
    return "<h1>Hello, World!</h1><p>Welcome to your first Flask app.</p>"

# Run the app locally if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
