
from flask import Blueprint, render_template, request, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from models import Surgery, User, Document
from app import db
from datetime import datetime

surgeries = Blueprint('surgeries', __name__)

SURGERY_TYPES = {
    'mamoplastia_masc': 'Mamoplastia masculinizadora',
    'neocolpo': 'Neocolpovulvovaginoplastia', 
    'histerectomia': 'Histerectomia',
    'metoido': 'Metoidoplastia',
    'tireo': 'Tireoplastia',
    'mamoplastia_prot': 'Mamoplastia com prótese',
    'neofalo': 'Neofaloplastia'
}

@surgeries.route('/surgeries/<type>', methods=['GET', 'POST'])
@login_required
def manage_surgery(type):
    if type not in SURGERY_TYPES:
        abort(404)
        
    if request.method == 'POST':
        surgery = Surgery(
            type=type,
            user_id=current_user.id,
            surgeon_id=request.form.get('surgeon_id'),
            scheduled_date=datetime.strptime(request.form.get('date'), '%Y-%m-%d'),
            notes=request.form.get('notes')
        )
        db.session.add(surgery)
        db.session.commit()
        flash('Cirurgia registrada com sucesso!', 'success')
        return redirect(url_for('dashboard'))
        
    surgeons = User.query.filter_by(role='surgeon').all()
    return render_template('surgery/request.html', 
                         surgery_type=SURGERY_TYPES[type],
                         surgeons=surgeons)

@surgeries.route('/surgeries/list')
@login_required
def list_surgeries():
    if current_user.role == 'surgeon':
        surgeries = Surgery.query.filter_by(surgeon_id=current_user.id).all()
    else:
        surgeries = Surgery.query.filter_by(user_id=current_user.id).all()
    return render_template('surgery/list.html', surgeries=surgeries)
