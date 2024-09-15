from sqlalchemy import create_engine, MetaData, Table, Column, insert, Select, update, delete
from sqlalchemy.types import Integer, Unicode, UnicodeText
from sqlalchemy.schema import ForeignKey

from Softserve.lesson08.my_regex import result

engine = create_engine(r"sqlite:///main.db", echo=True)

metadata = MetaData()
countries_table = Table("countries",
                metadata,
                Column('id', Integer, primary_key=True),
                Column('name', Unicode(255)),
                Column('code', Unicode(255)))
indicators_table = Table("indicators",
                metadata,
                Column('id', Unicode(255), primary_key=True),
                Column('name', Unicode(255)))
data_table = Table("data",
                metadata,
                Column('country_id', ForeignKey("countries.id")),
                Column('indicator', ForeignKey("indicators.id")),
                Column('data', UnicodeText))

# metadata.create_all(engine)

# conn = engine.connect()
# new_country = {'name': 'Canada', 'code': 'CAN'}
# country = insert(countries_table).values(new_country)
# conn.execute(country)
# conn.commit()

# conn = engine.connect()
# query = Select(countries_table)
# country = conn.execute(query)
# conn.commit()
#
# for row in country:
#     print(row)

# conn = engine.connect()
# update_country = {"name": "Canada_update", "code": "CAN_UPDATE"}
# conn.execute(update(countries_table).where(countries_table.c.id == 1).values(update_country))
# conn.commit()

# conn = engine.connect()
# delete_stmt = delete(countries_table).where(countries_table.c.id == 1)
# conn.execute(delete_stmt)
# conn.commit()