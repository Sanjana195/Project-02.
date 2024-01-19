from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/admin', methods=['GET'])
def admin():
    # Simulating the logged-in state as Admin
    # In a real application, you would implement authentication and authorization logic
    is_admin = True

    if is_admin:
        return render_template('admin.html')
    else:
        return "Unauthorized access to the Admin page."

if __name__ == '__main__':
    app.run(debug=True)
