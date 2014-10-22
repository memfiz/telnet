#!/usr/bin/env python
# -*- coding: utf8 -*-

'''Element Manager xr class'''

__author__ = "Arnis Civciss (arnis.civciss@lattelecom.lv)"
__copyright__ = "Copyright (c) 2012 Arnis Civciss"
#__version__ = "$Revision: 0.1 $"
#__date__ = "$Date: 2012/01/08 $"
#__license__ = ""

import re
from lib.telnet import Telnet

class CliError(Exception):
  '''iSAM command line error exception class.'''
  def __init__(self, command, output):
      '''Initialize cli exception. Join output in one string if it's a list.'''
      self.command = command
      if isinstance(output, list):
        self.output = ''.join([`num` for num in output])
      else:  
        self.output = output
  def __str__(self):
      '''Returns friendly cli error. Command and error ouput.'''
      return "cli error in command: %s\nOutput: %s." % (self.command, self.output)

class EmXr(Telnet):
  '''XR Element Manager Class'''
  def __init__(self, **kwargs):
    '''Initialize the node. Mandatory parameter - host - node IP address.
    Default parameters:
    user = 'script2'    
    passwd = 'xxxx'
    login_wait = 'name:'
    password_wait = 'assword:'
    prompt='#'
    timeout= 15
    port = 23
    enable_string=''
    enable_prompt=''
    enable_passwd = ''
    enable_wait=''
    init_command='terminal length 0'
    debuglevel=None #100 is debug on
    '''
    host = kwargs['host']
    debuglevel = kwargs.get('debuglevel', 100)
    user = 'user'  
    passwd = 'password'
    login_wait = 'name:'
    password_wait = 'assword:'
    prompt='#'
    timeout= 15
    port = 23
    enable_string=''
    enable_prompt='#'
    enable_wait = 'assword'
    init_command = 'terminal length 0'
    enable_passwd = ''
    self.cli_err = re.compile('% Invalid input|% Bad IP|% Access denied|% No such configuration|%|Namespace is locked by another agent|Do you wish to proceed with this commit anyway', re.DOTALL)
    Telnet.__init__(self, host, user, passwd, login_wait, password_wait, port,
                prompt, timeout, enable_string, enable_prompt, enable_passwd, 
                enable_wait, init_command, debuglevel)
  
  #def write_raw_sequence(self, seq):

  def open(self):
    out = Telnet.open(self)
    reh = re.compile('\n([^#]+)', re.DOTALL)
    out = Telnet.run_command(self, 'terminal exec prompt no-timestamp')
    out = Telnet.run_command(self, 'terminal monitor disable')
    if reh.search(out).group(1):
      part = (reh.search(out).group(1)).rsplit(':')[1]
      self.prompt = part
      self.hostname = part

  def run_command(self, command):
    '''Runs any command on the node. Raises CliError in case of syntax errors.
    Returns output as a list.'''
    out = Telnet.run_command(self, command)
    out = out.translate(None, '\b')
    if self.cli_err.search(out):
      raise CliError(command, out)
    return out
       
if __name__ == "__main__":
  pass
  try:
    rtr = EmXr(host='192.168.140.1', debuglevel=0)
    rtr.open()
    print rtr.hostname
    print rtr.prompt
    out = rtr.run_command('show arp vrf ngn vlan 4005')
    for key, value in arp.items():
      print "Key %s, Value %s" % (key, value)

  except CliError as e:
    print 'Cli Error %s ' % e

  # except CliError as e:
  #   print 'Cli Error %s ' % e


