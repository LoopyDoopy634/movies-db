from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def landing_page(request):
    return render(request, 'landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to home page upon successful login
            return redirect('home')  # Change 'home' to your desired URL name for home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def home_page(request):
    # Render your home page template
    return render(request, 'home.html')

import requests
from django.http import JsonResponse
from django.conf import settings

GITHUB_REPO_OWNER = 'LoopyDoopy634'
GITHUB_REPO_NAME = 'movies-db'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/commits'

def fetch_commits():
    response = requests.get(GITHUB_API_URL)
    commits = response.json()
    return commits

def commit_list(request):
    commits = fetch_commits()
    context = {
        'commits': commits
    }
    return render(request, 'commit_list.html', context)
