from exts import db

from sqlalchemy import create_engine, exc



class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email= db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    
    
    
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        
    def __repr__(self):
        return f'<Users {self.username} >'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        
        db.session.delete(self)
        db.session.commit()

    def update(self, name, username, email):
       
        self.name = name
        self.username = username
        self.email = email

        db.session.commit()

    

class Albums(db.Model):
    __tablename__ = 'Albums'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    Album_title = db.Column(db.String, nullable=False)
   
    
    
    def __init__(self, user, Album_title):
        self.user_id = user_id
        self.Album_title = Album_title
        
    def __repr__(self):
        return f"<Albums {self.Album_title}"
    
    
    def save(self):
        
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        
        db.session.delete(self)
        db.session.commit()

    def update(self, user_id, Album_title):
       
        self.user_id = user_id
        self.Album_title = Album_title

        db.session.commit()

        
        
        
class Photos(db.Model):
    __tablename__ = 'Photos'
    id = db.Column(db.Integer(), primary_key=True)
    Album_id = db.Column(db.Integer(), nullable=True)
    photo_title = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String(120), nullable=False)
    
    
    def __init__(self,Album_id, photo_title, image_url):
        self.Album_id = Album_id
        self.photo_title = photo_title
        self.image_url = image_url 
    
    def __repr__(self):
        return f'<Photos {photo_title}>'
    
    def save(self):
       
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
       
        db.session.delete(self)
        db.session.commit()

    def update(self, photo_title, image_url):
        self.Album_id = Album_id
        self.photo_title = photo_title
        self.image_url = image_url

        db.session.commit()
        
          
        

    


    
    
    
    
    
    
    