from app import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
