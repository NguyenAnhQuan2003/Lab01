import json
import psycopg2
from config import load_config

with open('data.json') as f:
    data = json.load(f)

def insert_data(tiki_list):
    sql = ("INSERT INTO data_tiki(id, name, url_key, price, description, thumbnail_url) VALUES "
           "(%s, %s, %s, %s, %s, %s)"
           "ON CONFLICT (id) DO NOTHING")
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, tiki_list)
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def prepare_tiki_list(data):
    tiki_list = []
    for item in data:
        tiki_list.append((
            item.get("id"),
            item.get("name"),
            item.get("url_key"),
            item.get("price"),
            item.get("description"),
            item.get("thumbnail_url")
        ))
    return tiki_list
if __name__ == '__main__':
    tiki_data = prepare_tiki_list(data)
    insert_data(tiki_data)