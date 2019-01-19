from flask import Flask, render_template, redirect, url_for
from flask import session, escape, request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/hello')
def hello_world():
    return "Hello! World!"

#  http://0.0.0.0:4444/user/kevin/123
@app.route('/user/<string:username>/<int:id>')
def show_user(username, id):
    return 'User: %s. Id: %d' % (username, id)

#  http://0.0.0.0:4444/render/kevin
#  http://0.0.0.0:4444/render
@app.route('/render/')
@app.route('/render/<usr>')
def render_test(usr = None):
    return render_template('hello.html', usr = usr)

#  跳转，注意，url_for是转到def函数名，后面是参数
@app.route('/redirect')
def redirect_test():
    return redirect(url_for('render_test', usr = 'kevinnnn'))

@app.route('/')
def index():
    if 'username' in session:
        return '''
        <h1> Logged in as %s' </h1>
        <li><input type="button" value="Logout" onclick='location.href=("/logout")'/>
        ''' % escape(session['username'])
    return '''
    <h1> Your are not Logged in </h1>
    <li><input type="button" value="Login" onclick='location.href=("/login")'/>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return '''
        <h1> You have logged in! </h1>
        <li><input type="button" value="Logout" onclick='location.href=("/logout")'/>
        '''

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('login.html')
    # return '''
    #         <form method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #         </form>
    # '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444)