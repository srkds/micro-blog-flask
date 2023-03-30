from app import app

@app.route('/')
@app.route('/index')
def home():
    return "Welcome to microblog 🚀"