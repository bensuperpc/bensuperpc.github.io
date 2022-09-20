from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import IdMixin, TimedMixin, db


class User(TimedMixin, IdMixin, UserMixin, db.Model):
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(256))
    picture_url = db.Column(
        db.Text,
        default="https://upload.wikimedia.org/wikipedia/commons/8/88/Bensuperpc_cat.jpg",
    )
    admin = db.Column(db.Boolean, default=False)

    comments = db.relationship("Comment", back_populates="user")

    posts = db.relationship("Post", back_populates="user")

    connect = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha512")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def comment_count(self):
        return len(self.comments)

    def post_count(self):
        return len(self.posts)

    def connect_count(self):
        return self.connect

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return f"<User {self.name}>"
