import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3.db')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
        cursor.execute(queries.CREATE_TABLE_product_details)
        cursor.execute(queries.CREATE_TABLE_collection_products)


async def sql_insert_store_to_product_details(productid, category, infoproduct):
    cursor.execute(
        queries.INSERT_product_details,
        (productid, category, infoproduct)
    )
    db.commit()

async def sql_insert_store_to_collection_products(productid, collection):
    cursor.execute(
        queries.INSERT_collection_products,
        (productid, collection)
    )
    db.commit()


