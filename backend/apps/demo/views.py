from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
import random

# Serializers
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'user', 'comments']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

# Views
class PostListView(APIView):
    def get(self, request):
        # Pagination: Limit the number of posts per request
        posts = Post.objects.all().order_by('-timestamp')[:10]  # Adjust the limit as needed
        data = []

        for post in posts:
            comments = post.comments.all()
            random_comments = random.sample(list(comments), min(len(comments), 3))  # Sampling up to 3 comments
            
            # Serialize the post and random comments
            post_data = {
                'text': post.text,
                'timestamp': post.timestamp,
                'user': UserSerializer(post.user).data,  # Serialize user
                'comment_count': comments.count(),
                'comments': CommentSerializer(random_comments, many=True).data
            }
            data.append(post_data)
        
        return Response(data, status=status.HTTP_200_OK)
