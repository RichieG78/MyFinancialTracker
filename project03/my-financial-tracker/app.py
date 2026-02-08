from flask import Flask, render_template, request, redirect, url_for, jsonify
import uuid

app = Flask(__name__)

# --- Expense Classes ---
# Base class for all expenses
class Expense:
    def __init__(self, description, amount):
        self.id = str(uuid.uuid4()) # Unique ID for identification
        self.description = description
        self.amount = float(amount)
        self.type = None # To be set by subclasses

# Subclass for fixed expenses (Target: 50%)
class FixedExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'fixed'

# Subclass for fun/discretionary expenses (Target: 30%)
class FunExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'fun'

# Subclass for savings/future expenses (Target: 20%)
class FutureExpense(Expense):
    def __init__(self, description, amount):
        super().__init__(description, amount)
        self.type = 'future'

# --- Income Classes ---
# Base class for income sources
class Income:
    def __init__(self, amount, frequency):
        self.id = str(uuid.uuid4()) # Unique ID for identification
        self.amount = float(amount)
        self.frequency = frequency
        self.description = None
        self.type = None

# Subclass for the main salary/primary income
class PrimaryIncome(Income):
    def __init__(self, amount, frequency):
        super().__init__(amount, frequency)
        self.description = "Primary Income"
        self.type = 'primary'

# Subclass for any additional income sources
class OtherIncome(Income):
    def __init__(self, amount, frequency, description=None):
        super().__init__(amount, frequency)
        self.type = 'other'
        if description:
            self.description = description
        else:
             self.description = "Other Income"

# In-memory storage (reset on server restart)
expenses = []
incomes = []

# Helper function to normalize all income to a monthly value
def calculate_monthly_income(income):
    amount = income.amount
    freq = income.frequency.lower()
    if freq == 'hourly':
        return amount * 40 * 52 / 12 # Approximation: 40hr work week
    elif freq == 'weekly':
        return amount * 52 / 12
    elif freq == 'monthly':
        return amount
    elif freq == 'annually':
        return amount / 12
    return 0

# --- Routes ---

# Home Route: Displays the dashboard
@app.route('/')
def index():
    # Calculate totals for charts
    total_income = sum(calculate_monthly_income(i) for i in incomes)
    total_fixed = sum(e.amount for e in expenses if e.type == 'fixed')
    total_fun = sum(e.amount for e in expenses if e.type == 'fun')
    total_future = sum(e.amount for e in expenses if e.type == 'future')

    return render_template('dashboard.html', 
                           expenses=expenses, 
                           incomes=incomes,
                           total_income=total_income,
                           total_fixed=total_fixed,
                           total_fun=total_fun,
                           total_future=total_future)

# Route to add new income (Handles both displaying form and processing submission)
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
                # Use provided description or generate a default like "Other 1", "Other 2"
                if not other_description:
                    count = len([i for i in incomes if i.type == 'other']) + 1
                    other_description = f"Other Income {count}"
                new_income = OtherIncome(amount, frequency, other_description)
            
            if new_income:
                incomes.append(new_income)
                return redirect(url_for('index'))

    return render_template('add-income.html')

# Route to add new expenses (Handles both displaying form and processing submission)
@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        expense_type = request.form.get('expense_type')
        
        if description and amount and expense_type:
            new_expense = None
            # Instantiate correct class based on user selection
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

# API Route: Delete Expense (Called via AJAX)
@app.route('/delete-expense/<expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    global expenses
    initial_count = len(expenses)
    # Filter out the expense with the matching ID
    expenses = [e for e in expenses if e.id != expense_id]
    
    if len(expenses) < initial_count:
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Expense not found'}), 404

# API Route: Update Expense (Called via AJAX)
@app.route('/update-expense/<expense_id>', methods=['POST'])
def update_expense(expense_id):
    data = request.json
    for expense in expenses:
        if expense.id == expense_id:
            if 'description' in data:
                expense.description = data['description']
            if 'amount' in data:
                try:
                    expense.amount = float(data['amount'])
                except ValueError:
                    return jsonify({'success': False, 'error': 'Invalid amount'}), 400
            return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Expense not found'}), 404

# API Route: Delete Income (Called via AJAX)
@app.route('/delete-income/<income_id>', methods=['DELETE'])
def delete_income(income_id):
    global incomes
    initial_count = len(incomes)
    incomes = [i for i in incomes if i.id != income_id]
    if len(incomes) < initial_count:
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Income not found'}), 404

# API Route: Update Income (Called via AJAX)
@app.route('/update-income/<income_id>', methods=['POST'])
def update_income(income_id):
    data = request.json
    for income in incomes:
        if income.id == income_id:
            if 'description' in data:
                income.description = data['description']
            if 'amount' in data:
                try:
                    income.amount = float(data['amount'])
                except ValueError:
                    return jsonify({'success': False, 'error': 'Invalid amount'}), 400
            return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Income not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
