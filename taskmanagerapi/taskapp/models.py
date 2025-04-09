from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone


# 👤 Custom User
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# 🧱 Abstract Base Model (for reusability)
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# profile model
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    


# 📌 Tag for categorizing tasks
class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# ✅ Task Model
class Task(BaseModel):
    PRIORITY_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date()

    def __str__(self):
        return self.title
