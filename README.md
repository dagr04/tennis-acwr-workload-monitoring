# Tennis Training Load Monitoring Using ACWR

## Overview
This project applies sports analytics principles to monitor and manage training load in collegiate tennis athletes. Using the **Acute-to-Chronic Workload Ratio (ACWR)**, the system identifies workload spikes that may increase injury risk and provides recomendations for the coaching staff.

## The Problem 
High training volumes in college tennis often lead to fatigue-related injuries. Coaches frequently rely on intuition rather than objective workload data when adjusting training intensity.

## The Analysis
The system calculates:
- **Daily Workload:** Calculated as the sum of Practice, Gym, and Match hours multiplied by session intensity.
- **Acute Load (Fatigue):** A 7-day rolling average of daily workload.
- **Chronic Load (Fitness):** A 28-day rolling average of daily workload.
- **ACWR** = $\frac{\text{Acute Load}}{\text{Chronic Load}}$.
 
## The Solution
- Track ACWR trends over time for each athlete
- Provide actionable workload recommendations (reduce, maintain, or increase load)

## Features
- **Automated Scheduling:** The generator simulates realistic tennis schedules, including automatic rest days following match play.
- **Visual Tracking:** Generates a plot for each player showing their ACWR trend against the "Optimal Zone" (0.8 - 1.3). And creates a team-wide summary table for quick decision-making.


## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

## How to Run
```bash
pip install -r requirements.txt
python3 dashboard.py
