import cherrypy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from mako.template import Template


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    sno = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    desc = Column(String(500), nullable=False)
    date_created = Column(String, default=datetime.utcnow)


engine = create_engine('sqlite:///database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class MyApp:
    
    @cherrypy.expose
    def index(self, title=None, desc=None):
        if title and desc:
            user = User(title=title, desc=desc)
            session.add(user)
            session.commit()

        alluser = session.query(User).all()
        user_list = [f"{user.sno} {user.title} {user.desc} {user.date_created}" for user in alluser]
        index_tmpl = Template(filename='templates/test.html')
        return index_tmpl.render(users=user_list)
    
    @cherrypy.expose
    def update(self, sno):
        title = input("Enter Updated title:")
        desc = input("Enter Updated description:")
        user = session.query(User).filter_by(sno=sno).first()
        user.title = title
        user.desc = desc
        session.add(user)
        session.commit()

        alluser = session.query(User).all()
        user_list = [f"{user.sno} {user.title} {user.desc} {user.date_created}" for user in alluser]
        return "Users: {}".format(",".join(user_list))

    @cherrypy.expose
    def delete(self, sno):
        user = session.query(User).filter_by(sno=sno).first()
        session.delete(user)
        session.commit()

        alluser = session.query(User).all()
        user_list = [f"{user.sno} {user.title} {user.desc} {user.date_created}" for user in alluser]
        return "Users: {}".format(",".join(user_list))


if __name__ == "__main__":
    cherrypy.quickstart(MyApp())
