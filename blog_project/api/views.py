from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from users.models.user_model import User

# Create your views here.
from rest_framework import generics, permissions, status

from api.serializers.blog_post import PostSerializer
from api.serializers.user import UserSerializer
from blog.models.blog_post import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Only author can modified or delete blog.
        return obj.author == request.user


class RevokeTokenPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only author can modified or delete blog.
        return obj.user == request.user


# allow a user to revoke access to a token
class RevokeAuthToken(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, RevokeTokenPermission]
    lookup_field = 'key'
    lookup_url_kwarg = 'token'
    queryset = Token.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Token Revoked", status=status.HTTP_200_OK)


class BlogPostList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogPostDetail(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogPostUpdate(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, CustomPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request.data['author'] = request.user.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class BlogPostDelete(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, CustomPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        import pdb
        pdb.set_trace()
        self.perform_destroy(instance)
        return Response(f"Blog post with id:{kwargs['pk']} deleted", status=status.HTTP_200_OK)


class BlogPostCreate(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, CustomPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # making sure post is associated with current login user
        request.data['author'] = request.user.id
        serializer = self.get_serializer(data=request.data, )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
