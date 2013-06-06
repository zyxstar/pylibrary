#coding:utf-8

import fn_db
import fn_ref

def get_bookins_join(bookinsid):
    query = fn_db.db.query("""
        SELECT a.*, b.*
            FROM LIM_BOOKINS a LEFT JOIN LIM_BOOKCLS b ON a.bookclsid = b.bookclsid
           WHERE a.bookinsid = $bookinsid
        """, vars = locals())
    for item in query:
        return item
    return None

def bind_ref(book):
    fn_ref.bind(book,
               inssts = "BOOKINSSTS",
               catcd = "CAT",
               placecd = "PLACE",
               pubcd = "PUB")


