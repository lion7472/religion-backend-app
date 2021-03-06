from application.extensions import db, ma


class Video(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String(64), nullable=True)
    text = db.Column(db.String(512), nullable=True)
    video_url = db.Column(db.String(256), nullable=False)
    thumbnaiUrl = db.Column(db.String(256), nullable=True)
    

class VideoSchema(ma.ModelSchema):
    class Meta:
        model = Video
