function createChart(type='pie', data=[], labels=[],
                        backgroundColor=[], borderColor=[]){
    const ctx = document.getElementById('chart').getContext('2d');
     new Chart(ctx, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        label: '# of Votes',
                        data: data,
                        backgroundColor: backgroundColor,
                        borderColor: borderColor,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
}
