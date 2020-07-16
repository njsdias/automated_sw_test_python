from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

# patch allow us compares the output of a print


class AppTest(TestCase):

    def test_print_blogs(self):

        # Load class Blog
        blog = Blog('Test', 'Test Author')

        # Put the value in the app.py blogs dictionary
        app.blogs = {'Test': blog}

        # Here we go to compare what app.py prints with a string using the mock_print
        with patch('builtins.print') as mocked_print:
            # call function to print the dictionary content defined next by mocked_print
            app.print_blogs()

            # compares the previous print with the string
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')


