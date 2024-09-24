from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html

from companies.models import Company


@admin.register(Company)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link')
    list_filter = ('city',)

    @admin.display(description="supplier")
    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse('admin:companies_company_change', args=[obj.supplier.pk])
            link = format_html('<a href="{}">{}</a>', url, obj.supplier.name)
            return link
        return "-"

    @admin.action(description="Clear debt")
    def clear_debt(self, request, queryset):
        """
        Admin action for clearing debt.
        """
        updated_count = 0
        for obj in queryset:
            if obj.supplier:
                obj.debt = 0
                obj.save()
                updated_count += 1
            else:
                messages.warning(request, f"Company '{obj}' doesn't have a supplier.")
        if updated_count:
            messages.success(request, f"Debt has been cleared for {updated_count} companies.")
        else:
            messages.info(request, f"Companies with a supplier was not found.")

    actions = [clear_debt]
