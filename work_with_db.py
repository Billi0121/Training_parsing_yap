import pprint
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, declared_attr
 
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.upper()
    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=Base)

class Practice_Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20)) 

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session(engine)   



    # results = session.query(Pep).filter(Pep.pep_number >= 20).delete()
    # session.delete(results)
    # session.commit()

    # session.query(Pep).update(
    #     {'status': 'Waiting'}
    # )
    # session.commit()
    # results = session.query(Pep).filter(Pep.pep_number == 21).first()
    # results.status = 'Active'
    # session.commit()
    # print(results.all())

    # results = session.query(Pep.name, Pep.status, Pep.pep_number).first()
    # pprint.pprint(results)
    
    from sqlalchemy import insert, select, update, delete 

    # session.query(Practice_Pep).filter(Practice_Pep.status == 'Rejected').delete()
    # session.commit()


    
    session.execute(
        insert(Practice_Pep).values(
            name = 'Hey',
            status = 'Active',
            pep_number = 355
        )
    )
    session.commit()
  

    # status = session.query(Practice_Pep).filter(Practice_Pep.status  == 'Final').filter(Practice_Pep.pep_number <= 3311).count()
    # print(status)

    # status = session.query(Practice_Pep).filter(Practice_Pep.status  == 'Final').count()
    # print(status)
    # session.execute(
    #     insert(Practice_Pep).values(
    #         pep_number = 332333,
    #         name = 'Bilol',
    #         status = 'Final'
    #     )
    # )
    # session.commit()
    # session.commit()
    # p = session.execute(
    #     select(Post).where(
    #         Post.text == 'Hello World'
    #     )
    # ).first()
    # # session.commit()
    # print(p)