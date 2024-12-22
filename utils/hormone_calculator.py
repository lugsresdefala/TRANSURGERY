
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class HormoneCalculator:
    @staticmethod
    def calculate_elimination_rate(peak_concentration: float, basal_concentration: float, interval: int) -> float:
        return -math.log(basal_concentration/peak_concentration) / interval
    
    @staticmethod
    def predict_concentration(time: int, initial_conc: float, ke: float) -> float:
        return initial_conc * math.exp(-ke * time)
        
    @staticmethod
    def calculate_optimal_dose(target_concentration: float, volume_distribution: float, bioavailability: float) -> float:
        return (target_concentration * volume_distribution) / bioavailability
        
    @staticmethod
    def calculate_steady_state(half_life: float, dosing_interval: int) -> int:
        return math.ceil(5 * half_life / dosing_interval) * dosing_interval

