
from flask_mail import Message
from app import mail, db
from models import User, Notification
import threading

class NotificationQueue:
    _pending = []
    
    @classmethod
    def add(cls, notification):
        cls._pending.append(notification)
    
    @classmethod
    def get_pending(cls):
        pending = cls._pending[:]
        cls._pending = []
        return pending

class NotificationSystem:
    @staticmethod
    def send_notification(user_id, title, message, notification_type='info'):
        notification = {
            'user_id': user_id,
            'title': title,
            'message': message,
            'type': notification_type
        }
        NotificationQueue.add(notification)
    
    @staticmethod
    def process_notification(notification):
        user = User.query.get(notification['user_id'])
        if user and user.email:
            msg = Message(
                notification['title'],
                recipients=[user.email],
                body=notification['message']
            )
            mail.send(msg)
            
        db_notification = Notification(
            user_id=notification['user_id'],
            title=notification['title'],
            message=notification['message'],
            type=notification['type']
        )
        db.session.add(db_notification)
        db.session.commit()
    
    @staticmethod
    def send_all_notifications():
        notifications = NotificationQueue.get_pending()
        threads = []
        for notif in notifications:
            t = threading.Thread(target=NotificationSystem.process_notification, args=(notif,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
