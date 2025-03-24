from flask_frozen import Freezer
from app import create_app

app = create_app()

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()  # 生成静态文件到 build/ 目录