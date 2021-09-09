# New Project Checklist
1. Install ```pipenv install pymysql flask```
2. Inside project folder create folders/files...
    ```
    Project Folder
        flask_app
            > config
                - mysqlconnection.py
            > controllers
                - routes.py
            > models
                (Should contain .py files as classes that are in conjunction with the tables in MySQL database. Attributes are columns)
            > static
                > css
                    - style.css
                > img
                > js
            > templates
                (html files to be rendered)
            __init__.py
        server.py
    ```
3. Copy and past mysqlconnection code - shouldn't need to change anything:
    ```
    # a cursor is the object we use to interact with the database
    import pymysql.cursors
    # this class will give us an instance of a connection to our database
    class MySQLConnection:
        def __init__(self, db):
            # change the user and password as needed
            connection = pymysql.connect(host = 'localhost',
                                        user = 'root', 
                                        password = '.SQL.W3ltr4um./,', 
                                        db = db,
                                        charset = 'utf8mb4',
                                        cursorclass = pymysql.cursors.DictCursor,
                                        autocommit = True)
            # establish the connection to the database
            self.connection = connection
        # the method to query the database
        def query_db(self, query, data=None):
            with self.connection.cursor() as cursor:
                try:
                    query = cursor.mogrify(query, data)
                    print("Running Query:", query)
                    executable = cursor.execute(query, data)
                    if query.lower().find("insert") >= 0:
                        # INSERT queries will return the ID NUMBER of the row inserted
                        self.connection.commit()
                        return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                        # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                        result = cursor.fetchall()
                        return result
                    else:
                        # UPDATE and DELETE queries will return nothing
                        self.connection.commit()
                except Exception as e:
                    # if the query fails the method will return FALSE
                    print("Something went wrong", e)
                    return False
                finally:
                    # close the connection
                    self.connection.close() 
    # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
    def connectToMySQL(db):
        return MySQLConnection(db)
    ```
4. server.py code:
    ```
    from flask_app.controllers import routes
    from flask_app import app

    if __name__=="__main__":
        app.run(debug=True)
    ```

5. __init__.py code:
    ```
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "shhhhhh"
    ```
6. Sample Model code; NOTE - class attributes should correlate with columns in table of sql database
    ```
    from flask_app.config.mysqlconnection import connectToMySQL

    class Author:
        def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
    ```
7. 
# Snippets
Create your own for boilerplate code


