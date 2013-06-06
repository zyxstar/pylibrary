#coding:utf-8
import fn_db
import fn_utils
import datetime
import os

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

_dir = os.path.abspath(fn_utils.module_path())
cache_opts = {
    'cache.type': 'file', #'memory'
    'cache.data_dir': _dir + '/cache/data',
    'cache.lock_dir': _dir + '/cache/lock'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

@cache.cache('getcdlist', expire = 3600)
def getcdlist(grp):
    q = fn_db.db.select('SYC_REFCD', what = 'cd,sdesc', where = 'grp=$grp', vars = locals(), order = 'ordseq')
    return [(item.cd, item.sdesc) for item in q]

def getcd(grp, key):
    dic = dict(getcdlist(grp))
    if dic.has_key(key):
        return dic[key]
    return ""

def bind(storage, **kw):
    for k, v in kw.items():
        storage[k + '_r'] = getcd(v, storage[k])

def ins_refcd(**kw):
    kw['insdt'] = datetime.datetime.now()
    kw['upddt'] = datetime.datetime.now()
    fn_db.db.insert('SYC_REFCD', **kw)
    cache.invalidate(getcdlist, 'getcdlist', kw['grp'])

def upd_refcd(grp, cd, **kw):
    kw['upddt'] = datetime.datetime.now()
    fn_db.db.update('SYC_REFCD', where = 'grp=$grp and cd=$cd', vars = locals(), **kw)
    cache.invalidate(getcdlist, 'getcdlist', grp)

def init_refcd():
    ins_refcd(grp = 'GENDER', cd = 'F', sdesc = u'女')
    ins_refcd(grp = 'GENDER', cd = 'M', sdesc = u'男')

    ins_refcd(grp = 'CARDSTS', cd = '0', sdesc = u'有效')
    ins_refcd(grp = 'CARDSTS', cd = '1', sdesc = u'挂失')
    ins_refcd(grp = 'CARDSTS', cd = '2', sdesc = u'注销')

    ins_refcd(grp = 'BOOKINSSTS', cd = '0', sdesc = u'可借')
    ins_refcd(grp = 'BOOKINSSTS', cd = '1', sdesc = u'已借')
    ins_refcd(grp = 'BOOKINSSTS', cd = '2', sdesc = u'丢失')

    ins_refcd(grp = 'BORRACT', cd = 'BORROW', sdesc = u'借出')
    ins_refcd(grp = 'BORRACT', cd = 'OVERDUE', sdesc = u'超期')
    ins_refcd(grp = 'BORRACT', cd = 'GIVEBACK', sdesc = u'归还')
    ins_refcd(grp = 'BORRACT', cd = 'RENEW', sdesc = u'续借')  
    ins_refcd(grp = 'BORRACT', cd = 'LOST', sdesc = u'丢失')
    ins_refcd(grp = 'BORRACT', cd = 'DEFACE', sdesc = u'污损')

    ins_refcd(grp = 'PAY', cd = 'CASH', sdesc = u'现金')
    ins_refcd(grp = 'PAY', cd = 'ACC', sdesc = u'记账')




    ins_refcd(grp = 'ORG', cd = 'SD', sdesc = u'自达康')
    ins_refcd(grp = 'ORG', cd = 'MD', sdesc = u'中间带')
    
    ins_refcd(grp = 'PLACE', cd = 'P1', sdesc = u'地方1')
    ins_refcd(grp = 'PLACE', cd = 'P2', sdesc = u'地方2')

    ins_refcd(grp = 'PUB', cd = 'P1', sdesc = u'PUB1')
    ins_refcd(grp = 'PUB', cd = 'P2', sdesc = u'PUB2')

    ins_refcd(grp = 'CAT', cd = 'C1', sdesc = u'CAT1')
    ins_refcd(grp = 'CAT', cd = 'C2', sdesc = u'CAT2')

