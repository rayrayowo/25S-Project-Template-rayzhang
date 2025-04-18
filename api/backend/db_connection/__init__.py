#------------------------------------------------------------
# This file creates a shared DB connection resource
#------------------------------------------------------------
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor

# 创建共享的数据库连接对象
db = MySQL(cursorclass=DictCursor)
# the parameter instructs the connection to return data 
# as a dictionary object. 
db = MySQL(cursorclass=cursors.DictCursor)