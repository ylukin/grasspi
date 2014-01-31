#! /usr/bin/env python
import sqlite3
import datetime

def grasspi_create_db():
    conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()

    # Create table
    c.execute('''create table grasspidb
    (provider text, date text, time text, current_rain real,total_rain real,
    current_wind_speed real, current_wind_direction text, current_humidity real,
    current_air_oressure real, current shortwave_rad real, current_atm_rad real,
    day_length real, elevation real)''')
    # Save (commit) the changes
    conn.commit()
    c.close()
    print 'db created'

def grasspi_add_db(x):
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    print x 
    c.execute('insert into grasspidb values (?,?,?,?,?,?,?,?,?,?,?,?,?)',x)
    # Save (commit) the changes
    conn.commit()
    # We can also close the cursor if we are done with it
    c.close()
    print 'db saved'
    
def grasspi_print_db():
    conn = sqlite3.connect('grasspi.db')
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT * FROM grasspidb"):
        print row
    c.close()

def grasspi_query_db_on_provider(provider):
    
    provider_entries = []
    conn = sqlite3.connect('grasspi.db')
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT * FROM grasspidb WHERE provider = 'WG'"):
       provider_entries.append(row)
    c.close()
    return provider_entries    

def grasspi_delete_entries(prov):
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    c.execute("SELECT * FROM grasspidb")
    delete_list = c.fetchall()
    #in_time = datetime.datetime.strptime(delete_date,"%Y-%m-%d") 
    #print in_time
    for row in delete_list:
        #rowtime = datetime.datetime.strptime(row[1],"%Y-%m-%d") 
        #print rowtime
        #if (rowtime > in_time):
        c.execute("DELETE FROM grasspidb WHERE provider = 'WS'")
    conn.commit()
    c.close()


entries_based_on_provider = []
grasspi_create_db()
row = ['WS','2014-07-30','4:00 AM',0,0,0,'NE',0,0,0,0,0,0]
grasspi_add_db(row)
grasspi_print_db()
entries_based_on_provider = grasspi_query_db_on_provider('WG')
grasspi_delete_entries('WS')
for i in range (0,len(entries_based_on_provider)):
    print entries_based_on_provider[i]
