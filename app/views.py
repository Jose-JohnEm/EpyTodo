from app import app

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
        return "Hello World\n"

@app.route('/user/<username>', methods=['POST'])
def route_add_user(username):
    return 'User added!\n'