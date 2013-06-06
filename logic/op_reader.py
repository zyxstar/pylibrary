#coding:utf-8

import fn_db
import fn_ref

def can_borrow(typborrcat, catcd):
    return catcd in typborrcat.split(',')#should modify

def get_reader_join(readercardno):
    query = fn_db.db.query("""
        SELECT a.*, b.*, c.*
          FROM LIM_READERCARD a LEFT JOIN LIM_READER b ON a.readerid = b.readerid
               LEFT JOIN LIC_READERTYP c ON b.readertypcd = c.readertypcd
         WHERE a.readercardno = $readercardno
        """, vars = locals())
    for item in query:
        return item
    return None

def decreaseAcc(readerid, money):
    fn_db.decrease("LIM_READER", "readerid", readerid, 'deposit', money)

def increaseAcc(readerid, money):
    fn_db.increase("LIM_READER", "readerid", readerid, 'deposit', money)

def bind_ref(reader):
    fn_ref.bind(reader,
               gender = "GENDER",
               orgcd = "ORG",
               cardsts = "CARDSTS")



