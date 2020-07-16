from unittest import TestCase
from post import Post


class PostTest(TestCase):

    def test_create_post(self):
        # Post is an object that contains a Title Test and Content of Content Test
        p = Post('Test', 'Test Content')

        # It's says: TestCase verify if string 'Test' and post Title are the same
        # In this situation they are.
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {
            'title': "Test",
            'content': "Test Content"
        }

        self.assertDictEqual(expected, p.json())



