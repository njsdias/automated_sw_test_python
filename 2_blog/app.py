
# Create small user interfaces for users can creates blogs and posts

blogs = dict() # blog_name : Blog object


def menu():
    # Show the useres the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()


def print_blogs():
    # Print the available blogs
    # [(blog_name, Blog) , (blog_name, Blog)]
    for key, blog in blogs.items():
        print('- {}'.format(blog))
