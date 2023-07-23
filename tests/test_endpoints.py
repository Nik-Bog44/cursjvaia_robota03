import requests


def test_get_all_posts():
    url = 'http://localhost:5000/api/posts'
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for post in response.json():
        assert isinstance(post, dict)
        assert 'poster_name' in post
        assert 'poster_avatar' in post
        assert 'pic' in post
        assert 'content' in post
        assert 'views_count' in post
        assert 'likes_count' in post
        assert 'pk' in post


def test_get_post_by_id():
    post_id = 1  # Здесь указываем идентификатор конкретного поста
    url = f'http://localhost:5000/api/posts/{post_id}'
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    post = response.json()
    assert 'poster_name' in post
    assert 'poster_avatar' in post
    assert 'pic' in post
    assert 'content' in post
    assert 'views_count' in post
    assert 'likes_count' in post
    assert 'pk' in post
