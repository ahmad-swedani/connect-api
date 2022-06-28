from django.urls import path
from .views import (
    PostViewsList,
    PostDetail,
    OfferViewsList,
    OfferDetail,
    CommentViewsList,
    CommentDetail,
    ActivityViewsList,
    ActivityDetail
)

urlpatterns = [
    path("post", PostViewsList.as_view(), name="post"),
    path("post/<int:pk>/post_detail", PostDetail.as_view(), name="post_detail"),
    path("offer/", OfferViewsList.as_view(), name="offer"),
    path("offer/<int:pk>/offer_detail/", OfferDetail.as_view(), name="offer_detail"),
    path("comment", CommentViewsList.as_view(), name="comment"),
    path(
        "comment/<int:pk>/comment_detail/",
        CommentDetail.as_view(),
        name="comment_detail",
    ),
    path("activity", ActivityViewsList.as_view(), name="activity"),
    path(
        "activity/<int:pk>/activity_detail/",
        ActivityDetail.as_view(),
        name="activity_detail",
    ),
]
