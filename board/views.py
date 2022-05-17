import django_filters
from rest_framework import views, viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from board.models import Post
from board.serializers import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


# model-serializer
#  - HTTP로 어떤 데이터를 받을지, Response로 어떤 데이터를 출력할지 (serialization 고민을 해결한다.)
#  - 모델 생성, 업데이트, 삭제 등을 할 수 있다. (flask나 spring상에서 serivces.py 에 구현하는 내용들)

class PostViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,      # GET ~/posts/
                  mixins.RetrieveModelMixin,  # GET ~/posts/{id}/
                  mixins.UpdateModelMixin,    # POST ~/posts/{id}/
                  mixins.DestroyModelMixin):  # DELETE ~/posts/{id}/
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['category']

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # create 함수가 있으면   -> POST (resource-url)/
    # list 함수가 있으면     -> GET (resource-url)/
    # retrieve 함수가 있으면 -> GET (resource-url)/(id)/
    # destroy 함수가 있으면  -> DELETE (resource-url)/(id)/
