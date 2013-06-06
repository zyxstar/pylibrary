#coding:utf-8
import web, os, datetime, traceback, StringIO
_dir = os.path.abspath(fn_utils.module_path())

db = web.database(dbn = 'sqlite', db = _dir + '/database/data')
#db = web.database(dbn = 'sqlite', db = _dir + '/../database/data')

def ins(table, **kw):
    kw['insdt'] = datetime.datetime.now()
    kw['upddt'] = datetime.datetime.now()
    return db.insert(table, **kw)

def upd(table, keynm, keyval, **kw):
    kw['upddt'] = datetime.datetime.now()
    db.update(table, where = '%s=$%s' % (keynm, keynm), vars = {keynm:keyval}, **kw)

def get(table, keynm, keyval):
    for item in db.select(table, where = '%s=$%s' % (keynm, keynm), vars = {keynm:keyval}):
        return item
    return None

def delete(table, keynm, keyval):
    db.delete(table, where = '%s=$%s' % (keynm, keynm), vars = {keynm:keyval})

def increase(table, keynm, keyval, field, step = None):
    if step == None:step = 1
    kw = {'upddt':datetime.datetime.now(), keynm:keyval}
    db.query("UPDATE %s SET upddt=$upddt,%s=%s+%s WHERE %s=$%s" % (table, field, field, step, keynm, keynm), vars = kw)

def decrease(table, keynm, keyval, field, step = None):
    if step == None:step = 1
    kw = {'upddt':datetime.datetime.now(), keynm:keyval}
    db.query("UPDATE %s SET upddt=$upddt,%s=%s-%s WHERE %s=$%s" % (table, field, field, step, keynm, keynm), vars = kw)

def getExceptMsg():
    fp = StringIO.StringIO()
    traceback.print_exc(file = fp)
    return fp.getvalue()


def deleteTest():
    def _d(table, keynm):
        db.delete(table, where = "%s like 'T_%s'" % (keynm, '%'))
    _d("LIC_READERTYP", "readertypcd")
    _d("LIM_READERCARD", "readercardno")
    _d("LIM_READER", "readerid")
    _d("LIM_BOOKCLS", "bookclsid")
    _d("LIM_BOOKINS", "bookinsid")
    _d("LIT_BORRNOW", "readerid")
    _d("LIT_BORRHIS", "readerid")
    _d("LIT_BORRLOG", "bookinsid")
    
