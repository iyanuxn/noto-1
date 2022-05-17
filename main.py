
# Importing the create_app function from the website.py file.
from website.__inti__ import create_app
# This is the main file that runs the app.
app = create_app()

# This is a conditional statement that checks if the file is being run directly. If it is, then it
# runs the app.
if __name__ == '__main__':
    app.run(debug=True)
    
    
