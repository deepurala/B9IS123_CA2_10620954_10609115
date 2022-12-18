https://github.com/deepurala/B9IS123_CA2_10620954_10609115

# B9IS123_CA2_10620954_10609115

Group Details: Group K

Business Use case: Store admin portal

Scenario: Web portal to perform basic CRUD operations for Store admins to manage store items

Web Application User Interface

Backend Code- Python

Integrate - API (Python Flask API)

Database: MySQL

## Project Grop Details:
------------------------------
* **Group :** K
*  **Participants :** 

1. PRADEEP NAGENDRA URALA (10609115)
2. DEVIKA BOLLUR THIRUMALESHWARA (10620954)


-------------------
# Store Admin Portal

This web portal could be used to allow store admins to manage store items. The portal would allow admins to Create, Read, Update, and Delete (CRUD) store items. 

The portal would have a main page that shows a list of all the store items. This page would also have the option to edit or delete the item. 

The portal would also have an “Add Product Data” option, which would allow admins to add new items to the store. This  would require admins to enter information about the item, such as its name, description, and price . 

Overall, this web portal would provide store admins with a convenient way to manage store items. It would allow them to easily view, add, update, and delete items.

## Technology and Libraries used
* **Backend Technologies :**
1. Python
2. Flask
3. flask_mysqldb

* **Database Technologies :**
1. MYSQL

* **Frontend Technologies :**
1. HTML5
2. CSS3
3. BOOTSTRAP
4. Javascript
5. Jquery

* **Local Server :**
1. WAMPSERVER



## Installing flask framework
```bash
pip install flask
```

```bash
pip install flask_mysqldb
```

## Individual contribution

### Devika Bolluru Thirumaleshwara (10620954)
Created the HTML files which will be used to render the frontend. Used Bootstrap and CSS to create a modern and stylish UI. Created a JavaScript file to handle the frontend logic and to validate.
Created the database and tables for the application. 
For the backend setup  installed the necessary packages for  Flask application.
Connecting the application to the database.
I worked on the READ and DELETE operations in the app.py file as part of the CRUD operation.


### Pradeep Nagendra Urala (10609115)
I collaborated with my team mate to code a few REST API methods in python file and also understand and makes according changes in the landing page. As the landing page was already structued by my team mate, I had to work on the minor deatils of the app.py file and test these REST API functions in local WAMP server. 
Once, we had the application ready, I moved on to the deployment part of the application where I creaded a new Azure web app in the student account of Azure portal. I did refere to a few [microsoft documentation](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli) on how to deploy the GitHub repos onto Azure. Here I have used a native feature of GitHub called GitHub Actions to authenticate this repository to Azure web app portal. After a few tries I was able to deploy the GitHub project onto the Azure web app.

## References
1. Flask:
	https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
	https://webdamn.com/create-restful-api-using-python-mysql/

2. Frontend:
	https://www.codewithrandom.com/2022/08/12/ecommerce-website-using-html-css-and-javascript-simple-and-responsive-ecommerce-website/
	https://getbootstrap.com/docs/5.2/forms/overview/

3. Database:
	https://youtu.be/HXV3zeQKqGY
	https://youtu.be/6L3HNyXEais

4. Deployment:
	https://youtu.be/lQgsRuZXhcY
