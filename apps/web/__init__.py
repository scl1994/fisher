from flask import Blueprint

web = Blueprint("web", __name__)

# 装饰器在导入的时候运行，从而进行路由注册
from .book import search

