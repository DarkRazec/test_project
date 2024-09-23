from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from companies.models import Company
from companies.serizalizers import CompaniesSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model
    """
    serializer_class = CompaniesSerializer
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)
