from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from companies.models import Company
from companies.serizalizers import CompaniesSerializer, CompaniesUpdateSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model
    """
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return CompaniesUpdateSerializer
        return CompaniesSerializer
