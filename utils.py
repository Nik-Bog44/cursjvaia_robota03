import json
import os


def get_posts_all():
    """ Возвращает посты"""
    file_path = os.path.join('data', 'posts.json')
    with open(file_path, 'r') as file:
        posts_data = json.load(file)
        return posts_data


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    file_path = os.path.join('data', 'posts.json')
    with open(file_path, 'r') as file:
        posts_data = json.load(file)
        user_posts = [post for post in posts_data['posts'] if post['poster_name'] == user_name]

        if not user_posts:
            if any(post['poster_name'] == user_name for post in posts_data['posts']):
                raise ValueError(f"No posts found for user '{user_name}'")
            else:
                raise ValueError(f"User '{user_name}' not found")

        return user_posts


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста."""
    file_path = os.path.join('data', 'comments.json')
    with open(file_path, 'r') as file:
        comments_data = json.load(file)
        post_comments = comments_data.get(str(post_id), [])

        if not post_comments:
            if str(post_id) in comments_data:
                raise ValueError(f"No comments found for post with id {post_id}")
            else:
                raise ValueError(f"Post with id {post_id} not found")

        return post_comments


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    file_path = os.path.join('data', 'posts.json')
    with open(file_path, 'r') as file:
        posts_data = json.load(file)
        matching_posts = [post for post in posts_data['posts'] if query.lower() in post['content'].lower()]

        return matching_posts


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору."""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
    raise ValueError('Пост не найден.')
