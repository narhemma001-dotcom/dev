from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import PostModel

class SimplePostTest(TestCase):
    """Super basic tests - just to learn"""
    
    def test_create_user(self):
        """Test we can create a user"""
        user = User.objects.create_user('test', 'test@test.com', 'test123')
        self.assertEqual(user.username, 'test')
        print("✅ TEST 1 PASSED: Can create user")
    
    def test_create_post(self):
        """Test we can create a post"""
        user = User.objects.create_user('author', 'author@test.com', 'test123')
        post = PostModel.objects.create(
            title='Test Post',
            content='Hello World',
            author=user
        )
        self.assertEqual(post.title, 'Test Post')
        print("✅ TEST 2 PASSED: Can create post")

class PublicAPITest(TestCase):
    """Test API endpoints"""
    
    def test_anyone_can_view_posts(self):
        """Test GET /api/posts/ (should work for anyone)"""
        client = APIClient()
        response = client.get('/api/posts/')
        
        # Check status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        print("✅ TEST 3 PASSED: Anyone can view posts")
        
        # Optional: Check response format
        self.assertIn('application/json', response['Content-Type'])