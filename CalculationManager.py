from Result import Result
from TaxConfig import TaxConfig


class CalculationManager:

    # PENSION = 0

    tax_config = TaxConfig()

    def __init__(self, provided_salary, provided_pension):
        self.salary_before_taxes = provided_salary
        # self.PENSION = provided_pension
        self.result = Result()
        self.result.salary_before_tax = provided_salary
        # self.result.pension_percent = provided_pension
        self.result.tax_free = self.tax_config.get_tax_free()

    def get_result(self):
        return self.result

    def count_tax_5(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_5_min()):
            if self.salary_before_tax > (self.tax_config.get_tax_5_max()):
                salary_above = (self.tax_config.get_tax_5_max()) - (self.tax_config.get_tax_5_min())
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_5_min())
            self.result.tax_5_pay = round(salary_above * float(0.05), 2)

    def count_tax_10(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_10_min()):
            if self.salary_before_taxes > (self.tax_config.get_tax_10_max()):
                salary_above = (self.tax_config.get_tax_10_max()) - (self.tax_config.get_tax_10_min())
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_10_min())
            self.result.tax_10_pay = round(salary_above * float(0.10), 2)

    def count_tax_15(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_15_min()):
            if self.salary_before_taxes > (self.tax_config.get_tax_15_max()):
                salary_above = (self.tax_config.get_tax_15_max()) - (self.tax_config.get_tax_15_min())
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_15_min())
            self.result.tax_15_pay = round(salary_above * float(0.15), 2)

    def count_tax_20(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_20_min()):
            if self.salary_before_taxes > (self.tax_config.get_tax_20_max()):
                salary_above = (self.tax_config.get_tax_20_max()) - (self.tax_config.get_tax_20_min())
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_20_min())
            self.result.tax_20_pay = round(salary_above * float(0.20), 2)

    def count_tax_25(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_25_min()):
            if self.salary_before_taxes > (self.tax_config.get_tax_25_max()):
                salary_above = (self.tax_config.get_tax_25_max()) - (self.tax_config.get_tax_25_min())
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_15_min())
            self.result.tax_25_pay = round(salary_above * float(0.25), 2)

    def count_tax_30(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_30_min()):
            salary_above = self.salary_before_taxes - (self.tax_config.get_tax_30_min())
            self.result.tax_30_pay = round(salary_above * float(0.30), 2)

    def count_tax_cess(self):
        salary_above = (self.result.get_annual_tax_5() + self.result.get_annual_tax_10() + self.result.get_annual_tax_15() + self.result.get_annual_tax_20() + self.result.get_annual_tax_25() + self.result.get_annual_tax_30())
        self.result.tax_cess_pay = round(salary_above * float(0.04), 2)
    # def count_ni_12(self):
    #     if self.salary_before_taxes > self.tax_config.get_year_ni_12():
    #         if self.salary_before_taxes > self.tax_config.get_year_ni_2():
    #             salary_above = self.tax_config.get_year_ni_2() - self.tax_config.get_year_ni_12()
    #         else:
    #             salary_above = self.salary_before_taxes - self.tax_config.get_year_ni_12()
    #         self.result.ni_12_pay = round(salary_above * float(0.12), 2)
    #
    # def count_ni_2(self):
    #     if self.salary_before_taxes > self.tax_config.get_year_ni_2():
    #         salary_above = self.salary_before_taxes - self.tax_config.get_year_ni_2()
    #         self.result.ni_2_pay = round(salary_above * float(0.02), 2)
    #
    # def count_pension(self):
    #     if self.result.pension_percent != 0:
    #         pension_pay = self.result.salary_before_tax * self.result.pension_percent / 100
    #         self.result.salary_after_tax = self.result.salary_after_tax - pension_pay
    #         self.PENSION = pension_pay
    #         self.result.pension = pension_pay

    def count_salary_after_taxes(self):
        self.result.salary_after_tax = self.result.salary_before_tax \
                                       - self.result.get_annual_tax_30() \
                                       - self.result.get_annual_tax_25() \
                                       - self.result.get_annual_tax_20() \
                                       - self.result.get_annual_tax_15() \
                                       - self.result.get_annual_tax_10() \
                                       - self.result.get_annual_tax_5() \
                                       - self.result.get_annual_tax_cess() \
                                       # - self.result.get_annual_ni_12() \
                                       # - self.result.get_annual_ni_2() \
                                       # - self.result.get_annual_pension()