class Post:
    # class has two proprieties: title and content
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Post can saves a MongoDB database
    # Display it as dictionary or send it by a REST API
    # through a json
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
