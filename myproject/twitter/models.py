from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    # Evita conflitos com auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="twitter_users",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="twitter_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField()
    image = models.ImageField(upload_to="tweets/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)
    retweets = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
