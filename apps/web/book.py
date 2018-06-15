from flask import jsonify

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通搜索关键字或者isbn号
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == "isbn":
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)