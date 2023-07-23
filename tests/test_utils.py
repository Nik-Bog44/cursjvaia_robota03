import unittest
from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts


class TestGetPostsAll(unittest.TestCase):
    def test_return_type(self):
        posts = get_posts_all()
        self.assertIsInstance(posts, list)

    def test_not_empty(self):
        posts = get_posts_all()
        self.assertGreater(len(posts), 0)


class TestGetCommentsByPostId(unittest.TestCase):
    def test_post_not_found(self):
        with self.assertRaises(ValueError):
            get_comments_by_post_id(999)

    def test_return_type(self):
        post_id_with_comments = 1  # Предполагаем, что пост с id=1 содержит комментарии
        comments = get_comments_by_post_id(post_id_with_comments)
        self.assertIsInstance(comments, list)


class TestGetPostByPk(unittest.TestCase):
    def test_post_not_found(self):
        with self.assertRaises(ValueError):
            get_post_by_pk(999)

    def test_return_type(self):
        post_id = 1  # Предполагаем, что пост с id=1 существует
        post = get_post_by_pk(post_id)
        self.assertIsInstance(post, dict)
        self.assertEqual(post['pk'], post_id)


class TestSearchForPosts(unittest.TestCase):
    def test_return_type(self):
        query = "Python"
        posts = search_for_posts(query)
        self.assertIsInstance(posts, list)

    def test_not_empty(self):
        query = "Python"
        posts = search_for_posts(query)
        self.assertGreater(len(posts), 0)

    def test_case_insensitive(self):
        query = "python"
        posts = search_for_posts(query)
        self.assertGreater(len(posts), 0)

    def test_no_results(self):
        query = "NonExistentQuery"
        posts = search_for_posts(query)
        self.assertEqual(len(posts), 0)


if __name__ == '__main__':
    unittest.main()
