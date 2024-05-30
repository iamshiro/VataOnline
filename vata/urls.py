from django.urls import path
from . import views

urlpatterns = [path('', views.IndexView.as_view(), name='index'),
               path('films/', views.FilmList.as_view(), name='films'),
               path('new/', views.NewFilms.as_view(), name='new'),
               path('feedback/', views.Feedback.as_view(), name='feedback'),
               path('review/<int:pk>', views.AddComments.as_view(), name='addcomments'),
               path('films/<int:pk>/', views.PostDetailView.as_view(), name='movie'),
               path('new/<int:pk>/', views.PostDetailView.as_view(), name='movie'),
               ]
