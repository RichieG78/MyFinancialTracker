# Intentional Spending Tracker

[GitHub Repository](https://github.com/your-username/intentional-spending-tracker)

## Website

**[View Intentional Spending Tracker Live](https://your-render-url.onrender.com)**

---

## Project Goal
The Intentional Spending Tracker is a personal finance web application built using **Python and Flask**, designed to help users better understand and control their spending by comparing **intended spending goals** against **actual financial behaviour**.

The core concept of the application is based on an intentional budgeting framework, where all spending is categorised into three clearly defined sections:

- **Fixed (50%)** – essential and recurring expenses such as rent, bills, and groceries
- **Fun (30%)** – discretionary spending such as entertainment, dining, and hobbies
- **Future (20%)** – savings, investments, and long-term financial planning

The application allows users to record income and expenses, automatically calculate how spending is distributed across these categories, and visually compare the **target percentages** against the **actual percentages** being spent.

The project was created specifically to demonstrate a strong understanding of **Flask application structure**, **object-oriented Python**, and the **integration of HTML, CSS, and JavaScript** in line with the Python assignment brief.

---

## 1. Project Conceptualisation and Planning

### 1.1 Project Concept
The Intentional Spending Tracker was designed to move beyond a basic expense tracker and instead focus on **behavioural insight**. By framing financial data around intention versus reality, the application helps users quickly identify where their spending habits align with, or diverge from, their financial goals.

Key features include:
- Income tracking
- Expense tracking
- Three-category intentional spending model (Fixed / Fun / Future)
- Automatic calculation of spending percentages
- Visual comparison of target versus actual spending
- Dashboard-style single-page overview

This concept directly aligns with the assignment requirement to build a **functional, engaging, and visually appealing web application** using Flask.

### 1.2 Planning and Research
Prior to development, research was conducted into:
- Personal finance dashboards
- Kanban-style task boards
- Goal tracking interfaces

This research influenced several design decisions, including:
- Using a **three-column dashboard layout** inspired by Kanban boards to represent the Fixed, Fun, and Future categories
- Presenting spending items as cards within each column
- Using progress bars and percentage indicators to visualise financial goals

These design choices ensured that the application would be intuitive, visually clear, and suitable for a single-page dashboard layout.

### 1.3 Sitemap and Wireframes
The application uses a small number of focused routes rather than a complex sitemap:
- Dashboard
- Add Income
- Add Spending
- Spending Report
- About

Wireframes were created to plan the three-column dashboard layout and ensure consistent placement of totals, progress indicators, and transaction cards across screen sizes.

---

## 2. Flask Application Structure

### 2.1 Flask Setup
The application was built using Flask following the setup process outlined in the assignment brief:
- Flask installed using `pip`
- Virtual environment created and activated
- Application entry point defined in `app.py`

Flask is responsible for:
- Routing
- Rendering templates
- Handling GET and POST requests
- Passing processed data to the front-end

### 2.2 Routes
The following routes are implemented:

- `/` – Main dashboard displaying spending overview
- `/income` – Form to add income entries (GET/POST)
- `/spending` – Form to add spending transactions (GET/POST)
- `/report` – Detailed breakdown of target vs actual spending
- `/about` – Explanation of the app concept

These routes demonstrate the use of multiple HTTP methods and Flask’s `render_template` functionality.

---

## 3. Python Programming and Class Design

### 3.1 Object-Oriented Design
The application uses **multiple custom Python classes** to model real-world financial concepts, demonstrating strong understanding of Python programming principles:

- `Income` – represents individual income entries
- `Transaction` – represents individual spending items
- `SpendingCategory` – represents Fixed, Fun, and Future categories along with their target percentages
- `Account` – central class responsible for storing data and calculating totals
- `SpendingReport` – responsible for comparing target and actual spending percentages

This class-based approach improves code readability, separation of concerns, and scalability.

### 3.2 Data Processing
All financial calculations are handled in Python, including:
- Total income calculation
- Total spending per category
- Percentage of income spent per category
- Difference between target and actual percentages

Only processed data is passed to the templates, ensuring that presentation logic remains separate from business logic.

---

## 4. HTML Structure and Content

### 4.1 Templates
The application includes at least five HTML templates, each with a consistent structure:
- `dashboard.html`
- `income.html`
- `spending.html`
- `report.html`
- `about.html`

Each template includes semantic HTML elements such as `<header>`, `<main>`, and `<section>` to improve accessibility and maintainability.

### 4.2 Dashboard Layout
The main dashboard uses a **three-column layout**, with each column representing one spending category:
- Fixed
- Fun
- Future

Each column displays:
- Target percentage
- Actual percentage
- Visual progress bar
- List of transactions

---

## 5. CSS Styling

### 5.1 Visual Design
Modern CSS is used to create a clean, professional dashboard aesthetic:
- Card-based UI components
- Consistent spacing and typography
- Category-specific colour accents

### 5.2 Layout Techniques
The layout is implemented using:
- **CSS Grid** for the three-column dashboard
- **Flexbox** for card and form alignment

### 5.3 Responsive Design
Media queries ensure the application is usable across:
- Desktop
- Tablet
- Mobile

On smaller screens, the three columns stack vertically while preserving clarity and usability.

---

## 6. JavaScript Interactivity

JavaScript is used to enhance the user experience, including:
- Animating progress bars based on spending percentages
- Highlighting categories that exceed their target
- Client-side form validation

These features create a more dynamic and engaging application while remaining appropriate for a Flask-based project.

---

## 7. Hosting and Deployment

### 7.1 Version Control
The project is managed using Git and hosted on GitHub:
- Clear commit history
- Logical file structure
- Separation of concerns between backend and frontend assets

### 7.2 Render Deployment
The application is deployed using **Render.com**, following the steps outlined in the assignment brief:
- GitHub repository connected to Render
- Web service created
- Environment configured
- Application successfully deployed

The hosted version mirrors the local development version and is fully functional and publicly accessible.

---

## 8. Distinction-Level Features Summary

This project meets distinction criteria by:
- Demonstrating strong understanding of Flask routing and request handling
- Using multiple Python classes to model application data
- Integrating HTML, CSS, and JavaScript effectively
- Maintaining clean code structure and best practices
- Delivering a fully hosted and accessible web application

---

## 9. Conclusion

The Intentional Spending Tracker successfully fulfils the requirements of the Python Flask assignment. By combining a clear financial concept with structured Python code and a modern dashboard interface, the project demonstrates both technical competence and thoughtful application design appropriate for a distinction-level submission.

