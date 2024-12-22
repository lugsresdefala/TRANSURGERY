
import os
import shutil
from datetime import datetime
import sqlite3
import logging

def create_backup():
    try:
        # Backup do banco de dados
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = 'backups/' + timestamp
        
        if not os.path.exists('backups'):
            os.makedirs('backups')
            
        os.makedirs(backup_dir)
        
        # Backup do banco SQLite
        shutil.copy2('instance/sgpt.db', f'{backup_dir}/sgpt.db')
        
        # Backup dos uploads
        if os.path.exists('uploads'):
            shutil.copytree('uploads', f'{backup_dir}/uploads')
            
        logging.info(f'Backup created successfully at {backup_dir}')
        return True
    except Exception as e:
        logging.error(f'Backup failed: {str(e)}')
        return False
