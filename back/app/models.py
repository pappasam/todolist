from marshmallow import Schema

from .extensions import ext

db = ext['db']

class Notes(db.Model):

    id = db.Column(
        db.Integer(), primary_key=True, autoincrement=True, nullable=False
    )
    content = db.Column(db.Text(), nullable=False)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return "<Notes {} {}>".format(self.id, self.content[:8])

class NotesSchema(Schema):

    class Meta:
        fields = ('id', 'content')
