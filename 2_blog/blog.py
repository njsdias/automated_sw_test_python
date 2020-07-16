# Blog has two main attributes: title, content
# Metadata, author, create dates, images

# Blog contains multiple posts title and author
# TH bolog initializes with a post empty list because
# at the it not has any posts
from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        # Representation
        # It will present the blog when we debug it
        # Write first the test and return here! It is a TDD test!
        # Make it most general as possible to tests pass!
        # If number od posts is greater than 1 it write a 's' at the end of word "post"
        return '{} by {} ({} posts)'.format(self.title,
                                            self.author,
                                            len(self.posts),
                                            's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        # The test is in the integration folder
        # because it depends by Post and Blog classes
        self.posts.append(Post(title, content))
        pass

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }