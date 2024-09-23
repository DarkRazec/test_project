from rest_framework.exceptions import ValidationError

from companies.services import get_company_level


class CompanyLevelValidator:

    def __call__(self, value):
        if value.get('supplier') is not None:
            match get_company_level(value.get('supplier')):
                case 2:
                    raise ValidationError("Lvl 3 companies cannot be created")
