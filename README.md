telnet
======

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
