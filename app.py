import sqlalchemy
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func, inspect, Date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import sem
from flask import (
	Flask,
	render_template,
	jsonify,
	request,
	redirect)
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///US_Businessess.sqlite"

Base = declarative_base()
class Businesspatterns(Base):
    __tablename__ = "businesspatterns"
    
    id = Column(Integer, primary_key=True)
    ESTAB = Column(Integer)
    NAICS2012 = Column(String)
    ZIPCODE = Column(String) 
    NAICS2012_TTL = Column(String)


engine = create_engine("sqlite:///US_Businesses.sqlite")
Base.metadata.create_all(engine)

#def populate_table (engine, table, csvfile):
    #conn = engine.connect()
    
    
    
    #df_insert = pd.read_csv(csvfile)
    
    #data = df_insert.to_dict(orient='records')
    #conn.execute(table.insert(), data)
#populate_table(engine, Businesspatterns.__table__,'census_data.csv')

@app.route("/BusinessPatterns")
def results():
    return jsonify(engine.execute("SELECT * FROM businesspatterns WHERE ZIPCODE =10001").fetchall())

if __name__ == '__main__':
	app.run()
