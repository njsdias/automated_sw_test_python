from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):

        # Load Blog class
        b = Blog('Test', 'Test Author')

        # Create post that receives a title and a content
        b.create_post('Test Post', 'Test Content')

        # Make asserts
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': "Test",
            'author': "Test Author",
            'posts': []
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': "Test",
            'author': "Test Author",
            'posts': [{'title': 'Test Post', 'content': 'Test Content'}]
        }

        self.assertDictEqual(expected, b.json())
