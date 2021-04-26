

class Result:

    def __init__(self):
        self.salary_before_tax = 0
        self.salary_after_tax = 0

        self.tax_5_pay = 0
        self.tax_10_pay = 0
        self.tax_15_pay = 0
        self.tax_20_pay = 0
        self.tax_25_pay = 0
        self.tax_30_pay = 0
        self.tax_cess_pay = 0
        # self.pension_percent = 0
        # self.pension = 0

    def get_annual(self, value):
        return round(value, 2)

    def get_month(self, value):
        return round(value / 12, 2)

    # Count based on 5 working days and 52 weeks in a year.
    def get_day(self, value):
        return round(value / (52 * 5), 2)

    # TAX FREE
    def get_annual_tax_free(self):
        return self.get_annual(self.tax_free)

    def get_month_tax_free(self):
        return self.get_month(self.tax_free)

    def get_day_tax_free(self):
        return self.get_day(self.tax_free)

    # SALARY BEFORE TAX
    def get_annual_salary_before_tax(self):
        return self.get_annual(self.salary_before_tax)

    def get_month_salary_before_tax(self):
        return self.get_month(self.salary_before_tax)

    def get_day_salary_before_tax(self):
        return self.get_day(self.salary_before_tax)

    # SALARY AFTER TAX
    def get_annual_salary_after_tax(self):
        return self.get_annual(self.salary_after_tax)

    def get_month_salary_after_tax(self):
        return self.get_month(self.salary_after_tax)

    def get_day_salary_after_tax(self):
        return self.get_day(self.salary_after_tax)

    # TAX 5%
    def get_annual_tax_5(self):
        return self.get_annual(self.tax_5_pay)

    def get_month_tax_5(self):
        return self.get_month(self.tax_5_pay)

    def get_day_tax_5(self):
        return self.get_day(self.tax_5_pay)

    # TAX 10%
    def get_annual_tax_10(self):
        return self.get_annual(self.tax_10_pay)

    def get_month_tax_10(self):
        return self.get_month(self.tax_10_pay)

    def get_day_tax_10(self):
        return self.get_day(self.tax_10_pay)

    # TAX 15%
    def get_annual_tax_15(self):
        return self.get_annual(self.tax_15_pay)

    def get_month_tax_15(self):
        return self.get_month(self.tax_15_pay)

    def get_day_tax_15(self):
        return self.get_day(self.tax_15_pay)

    # TAX 20%
    def get_annual_tax_20(self):
        return self.get_annual(self.tax_20_pay)

    def get_month_tax_20(self):
        return self.get_month(self.tax_20_pay)

    def get_day_tax_20(self):
        return self.get_day(self.tax_20_pay)

    # TAX 25%
    def get_annual_tax_25(self):
        return self.get_annual(self.tax_10_pay)

    def get_month_tax_25(self):
        return self.get_month(self.tax_25_pay)

    def get_day_tax_25(self):
        return self.get_day(self.tax_25_pay)

    # TAX 30%
    def get_annual_tax_30(self):
        return self.get_annual(self.tax_30_pay)

    def get_month_tax_30(self):
        return self.get_month(self.tax_30_pay)

    def get_day_tax_30(self):
        return self.get_day(self.tax_30_pay)

    # TAX CESS
    def get_annual_tax_cess(self):
        return self.get_annual(self.tax_cess_pay)

    def get_month_tax_cess(self):
        return self.get_month(self.tax_cess_pay)

    def get_day_tax_cess(self):
        return self.get_day(self.tax_cess_pay)

    # # NATIONAL INSURANCE 12%
    # def get_annual_ni_12(self):
    #     return self.get_annual(self.ni_12_pay)
    #
    # def get_month_ni_12(self):
    #     return self.get_month(self.ni_12_pay)
    #
    # def get_day_ni_12(self):
    #     return self.get_day(self.ni_12_pay)
    #
    # # NATIONAL INSURANCE 2%
    # def get_annual_ni_2(self):
    #     return self.get_annual(self.ni_2_pay)
    #
    # def get_month_ni_2(self):
    #     return self.get_month(self.ni_2_pay)
    #
    # def get_day_ni_2(self):
    #     return self.get_day(self.ni_2_pay)
    #
    # # PENSION
    # def get_annual_pension(self):
    #     return self.get_annual(self.pension)
    #
    # def get_month_pension(self):
    #     return self.get_month(self.pension)
    #
    # def get_day_pension(self):
    #     return self.get_day(self.pension)
