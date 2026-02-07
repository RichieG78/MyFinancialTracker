from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/add-income', methods=['GET', 'POST'])
def add_income():
    return render_template('add-income.html')

@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    return render_template('add-expense.html')

if __name__ == '__main__':
    app.run(debug=True)
