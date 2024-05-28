from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import View
from .models import Movie, Types, Genre
from datetime import date
from .forms import AddCommentsForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'VATAONLINE/index.html')


class Feedback(View):
    def get(self, request):
        return render(request, 'VATAONLINE/feedback.html')


class FilmList(View):
    def get(self, request):
        genres = Genre.objects.all()
        types = Types.objects.all()
        years = Movie.objects.values_list('year', flat=True).distinct()
        query = request.GET.get('query')

        genre_id = request.GET.get('genre')
        type_id = request.GET.get('type')
        year = request.GET.get('year')

        films = Movie.objects.all()

        if query:
            films = films.filter(title__icontains=query)
        if genre_id:
            films = films.filter(genres=genre_id)
        if type_id:
            films = films.filter(types=type_id)
        if year:
            films = films.filter(year=year)

        return render(request, 'VATAONLINE/films.html',
                      {'films': films, 'genres': genres, 'types': types, 'years': years})

    def post(self, request):
        query = request.POST.get('query')
        if query:
            return redirect(f'/films/?query={query}')
        return redirect('films')


class NewFilms(View):
    def get(self, request):
        current_year = date.today().year
        films = Movie.objects.filter(year=current_year)
        return render(request, 'VATAONLINE/new.html', {'films': films})


class PostDetailView(View):
    def get(self, request, pk):
        films = Movie.objects.get(id=pk)
        comments = films.addcomments_set.all()
        return render(request, 'VATAONLINE/movie_detail.html', {'film': films, 'comments': comments})


class AddComments(View):
    def post(self, request, pk):
        form = AddCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = get_object_or_404(Movie, pk=pk)
            comment.save()
        return redirect(f'/{pk}')
