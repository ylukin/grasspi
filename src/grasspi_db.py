#! /usr/bin/env python
import sqlite3
import datetime

def isSQLite3(filename):
    """ Check if database file already exists and is in valid SQLite3 format """
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return False
    else:
        fd = open(filename, 'rb')
        Header = fd.read(100)
        fd.close()

        if Header[0:16] == 'SQLite format 3\000':
            return True
        else:
            return False

def grasspi_create_db():
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()

    # Create weatherdata table
    c.execute('''create table weatherdata
    (provider text, date text, time text, current_rain real,total_rain real,
    current_wind_speed real, current_wind_direction text, current_humidity real,
    current_air_pressure real, current shortwave_rad real, current_atm_rad real,
    day_length real, elevation real)''')

    # Create wateringschedule table
    c.execute('''create table wateringschedule
    (zonenumber int, date text, time text, length int)''')

    # Save (commit) the changes
    conn.commit()
    c.close()
    print 'db created'

def grasspi_add_db(row, table):
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    c.execute('insert into ' + table + ' values (?,?,?,?,?,?,?,?,?,?,?,?,?)',[row["provider"],row["date"],row["time"],
    row["current_rain"],row["total_rain"],row["current_wind_speed"],row["current_wind_direction"],row["current_humidity"],
    row["current_air_pressure"],row["current_shortwave_rad"],row["current_atm_rad"],row["day_length"],row["elevation"]])
    # Save (commit) the changes
    conn.commit()
    # We can also close the cursor if we are done with it
    c.close()
    print 'db saved'
    
def grasspi_print_db(table):
    conn = sqlite3.connect('grasspi.db')
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT * FROM " + table):
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

#row = ['WS','2014-07-30','4:00 AM',0,0,0,'NE',0,0,0,0,0,0]
#grasspi_add_db(row)
#grasspi_print_db()
#entries_based_on_provider = grasspi_query_db_on_provider('WG')
#grasspi_delete_entries('WS')
#for i in range (0,len(entries_based_on_provider)):
#    print entries_based_on_provider[i]
