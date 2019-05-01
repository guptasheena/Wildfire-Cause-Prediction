import pandas as pd
import numpy as np
import sqlite3

class read_sql:
    def read_data():

        conn = sqlite3.connect('../data/FPA_FOD_20170508.sqlite')
        df = pd.read_sql("SELECT * from Fires",con=conn)
        firedata = df.filter(['SOURCE_REPORTING_UNIT_NAME','STATE','LATITUDE','LONGITUDE','FIRE_SIZE','FIRE_SIZE_CLASS','FIRE_YEAR','DISCOVERY_DATE','STAT_CAUSE_DESCR','CONT_DATE','CONT_DOY','CONT_TIME','OWNER_CODE','COUNTY'],axis=1)
        return firedata