document.addEventListener('DOMContentLoaded', function() {
    
    // Handle Delete
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.transaction-card');
            const expenseId = card.dataset.id;
            
            if(confirm('Are you sure you want to delete this expense?')) {
                fetch(`/delete-expense/${expenseId}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        card.remove();
                        // Optional: Reload to update totals or update DOM manually
                        location.reload(); 
                    } else {
                        alert('Error deleting expense');
                    }
                });
            }
        });
    });

    // Handle Edit
    document.querySelectorAll('.btn-edit').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.transaction-card');
            const expenseId = card.dataset.id;
            const detailsDiv = card.querySelector('.transaction-details');
            const titleEl = detailsDiv.querySelector('.transaction-title');
            const amountEl = detailsDiv.querySelector('.transaction-amount');
            
            // Check if already in edit mode
            if (this.textContent === 'Save') {
                const newDesc = titleEl.querySelector('input').value;
                const newAmount = amountEl.querySelector('input').value; // Basic validation needed

                fetch(`/update-expense/${expenseId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        description: newDesc,
                        amount: newAmount
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        titleEl.textContent = newDesc;
                        amountEl.textContent = '$' + parseFloat(newAmount).toFixed(2);
                        this.textContent = 'Edit';
                        // Optional: Reload to update totals
                         location.reload();
                    } else {
                        alert('Error updating expense');
                    }
                });

            } else {
                // Switch to edit mode
                const currentTitle = titleEl.textContent;
                const currentAmount = amountEl.textContent.replace('$', '').trim();

                titleEl.innerHTML = `<input type="text" value="${currentTitle}" class="edit-input-title">`;
                amountEl.innerHTML = `<input type="number" step="0.01" value="${currentAmount}" class="edit-input-amount">`;
                
                this.textContent = 'Save';
            }
        });
    });
});
