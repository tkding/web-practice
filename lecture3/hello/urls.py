from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"), #[nothing at the end of the route, what view should be rendered, for referencing]
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")
]

