from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Add print statements to debug
        print(f"Name: {name}, Email: {email}, Password: {password}")
        return render_template('success.html')
    else:
        # Handle other HTTP methods if necessary
        return "Method not allowed", 405

if __name__ == '__main__':
    app.run(debug=True)
