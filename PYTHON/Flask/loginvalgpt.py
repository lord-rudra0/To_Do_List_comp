from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Route for success page
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

# Password validation function
def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()_+" for char in password):
        return "Password must contain at least one special character."
    return None

# Route for login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Get 'nm' from form data
        password = request.form['pwd']  # Get 'password' from form data

        # Validate password
        password_error = validate_password(password)
        if password_error:
            return render_template_string(f'''
            <p>{password_error}</p>
            <a href="/login">Try Again</a>
            ''')
        
        return redirect(url_for('success', name=user))
    return '''
        <form method="post">
            Username: <input type="text" name="nm"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
