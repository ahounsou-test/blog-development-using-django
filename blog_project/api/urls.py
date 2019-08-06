from django.urls import path

from .views import UserList, UserDetail , PostDetail, PostList , CustomAuthToken , RevokeAuthToken

urlpatterns = [
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('auth-token/', CustomAuthToken.as_view(), name='api_token_get'),
    path('auth-token-revoke/<key>/', RevokeAuthToken.as_view(), name='revoke_token'),
]


