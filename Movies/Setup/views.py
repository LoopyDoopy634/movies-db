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
            return redirect('login')
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
            return redirect('homepage')  # Change 'home' to your desired URL name for home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'home_page.html', {'movies': movies})

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

from django.shortcuts import get_object_or_404
from .models import Movie, UserReview
from .forms import SignUpForm, UserReviewForm  

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = movie.reviews.all()
    user_review = None

    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_review = UserReview.objects.filter(movie=movie, username=username).first()
            if existing_review:
                user_review = existing_review
            else:
                user_review = form.save(commit=False)
                user_review.movie = movie
                user_review.save()
                return redirect('movie_detail', movie_id=movie.id)
    else:
        form = UserReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
        'user_review': user_review,
    }
    return render(request, 'movie_detail.html', context)

from .models import Movie

from django.shortcuts import render
from .models import Movie

def search_results(request):
    query = request.GET.get('query')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
        print(f"Search query: {query}")
        print(f"Movies found: {movies.count()}")
    else:
        movies = []
    return render(request, 'search_results.html', {'movies': movies})




from django.shortcuts import render
from .models import Movie

def home(request):
    year = request.GET.get('year')
    if year:
        movies = Movie.objects.filter(year_released=year)
    else:
        movies = Movie.objects.all()  # Or an empty QuerySet if you don't want to show any movies initially
    return render(request, 'home.html', {'movies': movies})

from django.shortcuts import render
from .models import Movie


def search_by_year(request):
    return render(request, 'search_by_year.html')

def search_by_year_results(request):
    year = request.GET.get('year')
    if year:
        movies = Movie.objects.filter(year_released=year)
        print(f"Search year: {year}")
        print(f"Movies found: {movies.count()}")
    else:
        movies = []
    return render(request, 'search_results.html', {'movies': movies})

import random


def random_movie(request):
    return render(request, 'random_movie.html')

def random_movie_results(request):
    movies = Movie.objects.all()
    movie = random.choice(movies) if movies else None
    return render(request, 'random_movie.html', {'movie': movie})

