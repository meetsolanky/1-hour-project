import random
import uuid
from django.contrib.auth.models import User
from apps.demo.models import Post, Comment  # Replace 'myapp' with the actual app name
from faker import Faker
from django.utils import timezone

# Initialize Faker
fake = Faker()

# Generate some users
def create_users(num_users=10):
    users = []
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        user = User.objects.create_user(username=username, email=email, password='password123')
        users.append(user)
    return users

# Generate posts for users
def create_posts(users, num_posts=50):
    posts = []
    for _ in range(num_posts):
        user = random.choice(users)
        post = Post.objects.create(
            text=fake.text(),
            user=user,
            timestamp=fake.date_time_this_decade()
        )
        posts.append(post)
    return posts

# Generate comments for posts
def create_comments(posts, users, num_comments=200):
    comments = []
    for _ in range(num_comments):
        post = random.choice(posts)
        user = random.choice(users)
        comment = Comment.objects.create(
            text=fake.text(),
            post=post,
            user=user,
            timestamp=fake.date_time_this_decade()
        )
        comments.append(comment)
    return comments

# Create dummy data
def generate_dummy_data(num_users=10, num_posts=50, num_comments=200):
    users = create_users(num_users)
    posts = create_posts(users, num_posts)
    comments = create_comments(posts, users, num_comments)
    print(f"Created {num_users} users, {num_posts} posts, and {num_comments} comments.")

# Run the script
if __name__ == "__main__":
    generate_dummy_data()
