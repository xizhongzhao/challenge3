#!/usr/bin/env python3

class Config(object):
    def __init__(self,configfile):
        self._configfile = configfile
        self._config = {}
    def get_config(self,key=None):
        with open(self._configfile,'r') as file:
            for line in file:
                s = line.split('=')
                fkey = s[0].strip()
                fvalue = s[1].strip()
                self._config[fkey] = fvalue
        if key == None:
            print(self._config)
        else:
            print(self._config[key])


class UserDate(object):
    def __init__(self,userdatafile):
        self._userdatafile = userdatafile
        self._userdata = {}
    def get_userdata(self,key=None):
        with open(self._userdatafile) as file:
            for line in file:
                s = line.split(',')
                fkey = s[0].strip()
                fvalue = s[1].strip()
                self._userdata[fkey] = fvalue
        if key == None:
            return self._userdate
        else:
            return self._userdate[key]



class                            
