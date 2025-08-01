from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # Beschränkt auf die letzten 5 Einträge
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log_message/", views.log_message, name="log_message"),
]

urlpatterns += staticfiles_urlpatterns()


