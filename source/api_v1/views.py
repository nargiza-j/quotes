from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.models import Quote
from api_v1.serializers import QuoteSerializer


# class UserPermission(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         if view.action in ['list','retrieve']:
#             return Quote.objects.filter(status=1)
#         elif view.action == 'create':
#             return True
#         else:
#             return False

class QuoteCreateApi(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteListView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteSingleObjectView(APIView):
    serializer_class = QuoteSerializer

    def put(self, request, *args, pk=None, **kwargs):
        quote = get_object_or_404(Quote, pk=pk)

        serializer = self.serializer_class(data=request.data, instance=quote)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

    def get(self, request, *args, pk=None, **kwargs):
        quote = get_object_or_404(Quote, pk=pk)
        serializer = self.serializer_class(quote)
        return Response(serializer.data)

    def delete(self, request, *args, pk=None, **kwargs):
        quote = get_object_or_404(Quote, pk=pk)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)