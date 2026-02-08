document.addEventListener('DOMContentLoaded', function() {
    const dataDisplay = document.getElementById('financial-data');
    if (!dataDisplay) return;

    const totalIncome = parseFloat(dataDisplay.getAttribute('data-total-income')) || 0;
    const totalFixed = parseFloat(dataDisplay.getAttribute('data-total-fixed')) || 0;
    const totalFun = parseFloat(dataDisplay.getAttribute('data-total-fun')) || 0;
    const totalFuture = parseFloat(dataDisplay.getAttribute('data-total-future')) || 0;

    // Default targets
    const TARGET_FIXED = 50;
    const TARGET_FUN = 30;
    const TARGET_FUTURE = 20;

    function updateChart(totalAmount, targetPercent, barClass, labelClass) {
        let percent = 0;
        if (totalIncome > 0) {
            percent = (totalAmount / totalIncome) * 100;
        }

        // Update Label
        const label = document.querySelector(`.${labelClass}`);
        if(label) {
            // Display decimal only if not a whole number to keep it clean, or 1 decimal fixed
            label.textContent = (percent % 1 === 0 ? percent : percent.toFixed(1)) + '%';
        }

        const bar = document.querySelector(`.${barClass}`);
        if (bar) {
            // Cap visual width at 100% to prevent overflow, but logic uses real percent
            bar.style.width = `${Math.min(percent, 100)}%`;
            
            const targetLine = bar.parentElement.querySelector('.target-line');
            if (targetLine) {
                if (percent > targetPercent) {
                    targetLine.style.backgroundColor = 'red';
                    bar.style.backgroundColor = 'red';
                } else {
                    targetLine.style.backgroundColor = ''; // Reset to default CSS
                    bar.style.backgroundColor = '';
                }
            }
        }
    }

    updateChart(totalFixed, TARGET_FIXED, 'bar-fixed', 'percent-fixed');
    updateChart(totalFun, TARGET_FUN, 'bar-fun', 'percent-fun');
    updateChart(totalFuture, TARGET_FUTURE, 'bar-future', 'percent-future');
});
