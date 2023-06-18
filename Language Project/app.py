from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    result = my_python_function()  # Call your Python function and retrieve the result
    return render_template('index.html', result=result)

def my_python_function():
    # Your Python function logic here
    return "Hello, World!"  # Replace with the actual result

if __name__ == '__main__':
    app.run()