#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 10/Apr/2015
# File: SortIPs.py
# Desc: sort ips according to the connection time
#
# Produced By CSRGXTU
from Connection import Connection
from time import time

class SortIPs(object):
  IPS = None
  RES = None

  def __init__(self, ips):
    self.IPS = ips
    self.RES = []
    
    self.addTimes()

  # add connection times to the ips
  #
  # @return num int how many ips added times
  def addTimes(self):
    for ip in self.IPS:
      start = time()
      conn = Connection(ip)
      if conn.httpsConn():
        end = time()
        self.RES.append([ip, end - start])

    return len(self.RES)

  # sort ascending of the ips
  #
  # @return lst list
  def asc(self):
    return sorted(self.RES, key=lambda l: l[1])  

  # sort descending or the ips
  #
  # @return lst list
  def desc(self):
    return sorted(self.RES, key=lambda l: l[1], reverse=True)
  
  # get top n ips
  #
  # @param n int
  # @return lst list
  def getTopNIPs(self, n):
    res = [x[0] for x in self.asc()]
    return res[0:n]

  def getIPS(self):
    return self.IPS

  def getRES(self):
    return self.RES

  def setIPS(self, ips):
    self.IPS = ips

  def setRES(self, lst):
    self.RES = lst
