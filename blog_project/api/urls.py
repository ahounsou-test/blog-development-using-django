from django.urls import path

from .views import (
    UserList,
    UserDetail,
    BlogPostDetail,
    BlogPostList,
    CustomAuthToken,
    RevokeAuthToken,
    BlogPostDelete,
    BlogPostCreate,
    BlogPostUpdate,
)

urlpatterns = [
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('blog-post/', BlogPostList.as_view(), name='post-list'),
    path('blog-post/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    path('blog-post/delete/<int:pk>', BlogPostDelete.as_view(), name='delete-post'),
    path('blog-post/create', BlogPostCreate.as_view(), name='create-post'),
    path('blog-post/update/<int:pk>', BlogPostUpdate.as_view(), name='update-post'),

    path('auth-token/', CustomAuthToken.as_view(), name='api_token_get'),
    path('auth-token-revoke/<token>/', RevokeAuthToken.as_view(), name='revoke_token'),
]
