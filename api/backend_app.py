from flask import Flask
from api.backend.db_connection import db

app = Flask(__name__)

# 从 .env 或硬编码配置中读取数据库连接参数
app.config["MYSQL_HOST"] = "mysql_db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "pawpal"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# 绑定 app 到数据库对象
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
