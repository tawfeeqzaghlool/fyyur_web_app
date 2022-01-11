from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable=False)
    website_link = db.Column(db.String(200))
    seeking_description = db.Column(db.String(1000))
    shows = db.relationship('Show', backref='Venue', lazy=True, cascade="save-update, merge, delete")

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __repr__(self) -> str:
        return f"Venue({self.id}, {self.name})"

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable=False)
    website_link = db.Column(db.String(200))
    seeking_description = db.Column(db.String(1000))
    shows = db.relationship('Show', backref='Venue', lazy=True, cascade="save-update, merge, delete")

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __repr__(self):
        return f"Artist({self.id}, {self.name})"

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
#class Show(db.Model):
#    __tablename__ = 'shows'

#    id = db.Column(db.Integer, primary_key=True)
#    start_time = db.Column(db.DateTime(timezone=True)
#    artist = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
#    venue = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

#    def __repr__(self):
#       start_time = self.start_time.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
#       return f"Show({self.id}, {start_time}, {self.artist_id}, {self.venue_id})"
db.create_all()