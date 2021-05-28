from rest_framework.generics import ListAPIView
from .serializers import PreziSerializer
from .models import Prezi



class ListPrezis(ListAPIView):
    serializer_class = PreziSerializer
    def get_queryset(self):
        search_value = self.request.query_params.get('search_value')
        ascending = self.request.query_params.get('ascending')
        if search_value:
            queryset = Prezi.objects.filter(title__icontains=search_value)
        else:
            queryset = Prezi.objects.all()
        if ascending == 'false':
            return queryset.order_by('-created_at')
        return queryset

