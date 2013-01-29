# -*- coding: utf-8 -*-

import sys
import os
if sys.hexversion > 0x03000000:
    import  winreg
else:
    import  _winreg as winreg

def update_env_profile(config_file=None):
    if config_file is None:
        config_file = r"d:/opt/conf/profile/profile.conf"

    if not os.path.exists(config_file) :
        print "file %s not exist!" % config_file
        return

    with open(config_file,'r') as f:
        for line in f:

            if not line or not line.strip('\n'): continue
            if line.startswith("#"):
                print 'comment ', line
                continue

            item = line.strip('\n').split('=')
            name ,value = item[0], item[1]
            print name, '=', value
            set_env_value(name, value)

def set_env_value(name,value):
    root = winreg.HKEY_CURRENT_USER
    sub_key = r"Environment"
    with winreg.OpenKey(root,sub_key,0,winreg.KEY_ALL_ACCESS) as key:
        #  winreg.REG_EXPAND_SZ: Null-terminated string containing references to environment variables (%PATH%).
        winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
        winreg.FlushKey(key)

if __name__ == "__main__":
    print 'start process env profile'
    update_env_profile()



