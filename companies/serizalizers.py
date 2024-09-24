from rest_framework import serializers

from companies.models import Company
from companies.services import get_company_level
from companies.validators import CompanyLevelValidator
from products.serializers import ProductsSerializer


class CompaniesSerializer(serializers.ModelSerializer):
    """Serializer for Employee objects"""
    level = serializers.SerializerMethodField()
    products = ProductsSerializer(source='product_set', many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        validators = [
            CompanyLevelValidator(),
        ]

    @staticmethod
    def get_level(obj):
        return get_company_level(obj)

    def validate_supplier(self, value):
        """Validator for supplier field"""

        if self.instance and value:
            if self.instance.id == value.id:
                raise serializers.ValidationError("A company cannot be a supplier to itself.")
            if not self.instance.supplier and Company.objects.filter(supplier=self.instance).exists():
                raise serializers.ValidationError("Factory's supplier field cannot be changed")

        return value


class CompaniesUpdateSerializer(CompaniesSerializer):
    class Meta(CompaniesSerializer.Meta):
        extra_kwargs = {
            'debt': {'read_only': True},
        }
