from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework import permissions  # autentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import renderers


# *********************** Snippets ***********************************************
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ****************************** Users ***********************************************
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ****************************** Users by username *********************************
class UsersByUsername(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = self.kwargs['username']
        return User.objects.filter(username=users)

    def get(self, request, *args, **kwargs):
        if not self.get_queryset():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return self.list(request, *args, **kwargs)
