from flask import Flask, url_for, render_template, request, abort, redirect
from CalculationManager import CalculationManager

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/", methods=['GET'])
def redirection():
    return redirect(url_for('tax_calculator'))


@app.route("/count", methods=['GET'])
def tax_calculator():
    provided_salary = request.args.get('providedSalary')
    show_description = request.args.get('showDescription')

    if not provided_salary:
        return render_template('tax.html', result=None)

    try:
        int(provided_salary)
    except ValueError:
        abort(400)


    calculation_manager = CalculationManager(float(provided_salary))
    calculation_manager.count_tax_0()
    calculation_manager.count_tax_5()
    calculation_manager.count_tax_10()
    calculation_manager.count_tax_15()
    calculation_manager.count_tax_20()
    calculation_manager.count_tax_25()
    calculation_manager.count_tax_30()


    calculation_manager.count_salary_after_taxes()

    return render_template('tax.html',
                           result=calculation_manager.get_result(),
                           provided_salary=provided_salary,
                           calculation_manager=CalculationManager,
                           show_description=show_description)


if __name__ == "__main__":
    app.run(debug= True, port='8000')
