from .. import db
from datetime import datetime

class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), nullable=True)
    short_url = db.Column(db.String(20), nullable=True, unique=True)
    page_title = db.Column(db.String(200), nullable=True, unique=False)
    number_access = db.Column(db.Integer, nullable=False, unique=False)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)