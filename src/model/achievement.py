from sqlalchemy import Column, Integer, String, Date, ForeignKey
from modules.database import Base

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(Text)
    creation_date = Column(DateTime, server_default=text('current_timestamp'))
    image_url = Column(String(256))

    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

    def __repr__(self):
        return '<Achievement %r %r>' % (
            self.title,
            self.description,
            self.creation_date
        )

