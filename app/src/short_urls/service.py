from threading import Thread
from app.src.short_urls.tasks import threaded_task
import datetime

from app.src import db
from app.src.short_urls.entity import ShortUrls
from app.src.short_urls.converter import Converter

def save_new_shorter(data):
    converter =  Converter()
    shorterObj = ShortUrls.query.filter_by(original_url=data['original_url']).first()
    if not shorterObj:
        shorterObj = ShortUrls(
            original_url=data['original_url'],
            number_access=1,
            created_at = datetime.datetime.utcnow()
        )
        db.session.add(shorterObj)
        db.session.commit()
        db.session.flush()
        db.session.refresh(shorterObj)
        setattr(shorterObj, 'short_url', converter.id_to_shortURL(shorterObj.id))

        thread = Thread(target=threaded_task, args=(shorterObj, ))
        thread.daemon = True
        thread.start()

        db.session.commit()
    return shorterObj

def get_most_frequent_url():
    return ShortUrls.query.order_by(ShortUrls.number_access.desc()).limit(100).all()

def get_a_url(short_url):
    shorterObj = ShortUrls.query.filter_by(short_url=short_url).first()
    shorterObj.number_access += 1
    setattr(shorterObj, 'number_access', shorterObj.number_access + 1)
    db.session.commit()
    db.session.flush()
    return shorterObj
