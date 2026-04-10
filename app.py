# Flask App
# Author: John Crumlish

from flask import Flask

# Create app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "WSAA Project Running"

# Run app
if __name__ == '__main__':
    app.run(debug=True)