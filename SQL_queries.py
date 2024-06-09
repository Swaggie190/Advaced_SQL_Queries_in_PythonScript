import pymysql.connections

try:

    # - Replace the below content with the appropriate database informations
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="Sw@ggie190",
        database="covid19"
    )

    cursor = db.cursor()
    # - Line function
    
    def Line():
        print("-----------------------------------------------------------------------------------------------------------------------")
    	
    # - Function to print SQL query result

    def PrintSqlResults(result):
        for row in result:
            print(row)

    # - Function to execute and print SQL queries

    def QueryExecute(Query,Text):
        cursor.execute(Query)
        result1 = cursor.fetchall()
        Line()
        print(Text)
        Line()
        PrintSqlResults(result1)

    # - Query to list the departments and the name of their regions

    Query = "SELECT codeDept,nomDept,nomReg FROM departement d, region r WHERE d.codeReg = r.codeReg"
    Text = "List of departments and their regions"
    QueryExecute(Query, Text)

    # - All departments located in Brittany

    Query = "SELECT codeDept,nomDept,nomReg FROM departement d, region r WHERE d.codeReg = r.codeReg AND r.nomReg = 'Bretagne' "
    Text = "List of departments located in Brittany"
    QueryExecute(Query, Text)

    # - Departments belonging to the same region as paris

    Query = "SELECT codeDept,nomDept,codeReg FROM departement WHERE d.codeReg = (SELECT codeDept,nomDept,nomReg FROM departement d, region r WHERE d.codeReg = r.codeReg AND r.nomReg = 'Bretagne')"
    Text = "List of departments located in Brittany"
    QueryExecute(Query, Text)

except pymysql.Error as err:
    print("Error:", err)

finally:
    if cursor:
        cursor.close()
    if db:
        db.close()
