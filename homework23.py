import sqlite3
from sqlite3 import Error
import os
import json

database = os.path.join(os.getcwd(), "film.db")
try:
	conn = sqlite3.connect(database)
except Error as e:
	print(e)

curs = conn.cursor()


#Title starts with "B"
# curs.execute("SELECT {} FROM {} WHERE {} like 'B%'". format("title", "film","title"))
# a = curs.fetchall()
# print(a)

# #Film with the largest duration

# curs.execute("SELECT {} FROM {} ORDER BY {} DESC". format("title", "film", "length"))
# a = curs.fetchall()
# print(a[0])

# #write into JSON

# curs.execute("SELECT * from {}".format("film"))
# a = curs.fetchall()
# with open("new_json.json", "w") as jsonfile:
# 	json.dump(a, jsonfile)

# #Create a new table
curs.execute("SELECT * FROM {} WHERE {} > 2010 AND {} BETWEEN 3 AND 5".format("film", "release_year", "rate"))
a = curs.fetchall()

new_query = """ CREATE TABLE IF NOT EXISTS filtered_film (
                                        film_id PRIMARY KEY,
                                        title NOT NULL,
                                        description text,
                                        release_year text,
                                        rate int,
                                        length int,
                                        special_features text
                                    ); """


curs.execute(new_query)
conn.commit()

insert_query = """INSERT INTO filtered_film(film_id, title, description, release_year, rate, length, special_features)
                    VALUES(a,a,a,a,a,a,a)
                    """

curs.execute(insert_query)
conn.commit()

