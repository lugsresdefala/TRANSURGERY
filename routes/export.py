
from flask import send_file
import json
from datetime import datetime
import csv
import io

def export_patient_data(patient_id, format='json'):
    patient = Patient.query.get_or_404(patient_id)
    data = {
        'personal': {
            'name': patient.full_name,
            'dob': patient.date_of_birth.isoformat(),
            'gender_identity': patient.gender_identity
        },
        'appointments': [{
            'date': apt.date_time.isoformat(),
            'description': apt.description
        } for apt in patient.appointments],
        'documents': [{
            'filename': doc.filename,
            'upload_date': doc.upload_date.isoformat()
        } for doc in patient.documents]
    }
    
    if format == 'json':
        return json.dumps(data, indent=2)
    elif format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        # Write CSV data
        return output.getvalue()
