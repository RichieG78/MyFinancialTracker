from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Expense Classes ---
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = float(amount)
        self.type = None # To be set by subclasses

class FixedExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'fixed'

class FunExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'fun'

class FutureExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'future'

# --- Income Classes ---
class Income:
    def __init__(self, amount, frequency):
        self.amount = float(amount)
        self.frequency = frequency
        self.description = None
        self.type = None

class PrimaryIncome(Income):
    def __init__(self, amount, frequency):
        super().__init__(amount, frequency)
        self.description = "Primary Income"
        self.type = 'primary'

class OtherIncome(Income):
    def __init__(self, amount, frequency, description=None):
        super().__init__(amount, frequency)
        self.type = 'other'
        if description:
            self.description = description
        else:
             self.description = "Other Income"

# In-memory storage
expenses = []
incomes = []

@app.route('/')
def index():
    return render_template('dashboard.html', expenses=expenses, incomes=incomes)

@app.route('/add-income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        amount = request.form.get('amount')
        frequency = request.form.get('frequency')
        income_type = request.form.get('income_type')
        other_description = request.form.get('other_description')

        if amount and frequency and income_type:
            new_income = None
            if income_type == 'primary':
                new_income = PrimaryIncome(amount, frequency)
            elif income_type == 'other':
                # Use provided description or generate a default like "Other 1", "Other 2" based on existing count
                if not other_description:
                    count = len([i for i in incomes if i.type == 'other']) + 1
                    other_description = f"Other Income {count}"
                new_income = OtherIncome(amount, frequency, other_description)
            
            if new_income:
                incomes.append(new_income)
                return redirect(url_for('index'))

    return render_template('add-income.html')

@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        expense_type = request.form.get('expense_type')
        
        if description and amount and expense_type:
            new_expense = None
            if expense_type == 'fixed':
                new_expense = FixedExpense(description, amount)
            elif expense_type == 'fun':
                new_expense = FunExpense(description, amount)
            elif expense_type == 'future':
                new_expense = FutureExpense(description, amount)
            
            if new_expense:
                expenses.append(new_expense)
                return redirect(url_for('index'))
            
    return render_template('add-expense.html')

if __name__ == '__main__':
    app.run(debug=True)
