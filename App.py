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

@app.route('/delete/<string:id_data>', methods = ['POST', 'GET', 'DELETE'])
def delete(id_data):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product WHERE id = %s", (id_data))
    flash("Deleted Successfully")
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods = ['POST', 'GET', 'PUT'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        productname = request.form['productname']
        productdescription = request.form['productdescription']
        productprice = request.form['productprice']

        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE product
        SET product_name =%s, product_description=%s, product_price=%s
        WHERE id = %s 
        """, (productname, productdescription, productprice, id_data) )

        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)