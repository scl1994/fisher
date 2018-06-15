def is_isbn_or_key(word):
    """
    :param word: 搜索关键词或isbn
    :return: 返回具体输入是key或isbn
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and short_word == 10 and short_word.isdigit:
        isbn_or_key = "isbn"
    return isbn_or_key
