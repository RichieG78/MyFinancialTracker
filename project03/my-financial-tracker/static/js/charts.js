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

    function updateChart(totalAmount, targetPercent, barClass) {
        let percent = 0;
        if (totalIncome > 0) {
            percent = (totalAmount / totalIncome) * 100;
        }

        const bar = document.querySelector(`.${barClass}`);
        if (bar) {
            // Cap visual width at 100% to prevent overflow, but logic uses real percent
            bar.style.width = `${Math.min(percent, 100)}%`;
            
            const targetLine = bar.parentElement.querySelector('.target-line');
            if (targetLine) {
                if (percent > targetPercent) {
                    targetLine.style.backgroundColor = 'red';
                    // Optional: Make the bar red too or just the line as requested?
                    // "target line should change colour to red"
                } else {
                    targetLine.style.backgroundColor = ''; // Reset to default CSS
                }
            }
        }
    }

    updateChart(totalFixed, TARGET_FIXED, 'bar-fixed');
    updateChart(totalFun, TARGET_FUN, 'bar-fun');
    updateChart(totalFuture, TARGET_FUTURE, 'bar-future');
});
