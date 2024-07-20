import requests
from django.core.management.base import BaseCommand
from Setup.models import Movie

class Command(BaseCommand):
    help = 'Fetches all movies from TMDb API and saves them to the database'

    def handle(self, *args, **kwargs):
        api_key = 'Your API key'
        base_url = 'https://api.themoviedb.org/3/movie/popular'
        page = 1
        total_movies = 0

        while True:
            response = requests.get(base_url, params={'api_key': api_key, 'page': page})
            if response.status_code == 200:
                data = response.json()
                movies = data.get('results', [])
                if not movies:
                    break

                for movie in movies:
                    title = movie.get('title', 'No Title')
                    release_date = movie.get('release_date', '0000-00-00')
                    year_released = release_date[:4] if release_date else '0000'
                    poster_path = movie.get('poster_path', '')
                    image_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ''
                    overview = movie.get('overview', '')

                    # Ensure year_released is a valid integer
                    try:
                        year_released = int(year_released)
                    except ValueError:
                        year_released = 0

                    Movie.objects.update_or_create(
                        title=title,
                        defaults={
                            'year_released': year_released,
                            'image': image_url,
                            'director': 'Unknown',  # Placeholder, as director info is not in this endpoint
                            'description': overview
                        }
                    )
                total_movies += len(movies)
                page += 1
                if page > data['total_pages']:
                    break
            else:
                self.stdout.write(self.style.ERROR(f'Failed to fetch movies: {response.status_code}'))
                break

        self.stdout.write(self.style.SUCCESS(f'Successfully fetched and saved {total_movies} movies'))
