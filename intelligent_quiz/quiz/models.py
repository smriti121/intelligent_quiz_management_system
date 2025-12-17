from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# -------------------------
# 1. USER PROFILE
# -------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    preferences = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Signal to create / save user profile automatically
@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    """
    Ensures every User has a UserProfile.
    If user is newly created, create a profile.
    If user exists but profile exists, save it.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Only save if the profile exists, avoids RelatedObjectDoesNotExist
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()


# -------------------------
# 2. CATEGORY MODEL
# -------------------------
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------------
# 3. QUESTION MODEL
# -------------------------
class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question_text = models.CharField(max_length=300)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    CORRECT_ANSWER_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    correct_answer = models.CharField(
        max_length=7,
        choices=CORRECT_ANSWER_CHOICES,
        default='option1'
    )

    def __str__(self):
        return f"{self.question_text} ({self.category.name})"


# -------------------------
# 4. QUIZ ATTEMPT (Score Table)
# -------------------------
class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', '-date_taken']  # leaderboard style

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions}"
