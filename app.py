from os import abort

from flask import Flask, render_template, request, jsonify

from utils import get_posts_all, get_comments_by_post_id, search_for_posts, get_posts_by_user, get_post_by_pk

app = Flask(__name__)


@app.route('/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_detail(postid):
    post = get_post_by_pk(postid)
    if not post:
        abort(404)

    comments = get_comments_by_post_id(postid)
    return render_template('post_detail.html', post=post, comments=comments, bookmark_icon='static/bookmark.png')


@app.route('/search/')
def search():
    query = request.args.get('s', '')
    if not query:
        return "Введите ключевое слово для поиска", 400

    matching_posts = search_for_posts(query)
    return render_template('search.html', query=query, posts=matching_posts)


@app.route('/users/<username>')
def user_feed(username):
    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', username=username, posts=user_posts)


@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена", 404


@app.errorhandler(500)
def internal_server_error(error):
    return "Ошибка сервера", 500
post=None

@app.route('/api/posts', methods=['GET'])
def api_get_all_posts():
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def api_get_post_by_id(post_id):
    post = get_post_by_pk(post_id)
    if not post:
        abort(404)  # Возвращаем статус-код 404, если пост не найден
    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
