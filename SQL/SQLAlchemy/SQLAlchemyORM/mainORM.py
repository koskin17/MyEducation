import sqlalchemy
from sqlalchemy import create_engine, Unicode, Column, Integer, ForeignKey, UnicodeText, MetaData
from sqlalchemy.orm import sessionmaker, relationship

DB = create_engine('sqlite:///library2.db', echo=True)
metadata = MetaData()
Session = sessionmaker(autoflush=False, bind=DB) # при значение autoflush = True (он по умолчанию)
                                                    # все значения записываются в базу данных
Base = sqlalchemy.orm.declarative_base()


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255))
    code = Column(Unicode(255))
    data = relationship("Data", back_populates="country")

class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Unicode(255), primary_key=True)
    name = Column(Unicode(255))
    data = relationship("Data", back_populates="indicator")

class Data(Base):
    __tablename__ = 'data'
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
    indicator_id = Column(Unicode(255), ForeignKey('indicators.id'), primary_key=True)
    data = Column(UnicodeText)
    country = relationship("Country", back_populates="data")
    indicator = relationship("Indicator", back_populates="data")


Base.metadata.create_all(bind=DB)

# session1 = Session()
# new_country = Country(name="Zulu", code="ZU")
# session.add(new_country)
# session.commit()

# Добавление сразу несколько записей в базу данных
# session2 = Session()
# with session2 as DB:
#     country1 = Country(name="Canada1", code="CAN1")
#     country2 = Country(name="Canada2", code="CAN2")
#     country3 = Country(name="Canada3", code="CAN3")
#     DB.add_all([country1, country2, country3])
#     DB.commit()

# Получение из базы данных всех записей
# session3 = Session()
# with session3 as DB:
#     countries = DB.query(Country).all()
#     for country in countries:
#         print(f"{country.id}.{country.name}.{country.code}")
#     DB.commit()

# Обновление записей в базе данных
# Для обновления объекта достаточно изменить значения его атрибутов и затем
# вызвать у объекта Session метод commit() для применения изменений
# update_country = "New Zealand"
# session4 = Session()
# with session4 as DB:
#     DB.query(Country).filter_by(id=1).first().name = update_country
#     DB.commit()

# Удаление записей
# session5 = Session()
# with session5 as DB:
#     erase = DB.query(Country).filter_by(id=7).first()
#     DB.delete(erase)
#     DB.commit()

