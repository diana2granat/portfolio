from django.urls import path
from portfolioapp.views import about_view, education_view, projects_view, moreinfo_view, contact_view

urlpatterns = [
    path("", about_view, name="about"),
    path("education/", education_view, name="education"),
    path("projects/", projects_view, name="projects"),
    path("moreinfo/", moreinfo_view, name="moreinfo"),
    path("contact/", contact_view, name="contact"),
]
