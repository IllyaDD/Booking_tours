from app import db


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True),
    name = db.Column(db.String(100), nullable=False),
    description = db.Column(db.String(500), nullable=False),
    price = db.Column(db.Float, nullable=False)
    # duration = db.Column(db.Integer, nullable=False),
    # image_url = db.Column(db.String(200), nullable=False),


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True),
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False),
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False),
    date_booked = db.Column(db.Date, nullable=False),
    quantity = db.Column(db.Integer, nullable=False),
    email = db.Column(db.String(255), nullable=False)
