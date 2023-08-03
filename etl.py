import pandas as pd
import configparser
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

# Setup logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

# Read the configuration file

config = configparser.ConfigParser()

config.read('config.ini')

# Database configuration

db_config = config['database']

engine = create_engine(
    f"mysql+mysqldb://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

Base = declarative_base()


# Define the Department and Employee classes

class Department(Base):
    __tablename__ = 'department'

    dept_id = Column(Integer, primary_key=True)

    dept_name = Column(String(50))


class Employee(Base):
    __tablename__ = 'employee'

    emp_id = Column(Integer, primary_key=True)

    name = Column(String(100))

    dept_id = Column(Integer, ForeignKey("department.dept_id"))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

try:

    # Load your CSV/JSON data into pandas DataFrame

    df_dept = pd.read_csv('departments.csv')

    df_emp = pd.read_csv('employees.csv')

    # Merge the first name and last name into name

    df_emp['name'] = df_emp['first_name'] + ' ' + df_emp['last_name']

    # Insert department data into MySQL/Postgres table

    for index, row in df_dept.iterrows():
        dept = Department(dept_id=row['dept_id'], dept_name=row['dept_name'])

        session.merge(dept)

    session.commit()

    # Insert employee data into MySQL/Postgres table

    for index, row in df_emp.iterrows():
        emp = Employee(emp_id=row['emp_id'], name=row['name'], dept_id=row['dept_id'])

        session.merge(emp)

    session.commit()

except Exception as e:

    logger.warning(f"An error occurred: {e}")

    session.rollback()

finally:

    session.close()

