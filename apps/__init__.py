from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("apps.secure")
    app.config.from_object("apps.setting")
    register_blueprints(app)
    return app


def register_blueprints(app):
    """
    :param app: Flask app核心对象
    :return:
    将蓝图注册到Flask核心对象上
    """
    from apps.web import web
    app.register_blueprint(web)
