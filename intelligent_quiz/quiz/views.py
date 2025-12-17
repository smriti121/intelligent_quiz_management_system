# quiz/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, QuizAttempt, UserProfile
from .forms import UserForm, UserProfileForm


# ---------------- Home Page ----------------
def home(request):
    return render(request, 'quiz/home.html')


# ---------------- Registration ----------------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'quiz/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'quiz/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'quiz/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)

        # Render the same page with success message
        messages.success(request, "Registration successful! You can now login.")
        return render(request, 'quiz/register.html')  # <-- do NOT redirect

    return render(request, 'quiz/register.html')




# ---------------- Login ----------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'quiz/login.html')


# ---------------- Logout ----------------
def user_logout(request):
    logout(request)
    return redirect('home')


# ---------------- Profile Page ----------------
@login_required
def profile(request):
    user_profile = request.user.userprofile
    attempts = QuizAttempt.objects.filter(user=request.user).order_by('-date_taken')

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'quiz/profile.html', {
        "user_form": user_form,
        "profile_form": profile_form,
        "attempts": attempts
    })


# ---------------- Start Quiz ----------------
@login_required
def start_quiz(request):
    questions = list(Question.objects.all())
    total = len(questions)

    if total == 0:
        return render(request, "quiz/start_quiz.html", {"question": None, "score": 0, "total": 0})

    # Initialize session quiz state
    if "q_no" not in request.session:
        request.session["q_no"] = 0
        request.session["score"] = 0

    q_no = request.session["q_no"]

    # Quiz completed
    if q_no >= total:
        score = request.session["score"]

        # Save attempt
        QuizAttempt.objects.create(
            user=request.user,
            score=score,
            total_questions=total
        )

        # Clear session
        for key in ["q_no", "score"]:
            if key in request.session:
                del request.session[key]

        return render(request, "quiz/start_quiz.html", {"question": None, "score": score, "total": total})

    # Current question
    question = questions[q_no]
    options = [
        question.option1,
        question.option2,
        question.option3,
        question.option4
    ]

    if request.method == "POST":
        selected = request.POST.get("answer")

        if selected == question.correct_answer:
            request.session["score"] += 1

        request.session["q_no"] += 1
        return redirect('start_quiz')

    return render(request, "quiz/start_quiz.html", {
        "question": question,
        "options": options,
        "current": q_no + 1,
        "total": total
    })


# ---------------- Leaderboard ----------------
def leaderboard(request):
    scores = QuizAttempt.objects.order_by('-score', '-date_taken')[:10]
    return render(request, "quiz/leaderboard.html", {"scores": scores})
