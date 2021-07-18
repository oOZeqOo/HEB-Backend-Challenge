from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app import get_session, get_engine

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)

    def __repr__(self):
        return "<User(id='%s', first_name='%s', last_name='%s', email='%s', address='%s', city='%s', state='%s', zipcode='%s')>" % (
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.address,
            self.city,
            self.state,
            self.zipcode,
        )

    def __str__(self):
        string = f"Id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zipcode}"
        return string

    @classmethod
    def query(cls):
        return get_session().query(cls)

    @classmethod
    def create_customer(cls, customer):
        session = get_session()
        new_customer = cls(**customer)
        session.add(new_customer)
        session.commit()

    @classmethod
    def get_by_city(cls, city):
        customers = cls.query().filter(cls.city == city).all()
        if len(customers) < 1:
            return None
        return customers

    @classmethod
    def get_by_id(cls, id):
        customer = cls.query().filter(cls.id == id).one_or_none()
        return customer

    @classmethod
    def get_all(cls):
        customers = cls.query().all()
        return customers

    def get_json(self):
        return {
            "id": self.id,
            "firt_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
        }


Base.metadata.create_all(get_engine())
