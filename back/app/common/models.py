from marshmallow import Schema

from .extensions import ext

db = ext['db']

class Notes(db.Model):

    id = db.Column(
        db.Integer(), primary_key=True, autoincrement=True, nullable=False
    )
    text = db.Column(db.Text(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False)

    def __init__(self, text, completed):
        self.text = text
        self.completed = completed

    def __repr__(self):
        template = "<Notes {}:{}:{}>"
        return template.format(self.id, self.completed, self.text[:8])

class NotesSchema(Schema):

    class Meta:
        fields = ('id', 'text', 'completed')
