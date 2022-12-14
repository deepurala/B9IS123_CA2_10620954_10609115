from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudapplication'

mysql = MySQL(app)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Succesfully")

        productname = request.form['productname']
        productdescription = request.form['productdescription']
        productprice = request.form['productprice']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product (product_name, product_description, product_price) VALUES (%s, %s, %s)", (productname, productdescription, productprice))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', product = data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)