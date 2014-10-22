#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Telnet class

SLEM Telnet basic
Can telnet into devices with password, login/password, without passwords.
Additionally enable password can be used. 
For debug use debuglevel=100.

"""

__author__ = "Arnis Civciss (arnis.civciss@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2012/01/08 $"
__license__ = ""

import telnetlib

class Telnet:
  """Basic Telnet class"""
  def __init__(self, host,  user=None, passwd=None, login_wait=None, password_wait=None, port=23,
                prompt='>', timeout=5, enable_string=None, enable_prompt='#', enable_passwd = None, 
                enable_wait='assword', init_command=None, debuglevel=None):
    """Init params"""
    self.host = host
    self.port = port
    self.login_wait = login_wait
    self.user = user
    self.password_wait = password_wait
    self.passwd = passwd
    self.prompt = prompt
    self.timeout = timeout
    self.enable_prompt = enable_prompt
    self.enable_passwd = enable_passwd
    self.enable_wait = enable_wait
    self.enable_string = enable_string
    self.init_command = init_command
    self.debuglevel = debuglevel
    self.tnobj = ''

  def open(self):
    """Opens telnet connection to a device"""
    self.do_login()
    self.do_enable()
    return self.init_cmd()

  def do_login(self):
    """Opens telnet connection and does login procedure"""
    tn = telnetlib.Telnet(self.host, self.port, self.timeout)
    self.tnobj = tn
    # sock = tn.get_socket()
    # if sock is not None:
    #   sock.send(chr(255) + chr(254) + chr(1))
    if self.debuglevel:
      self.set_debuglevel(self.debuglevel)
    if self.login_wait:
      tn.read_until(self.login_wait, self.timeout) 
      tn.write(self.user + '\r\n')
    if self.password_wait:
      tn.read_until(self.password_wait, self.timeout)
      tn.write(self.passwd + '\n')
      tn.read_until(self.prompt, self.timeout)
      
  def init_cmd(self):
    """executes init command"""
    if self.init_command:
      self.tnobj.write(self.init_command + '\n')
      if self.enable_prompt:
        return self.tnobj.read_until(self.enable_prompt, self.timeout)
      else:
        return self.tnobj.read_until(self.prompt, self.timeout)
  
  def do_enable(self):
    """enters enable mode if enable is specified"""
    if (self.enable_string) and (not self.enable_passwd):
      self.tnobj.write(self.enable_string + '\n')
      self.tnobj.read_until(self.enable_prompt, self.timeout) 
      self.prompt = self.enable_prompt
    elif (self.enable_string) and (self.enable_passwd):
      self.tnobj.write(self.enable_string + '\n')
      self.tnobj.read_until(self.enable_wait, self.timeout)
      self.tnobj.write(self.enable_passwd + '\n')
      self.tnobj.read_until(self.enable_prompt, self.timeout) 
      self.prompt = self.enable_prompt

  def set_debuglevel(self, debuglevel):
    """changes debuglevel: 0 - no debug, 100 - debug"""
    self.tnobj.set_debuglevel(debuglevel)

  def set_timeout(self, timeout):
    """changes timeout value"""
    self.timeout = timeout

  def run_command(self, command):
    """Runs any command on a router"""
    self.tnobj.write(command + str("\n"))
    output = self.tnobj.read_until(self.prompt, self.timeout)
    return output

        
  def close(self):
    """Closes telnet connection to a device"""
    self.tnobj.close()
    
if __name__ == "__main__":
  print('test')
  
  #Cisco IOS test        
  try:
    tel = Telnet(login_wait='name: ', password_wait='assword: ', host='192.168.148.26', port=23, user='xxx', 
      passwd='xxx', prompt='>', timeout=5, enable_string='enable', enable_wait='assword:', enable_prompt='#', 
      enable_passwd='xxxx', init_command='term length 0', debuglevel=0)
    tel.open()
    tel.set_timeout(600)
    tel.set_debuglevel(0)
    ver = tel.run_command('show ver')
    for line in ver:
      print line
  except Exception as e:
    print 'show run error: ' + str(e)

  

  # ver = tel.run_command('show proc cpu | e 0.00')
  # for line in ver:
  #   print line
  
  # ver = tel.run_command('show ip arp')
  # for line in ver:
  #   print line

  # tel.close()

  #Isam test
  # isam = Telnet(login_wait='ogin: ', password_wait='assword: ', host='10.165.12.15', port=23, user='isadmin', passwd='xxxxxxx', prompt='#', timeout=5)
  # isam.open()
  # ver = isam.run_command('show system cpu-load')
  # for line in ver:
  #   print line

  # try:
  #   gpon = Telnet(login_wait='name:', password_wait='assword:', host='192.168.104.24', 
                    # port=23, user='script', passwd='xxxxxx', prompt='>', timeout=5, 
                    # enable_string='enable', enable_prompt='#', init_command='scroll 512')
  #   gpon.open()
  #   ver = gpon.run_command('display board 0')
  #   for line in ver:
  #     print line
  # except Exception as e:
  #   print e

  #Cisco IOS-XR test
  # try:
  #   crs = Telnet(login_wait='name:', password_wait='assword:', host='192.168.133.249', 
  #               port=23, user='xxxxx', passwd='xxxxxx', prompt='#', timeout=5, 
  #               init_command='terminal length 0', debuglevel=0)
  #   crs.open()
  #   ver = crs.run_command('show bgp summary')
  #   for line in ver:
  #     print line
  # except IOError as e:
  #   print e

  #Cisco - only pasword and enable
  # tel = Telnet(password_wait='assword: ', host='192.168.148.105', 
  #             port=23, passwd='xxxxx', prompt='>', timeout=5, 
  #             enable_string='enable', enable_wait='assword:', enable_prompt='#', 
  #             enable_passwd='xxxxxxx', init_command='term length 0', debuglevel=0)
  # tel.open()
  # ver = tel.run_command('show proc cpu | e 0.00')
  # for line in ver:
  #   print line

  #For module Cisco
  # def get_running_config(self):
  #   """Gets running-config from a Cisco router"""
  #   try:
  #     self.tnobj.write('sh run\n')
  #     running_cfg = self.tnobj.read_until(self.prompt, self.timeout)
  #     #self.tnobj.write('exit \n')
  #     #self.tnobj.close()
  #   except Exception as e:
  #       raise Exception('telnet.get_running_config error: ' + str(e))
  #   else:
  #       return running_cfg.split('\n')

  #TL1
  # try:
  #   tel = Telnet(host='10.2.52.152', port=3083, timeout=5, debuglevel=0, prompt=';')
  #   tel.open()
  #   tel.run_command('ACT-USER::administrator:22222::xxxxxxx;')
  #   #tel.set_debuglevel(100)
  #   ver = tel.run_command('RD-EU::DSLS0001719:222222;')
  #   for line in ver:
  #     print line
  # except Exception as e:
  #   print 'Errorrrrrrrrrrrrrrr: ' + str(e)
    


