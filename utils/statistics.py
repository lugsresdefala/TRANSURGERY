
from models import Surgery, Patient, HormoneRecord
from sqlalchemy import func
import pandas as pd

class Statistics:
    @staticmethod
    def generate_full_report():
        stats = {
            'surgeries': Statistics.surgery_stats(),
            'patients': Statistics.patient_stats(),
            'hormones': Statistics.hormone_stats(),
            'waiting_times': Statistics.waiting_time_stats()
        }
        return stats
