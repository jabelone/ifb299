import pymysql


class mysqldb:
    def __init__(self, table_name, column_name):
        self.table_name = table_name
        self.column_name = column_name

        conn, curs = self.connectDB()
        # execute SQL
        sql = "select "+column_name+" from "+table_name
        self.executeDB(conn, curs, sql)

    def executeDB(self, conn, curs, sql):
        curs.execute(sql)
        # Fetch data
        self.rows = curs.fetchall()
        # print(self.rows)
        # close Connection
        conn.close()

    def connectDB(self):
        # MySQL Connection
        conn = pymysql.connect(host='ifb299.jaimyn.com.au', user='IFB299', password='YOLO_DANKMEMES_2017.*',
                               db='IFB299', charset='utf8')
        # generate cursor from Connection
        curs = conn.cursor()
        return conn, curs

    def getvariable(self):
        return self.rows

if __name__ == "__main__":
    db = mysqldb("student_library", "name")
    #for row in db.getvariable():
        #print(row)



