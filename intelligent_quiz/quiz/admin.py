from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Category, Question, QuizAttempt

# -------------------------
# 1. USER PROFILE INLINE
# -------------------------
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Extend the default User admin to include the UserProfile
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Unregister the original User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# -------------------------
# 2. CATEGORY
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# -------------------------
# 3. QUESTION
# -------------------------
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'get_correct_answer_text')
    list_filter = ('category',)
    search_fields = ('question_text',)

    def get_correct_answer_text(self, obj):
        # Shows the actual option text instead of 'option1', 'option2', etc.
        return getattr(obj, obj.correct_answer)
    get_correct_answer_text.short_description = 'Correct Answer'


# -------------------------
# 4. QUIZ ATTEMPT
# -------------------------
@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'score', 'total_questions', 'date_taken')
    list_filter = ('category', 'date_taken')
    search_fields = ('user__username',)
    ordering = ('-score', '-date_taken')
