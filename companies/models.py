# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Analysis(models.Model):
    id = models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    sales_growth = models.TextField(blank=True, null=True)
    profit_growth = models.TextField(blank=True, null=True)
    roe = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis'


class Balancesheet(models.Model):
    id = models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    equity_share_capital = models.TextField(blank=True, null=True)
    reserves = models.TextField(blank=True, null=True)
    borrowings = models.TextField(blank=True, null=True)
    other_liabilities = models.TextField(blank=True, null=True)
    total_liabilities = models.TextField(blank=True, null=True)
    fixed_assets = models.TextField(blank=True, null=True)
    cwip = models.TextField(blank=True, null=True)
    investments = models.TextField(blank=True, null=True)
    other_assets = models.TextField(blank=True, null=True)
    total_assets = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balancesheet'


class Cashflow(models.Model):
    id =  models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    cash_from_operating_activity = models.TextField(blank=True, null=True)
    cash_from_investing_activity = models.TextField(blank=True, null=True)
    cash_from_financing_activity = models.TextField(blank=True, null=True)
    net_cash_flow = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashflow'


class Companies(models.Model):
    symbol = models.TextField(primary_key=True)
    company_logo = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    nse_profile = models.TextField(blank=True, null=True)
    bse_profile = models.TextField(blank=True, null=True)
    face_value = models.TextField(blank=True, null=True)
    book_value = models.TextField(blank=True, null=True)
    roce_percentage = models.TextField(blank=True, null=True)
    roe_percentage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Documents(models.Model):
    id = models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    annual_report = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class ProfitDashboard(models.Model):
    company_id = models.TextField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    sales = models.TextField(blank=True, null=True)
    expenses = models.TextField(blank=True, null=True)
    operating_profit = models.TextField(blank=True, null=True)
    opm_percentage = models.TextField(blank=True, null=True)
    other_income = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    depreciation = models.TextField(blank=True, null=True)
    profit_before_tax = models.TextField(blank=True, null=True)
    tax_percentage = models.TextField(blank=True, null=True)
    net_profit = models.TextField(blank=True, null=True)
    eps = models.TextField(blank=True, null=True)
    dividend_payout_percentage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profit_dashboard'


class Profitandloss(models.Model):
    id = models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    sales = models.TextField(blank=True, null=True)
    expenses = models.TextField(blank=True, null=True)
    operating_profit = models.TextField(blank=True, null=True)
    opm_percentage = models.TextField(blank=True, null=True)
    other_income = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    depreciation = models.TextField(blank=True, null=True)
    profit_before_tax = models.TextField(blank=True, null=True)
    tax_percentage = models.TextField(blank=True, null=True)
    net_profit = models.TextField(blank=True, null=True)
    eps = models.TextField(blank=True, null=True)
    dividend_payout_percentage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profitandloss'


class Prosandcons(models.Model):
    id = models.TextField(primary_key=True)
    company_id = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prosandcons'
