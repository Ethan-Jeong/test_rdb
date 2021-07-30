# from bs4 import BeautifulSoup
# import requests
#
# res = requests.get('http://media.daum.net/economic/')
#
# import sqlite3
# if res.status_code == 200:
#     soup = BeautifulSoup(res.content, 'html.parser')
#     links = soup.select('a.link_txt')
#     # with sqlite3.connect('./db.sqlite3') as conn
#     connect = sqlite3.connect('../db.sqlite3')
#     cursor = connect.cursor()
#
#     for link in links:
#         title = str.strip(link.get_text())
#         href = str.strip(link.get('href'))
#         try:
#             cursor.execute(
#                 "insert into polls_economics(create_date, href, title) values(datetime('now'), ?, ?)", (href,title))
#             print(title, ' : ', href)
#         except:
#             pass
#
#     connect.commit()

import sqlite3

connect = sqlite3.connect('../db.sqlite3')

import pandas as pd

df_mask = pd.read_sql_query('select * from polls_economics where title like "%마스크%" ', connect)
df_work = pd.read_sql_query('select * from polls_economics where title like "%노동%" ', connect)
df_gain = pd.read_sql_query('select * from polls_economics where title like "%소득%" ', connect)

print(df_mask.info())
print(df_work.info())
print(df_gain.info())

df_mask.to_sql('mask_table' , connect , if_exists='replace' )
df_work.to_sql('work_table' , connect , if_exists='replace' )
df_gain.to_sql('gain_table' , connect , if_exists='replace' )


connect.close()