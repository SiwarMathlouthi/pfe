from django.urls import path
from .views import KpiListCreate, KpiDetail

urlpatterns = [
    path('kpi/', KpiListCreate.as_view(), name='kpi-list-create'),
    path('kpi/<int:pk>/', KpiDetail.as_view(), name='kpi-detail'),
]
