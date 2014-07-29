# -*- coding: UTF-8 -*-
from sqlalchemy import *
#import sqlalchemy.util as util
import string, sys
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey 
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey 
#from sqlalchemy import create_engine 
#from sqlalchemy.orm import sessionmaker 
#from sqlalchemy.orm import scoped_session 

#from sqlalchemy.databases import mysql
# step 1. imports
#from sqlalchemy import (create_engine, MetaData, Table, Column, Integer,
#    String, ForeignKey, Float, DateTime, event)
#from sqlalchemy.orm import sessionmaker, mapper, relationship

from sqlalchemy.engine import create_engine
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)



Base = declarative_base()
#http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

class Users(Base):
    __tablename__ = "t_users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)




#
mysql_engine = create_engine('mysql://root:password@localhost:3306/gobbs?charset=utf8',encoding = "utf-8",echo =True)
#mysql_engine = create_engine('mysql+mysqlconnector://root:password@172.16.206.169:3306/gobbs?charset=utf8',encoding = "utf-8",echo =True)   
#mysql_engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')
#mysql_engine = create_engine('mysql+oursql://scott:tiger@localhost/foo')



#mysql_engine.connect()    
metadata = MetaData()

#mysql_engine='InnoDB' 或者 mysql_engine='MyISAM' 表类型
#metadata.create_all(mysql_engine)

#conn = mysql_engine.connection()  #得到连接对象

#mysql_engine.raw_connection()


Base.metadata.bind = mysql_engine
DBSession = sessionmaker(bind=mysql_engine)

session = DBSession()

#http://www.linuxjournal.com/content/sqlalchemy
person = session.query(Users).first()


#print person.user_name


all_persons = session.query(Users).all()
for p in all_persons:
    print( p.user_name)

#for p in session.query(Person).filter_by(id=1):
#    print( p.first_name)

#def print():


class SqlAlchemyTest():
    @staticmethod
    def helloworld():
        print( "helloworld")