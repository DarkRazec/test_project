def get_company_level(company):
    """Возвращает уровень компании в иерархии."""
    if company.supplier:
        return get_company_level(company.supplier) + 1
    else:
        return 0
