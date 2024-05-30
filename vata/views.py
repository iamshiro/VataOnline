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

        genre_ids = request.GET.getlist('genre')
        type_ids = request.GET.getlist('type')
        years_selected = request.GET.getlist('year')

        films = Movie.objects.all()

        if query:
            films = films.filter(title__icontains=query)
        if genre_ids:
            films = films.filter(genres__in=genre_ids).distinct()
        if type_ids:
            films = films.filter(types__in=type_ids).distinct()
        if years_selected:
            films = films.filter(year__in=years_selected)

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
        return redirect('movie', pk=pk)