from rest_framework import generics
from .models import Kpi
from .serializers import KpiSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def kip_list(request):
    queryset = Kpi.objects.all()
    serializer = KpiSerializer(queryset, many=True)
    return Response(serializer.data)





class KpiListCreate(generics.ListCreateAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiSerializer

class KpiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiSerializer
