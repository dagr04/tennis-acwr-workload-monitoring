import numpy as np
import pandas as pd

class WorkloadGenerator:
    def __init__(self, player_name, start_date, days):
        self.player = player_name
        self.dates = pd.date_range(start = start_date, periods = days)
        self.rest_day = False
        self.rows = []

    def generate_day(self):
        if self.rest_day:
            practice_h = gym_h = match_h = 0
            intensity = 1
            workload = 0
            self.rest_day = False
    
        else:
            practice_h = np.random.randint(0, 3)
            gym_h = np.random.randint(0, 3)
    
            if practice_h <= 1 and gym_h <= 1:
                match_h = np.random.randint(2, 4)
            else:
                match_h = 0
    
            total_h = practice_h + gym_h + match_h
    
            if total_h > 0:
                intensity = np.random.randint(4, 10)
            else:
                intensity = np.random.randint(1, 3)
    
            workload = total_h * intensity
    
            if match_h > 0:
                self.rest_day = True
    
        return practice_h, gym_h, match_h, intensity, workload


    def run(self):
        for date in self.dates:
            practice_h, gym_h, match_h, intensity, workload = self.generate_day()

            self.rows.append({
                "Player": self.player,
                "Date": date,
                "Practice": practice_h,
                "Gym": gym_h,
                "Match": match_h,
                "Intensity": intensity,
                "Workload": workload
            })
            
        df = pd.DataFrame(self.rows)
        
        Acute = df['Workload'].rolling(window = 7, min_periods = 1).mean()
        Chronic = df['Workload'].rolling(window = 28, min_periods = 1).mean()
        df['ACWR'] = Acute / Chronic

        return df