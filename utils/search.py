
from sqlalchemy import or_

def advanced_search(query_string, filters=None):
    search = f"%{query_string}%"
    base_query = Patient.query
    
    if filters:
        if filters.get('age_min'):
            base_query = base_query.filter(Patient.date_of_birth <= filters['age_min'])
        if filters.get('gender_identity'):
            base_query = base_query.filter(Patient.gender_identity == filters['gender_identity'])
            
    return base_query.filter(or_(
        Patient.full_name.ilike(search),
        Patient.gender_identity.ilike(search),
        Document.ocr_content.ilike(search)
    )).join(Document, isouter=True).all()
