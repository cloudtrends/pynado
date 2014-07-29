

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
class Base(object):
    """Define the base conventions for all tables/classes."""
    @declared_attr
    def __tablename__(cls):
        """Table is named after the class name"""
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
    """Surrogate primary key column named 'id'"""

Base = declarative_base(cls=Base)



def fk(tablename, nullable=False):
    """Define a convention for all foreign key columns. 
    Just give it the table name."""
    return Column("%s_id" % tablename, Integer, ForeignKey("%s.id" % tablename), nullable=nullable)



class AddressPrototype(object):
    """Lots of objects will have an 'address'. Let's build a prototype for it.'"""

    street = Column(String(50))
    city = Column(String(50))
    state = Column(CHAR(2))
    zip = Column(String(15))


class HasAddresses(object):
    """Define classes that have a collection of addresses via the AddressPrototype foundation."""
    @declared_attr
    def addresses(cls):
        cls.Address = type("%sAddress" % cls.__name__, (AddressPrototype, Base), {'%s_id' % cls.__tablename__:fk(cls.__tablename__)})
        return relationship(cls.Address, backref=cls.__name__.lower(), cascade="all, delete-orphan")







