from django.db import models

# Create your models here.
class PostModel(models.Model):
    owner = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.owner.username} at {self.created_at}"
    
class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.owner.username} on {self.post.id}"    

class LikeModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey('users.User', related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'owner')
        ordering = ['-created_at']

    def __str__(self):
        return f"Like by {self.owner.username} on {self.post.id}"