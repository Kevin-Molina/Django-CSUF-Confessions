from django.urls import path, re_path

from . import views

urlpatterns = [
    path("submit/", views.ConfessionCreateView.as_view(), name="submit_confession"),
    path("<int:pk>/vote/", views.VoteSubmitView.as_view(), name="submit_vote"),
    path(
        "<int:pk>/delete/",
        views.ConfessionDeleteView.as_view(),
        name="delete_confession",
    ),
    path("<int:pk>/comments/", views.CommentListView.as_view(), name="view_confession"),
    path(
        "<int:pk>/comments/submit",
        views.CommentSubmitView.as_view(),
        name="submit_comment",
    ),
    path("", views.ConfessionListView.as_view(), name="confessions"),
]
