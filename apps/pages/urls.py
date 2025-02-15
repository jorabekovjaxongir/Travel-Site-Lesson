from django.urls import path
from .views import(
    destinationView,
    explore_tourView,
    travel_bookingView,
    our_galleryView,
    travel_guideView,
    testimonialView
)

urlpatterns = [
    path('destination/', destinationView, name='destination'),
    path('explore-tour/', explore_tourView, name='explore_tour'),
    path('travel-booking/', travel_bookingView, name='travel_booking'),
    path('our-gallery/', our_galleryView, name='our_gallery'),
    path('travel-guide/', travel_guideView, name='travel_guide'),
    path('testimonial/', testimonialView, name='testimonial'),
]
