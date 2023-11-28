
from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app= Flask(__name__)
mysql=MySQL()


app.config['MYSQL_DATABASE_HOST'] = 'Localhost'
app.config['MYSQL_DATABASE_HOST'] = 'root'
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'producto'

mysql.init_app(app)



if __name__== '__main__':
    app.run(debug=True)
