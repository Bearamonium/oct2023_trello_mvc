from init import db, ma
from marshmallow_sqlalchemy import fields

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date the card was created
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='cards')

class CardSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ['name', 'email'])

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user')
        ordered = True

card_schema = CardSchema()
cards_schema = CardSchema(many=True)