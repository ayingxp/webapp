from flask import Flask, escape

app = Flask(__name__)


@app.route("/index")
def hello_world():
    return "Hello world!"

@app.route("/")
def index():
    return "Hello to index!"


"""
通过把 URL 的一部分标记为 <variable_name>
    就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。
    通过使用 <converter:variable_name> ，
    可以 选择性的加上一个转换器，为变量指定规则。

    转换器类型：
        string: （缺省值）接受任何不包含斜杠的文本
        int: 接受正整数
        float: 接受正浮点数
        path: 类似string, 但可以包含斜杠
        uuid: 接受uuid字符串
"""


@app.route("/user/<string:username>")
def show_user_profile(username):
    """
    show the user profile for that user

    :param username: 参数名称必须与装饰器内参数的名称一致
    :return:
    """

    # Convert the characters &, <, >, ‘, and ” in string s to HTML-safe sequences.
    # Use this if you need to display text that might contain such characters in HTML.
    # Marks return value as markup string.

    return "User %s" % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)



"""
唯一的 URL / 重定向行为
"""

"""
访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
"""
@app.route('/projects/')
def projects():
    return 'The project page'


"""
about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。
如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。
这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。
"""
@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug=True)
