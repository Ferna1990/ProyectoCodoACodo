
from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app= Flask(__name__)
mysql=MySQL()


app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_HOST'] = 'root'
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'productos'

mysql.init_app(app)

@app.route('/')
def index():
    conn=mysql.connect()
    cursor=conn.cursor()
    sql = "insert into producto(nombre) values (Pizza);"
    cursor.execute(sql)
    conn.commit()

    return render_template('')

if __name__== '__main__':
    app.run(debug=True)
