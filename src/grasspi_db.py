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

def grasspi_create_db(table_name, schema):
    """ Create database file and table given the table schema """

    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    # Create table
    str = "CREATE TABLE if not exists " + table_name + " " + schema
    c.execute(str)
    # Save (commit) the changes
    conn.commit()
    c.close()
    
def grasspi_add_db(table_name,row):
    """ Adds an entry to database given table name and row of values """

    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    if table_name == "weatherdata":
	c.execute('INSERT INTO ' + table_name + ' values (?,?,?,?,?,?,?,?,?,?,?,?,?)',[row["date"],row["time"],
    	row["current_temp"],row["current_rain"],row["total_rain"],row["current_wind_speed"],
    	row["current_wind_direction"],row["current_humidity"],row["current_air_pressure"],
    	row["current_shortwave_rad"],row["current_atm_rad"],row["day_length"],row["elevation"]])
    elif table_name == "wateringschedule":
	c.execute('INSERT INTO ' + table_name + ' values (?,?,?,?)',[row["zonenumber"],row["date"],
	row["time"],row["length"]])
    # Save (commit) the changes
    conn.commit()
    # We can also close the cursor if we are done with it
    c.close()

def grasspi_print_db(table_name):
    """ Print contents of database table """

    conn = sqlite3.connect('grasspi.db')
    conn.text_factory = str
    c = conn.cursor()
    val = "SELECT * FROM " + table_name
    for row in c.execute(val):
        #conn.text_factory = str
        print row
    c.close()

def grasspi_query_db(table_name,query,value):
    """ Query the database given table name, query column and value """

    query_entries = []
    conn = sqlite3.connect('grasspi.db')
    conn.text_factory = str
    c = conn.cursor()
    val = "SELECT * FROM " + table_name + ' WHERE '+ query +' = '+"'" + value +"'"
    for row in c.execute(val):
       query_entries.append(row)
    c.close()
    return query_entries
    
def grasspi_delete_entries(table_name,query,value):
    """ Query database given table name, query column and value and delete entries """

    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    val = "SELECT * FROM " + table_name
    c.execute(val)
    delete_list = c.fetchall()
    
    for row in delete_list:
        str1 = "DELETE FROM " + table_name + ' WHERE '+ query +' = '+"'" + value +"'"
        c.execute(str1)
    conn.commit()
    c.close()
    
def grasspi_delete_db(table_name):
    """ Delete the database """

    sql = 'drop table IF EXISTS ' + table_name
    conn = sqlite3.connect('grasspi.db')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


