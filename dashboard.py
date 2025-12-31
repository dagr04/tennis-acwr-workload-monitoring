import pandas as pd
from workload_generator import WorkloadGenerator
import matplotlib.pyplot as plt

players = ['Alex', 'Jordan', 'Sam', 'Taylor', 'Casey']
team_summary = []

for player in players:

    gen = WorkloadGenerator(player, "2024-01-01", 90)
    data = gen.run()
    
    ratio = data.iloc[-1]['ACWR']
  
    if ratio > 1.5:
        status = 'High Risk'
        rec = 'Reduce Volume'
    elif ratio < 0.80:
        status = 'Detraining'
        rec = 'Increase Load'
    elif 0.80 <= ratio <= 1.30:
        status = 'Optimal'
        rec = 'Maintain'
    else:
        status = 'Caution' 
        rec = 'Monitor'

    team_summary.append({
        'Player': player,
        'ACWR': round(ratio, 2),
        'Status': status,
        'Recommendation': rec
    })

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['ACWR'], label='ACWR')
    plt.axhspan(0.8, 1.3, color='green', alpha=0.1, label='Optimal')
    plt.axhline(y=1.5, color='red', linewidth=1, linestyle='--', label='High Risk')
    plt.title(f'ACWR Over Time — {player}')
    plt.xlabel('Date')
    plt.ylabel('ACWR')
    plt.legend()
    plt.show()

dashboard_df = pd.DataFrame(team_summary)
print(dashboard_df)
