#!/usr/bin/env python
# -*- coding: utf8 -*-

"""

SLEM Mydb Class

"""
__author__ = "Arnis Civciss (arnis.civciss@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2012/08/09 $"
__copyright__ = "Copyright (c) 2012 Arnis Civciss"
__license__ = ""

import sys
import MySQLdb as mdb

class Mydb:
  """Class Db implemets methods to access SLEM Mysql data base."""
  def __init__(self, **kwargs):
    """Init - host, user, passwd, dbname - params."""
    self.host = kwargs['host']
    self.user = kwargs['user']
    self.passwd = kwargs['passwd']
    self.dbname = kwargs['dbname']
    
  def connect(self):
    """Connects and creates cursor and db handler."""
    self.dbh = mdb.connect(self.host,self.user,self.passwd,self.dbname)
    self.cursor = self.dbh.cursor(mdb.cursors.DictCursor)
     
  def do_sql(self, sql, sql_data=None, get='get'):
    '''Executes sql statement 
        if get=='get' selects and returns rows and rowcount.
        if get=='set' does executemany. sql_data is a tuple of parameters.
        e.g. 
        sql = """INSERT IGNORE INTO dslamz_dslamtype (type) VALUES (%s)"""
        sql_data = [("ETH"),("ATM")]
        try:
          la = mango.do_sql(sql, sql_data, 'set')
        except mango.Error(), e:
            print "Db Error %d: %s" % (e.args[0], e.args[1])
    '''
    if get == 'get':
      self.cursor.execute(sql)
      rows = self.cursor.fetchall()
      rowcount = self.cursor.rowcount
      return rows, rowcount
    elif get == 'set': 
      self.cursor.executemany(sql, sql_data)
      self.dbh.commit ()
      return 1
    else: pass

  def Error(self):
    """Error handling"""
    return mdb.Error

  def close(self):
    """Close connection."""
    self.dbh.close()
    
  def get_host(self):
    """returns host attribute"""
    return self.host

  def get_user(self):
    """returns user attribute"""
    return self.user

  def get_dbname(self):
    """returns dbname attribute"""
    return self.dbname

  def get_passwd(self):
    """returns passwd attribute"""
    return self.passwd

