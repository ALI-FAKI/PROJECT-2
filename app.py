from flask import Flask, request, render_template
from pymongo import MongoClient

# Initialize the Flask app
app = Flask(__name__)

# Connect to MongoDB (localhost:27017)
client = MongoClient('localhost', 27017)
db = client.membership_db  # Create/Connect to the database
members_collection = db.members  # Create/Connect to the collection

# Route for rendering the membership form
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submissions
@app.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Create a dictionary for the new member
    new_member = {
        'name': name,
        'email': email,
        'password': password
    }
    
    # Insert the new member into the database
    members_collection.insert_one(new_member)
    
    return f"Member {name} has been successfully registered!"

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)