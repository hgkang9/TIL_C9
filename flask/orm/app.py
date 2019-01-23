from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__) #플라스크 서버 위한 기본 설정

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlalchemy 초기화
db = SQLAlchemy(app)

#migrate 초기화
migrate = Migrate(app, db)

#table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
#명령어
#flask db init
#flask db migrate
#flask db upgrade

#정리
#[Create]
#INSERT INTO users(username, email) VALUES('hg', '@gmail.com')
#user = User(username='hg', email='@gmail.com')
#db.session.add(user)
#db.session.commit()

#[Read]
#SELECT * FROM users;
#users = User.query.all() -> 결과가 복수

#SELECT * FROM users WHERE username='hg';
#users = User.query.filter_by(username='hg').all()

#SELECT * FROM users WHERE username='hg'LIMIT 1;
#user = User.query.filter_by(username='hg').first()

#SELECT * FROM users WHERE id=2 LIMIT 1;
#user = User.query.get(2)
#primary key만 get으로 가져올 수 있음

#SELECT * FROM users WHERE email LIKE '%ex%';
#users = User.query.filter(User.email.like("%ex%")).all()

#ORDER(정렬)
#users = User.query.order_by(User.username).all()

#LIMIT
#users = User.query.limit(1).all()

#OFFSET
#users = User.query.offset(2).all()

#ORDER + LIMIT + OFFSET
#users = User.query.order_by(User.username).limit(1).offset(2).all()

#DELETE
#DELETE FROM users WHERE id=1;
#user = User.query.get(1)
#db.session.delete(user)
#db.session.commit()

#UPDATE
#UPDATE users SET username='abc' WHERE id=2;
#user = User.query.get(2)
#user.username = 'abc'
#db.session.commit()

#ALTER TABLE bands ADD COLUMN members INT;
#열을 추가하고 싶을 때