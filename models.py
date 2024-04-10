from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_INSIGHT_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/2001_Honda_Insight_Hybrid_1.0i_%28Interior%29.jpg/800px-2001_Honda_Insight_Hybrid_1.0i_%28Interior%29.jpg?20220806212143'

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Listing(db.Model):
    """Honda Insight Listing"""

    __tablename__ = "listings"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
        )

    date = db.Column(
        db.DateTime,
        nullable=False
    )

    title = db.Column(
        db.String(1000),
        nullable=False
    )

    price = db.Column(
        db.Integer,
        nullable=False,
    )

    city = db.Column(
        db.String(500),
        nullable=False
    )

    state = db.Column(
        db.String(20),
        nullable=False
    )

    mileage = db.Column(
        db.Integer,
        nullable=False
    )

    url = db.Column(
        db.String(1000),
        default=False
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_INSIGHT_URL
    )

    insight = db.Column(
        db.Boolean,
        nullable=False
    )

    first_gen = db.Column(
        db.Boolean,
        nullable=False
    )

    parts = db.Column(
        db.Boolean,
        nullable=False
    )

    site = db.Column(
        db.String(15),
        nullable=False
    )
    year = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    def serialize(self):
        """Serialize to dictionary"""

        return {
            "id": self.id,
            "date": self.date,
            "title": self.title,
            "price": self.price,
            "city": self.city,
            "state": self.state,
            "mileage": self.mileage,
            "url": self.url,
            "image": self.image,
            "insight": self.insight,
            "first_gen": self.first_gen,
            "parts": self.parts,
            "site": self.site,
            "year": self.year
        }




