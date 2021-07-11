from django.urls import path
from airport.views import (
    AirportViews, AirportDetailsViews, RunwayViews,
    RunwayDetailsViews, SurfaceViews, SurfaceDetailsViews
)

urlpatterns = [
    path('airports/', AirportViews.as_view()),
    path('single-airport/<int:pk>/', AirportDetailsViews.as_view()),
    path('runways/', RunwayViews.as_view()),
    path('single-runway/<int:pk>/', RunwayDetailsViews.as_view()),
    path('surfaces/', SurfaceViews.as_view()),
    path('single-surface/<int:pk>/', SurfaceDetailsViews.as_view()),
]