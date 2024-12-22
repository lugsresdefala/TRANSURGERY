from models import Document, db
from datetime import datetime

ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'gif'} # Added ALLOWED_EXTENSIONS

def validate_file(file):
    if not file:
        return False
    if not '.' in file.filename:
        return False
    ext = file.filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False
    if file.content_length > 16 * 1024 * 1024:  # 16MB limit
        return False
    return True

def create_document_version(document_id, file_path, user_id):
    original = Document.query.get(document_id)
    if not original:
        return None
        
    new_version = Document(
        patient_id=original.patient_id,
        filename=original.filename,
        file_path=file_path,
        version=original.version + 1,
        created_by=user_id,
        created_at=datetime.utcnow()
    )
    
    db.session.add(new_version)
    db.session.commit()
    return new_version