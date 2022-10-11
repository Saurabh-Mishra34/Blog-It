from flask import Flask,render_template,request,session
from flask_mysqldb import MySQL
import json
from flask_mail import Mail

with open('config.json','r') as c:
    params = json.load(c)["params"]


app = Flask(__name__)
app.secret_key = 'my-secret-key'
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = 'saurabhmishra.19.ce@iite.indusuni.ac.in',
#     MAIL_PASSWORD = ''
# )
# mail = Mail(app)

# app.config['MYSQL_HOST'] = params["host"]
# app.config['MYSQL_USER'] = params["user"]
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = params["db"]

# mysql=MySQL(app)

@app.route('/')
def l():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM home")
    # poe = cur.fetchall()
    return render_template('login.html')

@app.route('/home')
def h():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM home")
    # poe = cur.fetchall()
    # poe={'title':"",'subtitle':"by Saurabh",'data':"This is my first ever post. Delighted to post it"}
    return render_template('index.html')

@app.route('/dashboard',methods=['GET','POST'])
def dash():
    return render_template('login.html')
    # if('user' in session and session['user']==params['admin_user']):
    #     cur = mysql.connection.cursor()
    #     cur.execute("SELECT * FROM posts")
    #     data = cur.fetchall()
    #     return render_template('dashboard.html',params=params,data=data)
    #
    # if request.method=='POST':
    #     username=request.form.get('admin_name')
    #     password=request.form.get('admin_pass')
    #     if(username==params['admin'] and password==params['password']):
    #         cur = mysql.connection.cursor()
    #         cur.execute("SELECT * FROM posts")
    #         data = cur.fetchall()
    #         return render_template('dashboard.html', params=params,data=data)
    # else:
    #     return render_template('login.html',params=params)

@app.route('/about')
def au():
    return render_template('about.html')

@app.route('/add_pos',methods=['GET','POST'])
def apos():
    # if "user" in session and session['user'] == params['admin_user']:
    #     if request.method == 'POST':
    #         title = request.form['title']
    #         slug = request.form['slug']
    #         content = request.form['mess']
    #         cursor = mysql.connection.cursor()
    #         cursor.execute(f"INSERT INTO posts(`title`, `slug`, `content`) VALUES ({title},{slug},{content})")
    #         mysql.connection.commit()
    #         cursor.close()
    #         return render_template('add_pos.html',params=params,cursor=cursor)
    # else:
        return render_template('add_pos.html',params=params)

@app.route('/contact', methods = ['GET', 'POST'])
def c():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     u_email = request.form['email']
    #     u_phone = request.form['phone']
    #     msg = request.form['message']
    #     cursor = mysql.connection.cursor()
    #     cursor.execute(  "INSERT INTO contact VALUES(%s,%s,%s,%s)", (name, u_email,u_phone,msg))
    #     mysql.connection.commit()
    #     cursor.close()
    #     mail.send_message(f"You have a message from user {name}",sender=u_email,
    #                       recipients=['saurabhmishra.19.ce@iite.indusuni.ac.in'],
    #                       body= f"{msg} with\n phone no \t {u_phone} ")
    #     mail.send_message(f"Thank You {name}",sender='saurabhmishra.19.ce@iite.indusuni.ac.in',
    #                       recipients=[u_email],
    #                       body=f"We have registered your message for further enquires please wait for the reply ")
    return render_template('contact.html')


# ,methods=['GET']
@app.route('/post')
def po():
    return render_template('post.html')
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM posts")
    # data = cur.fetchall()

    # data = data

app.run(debug=True)