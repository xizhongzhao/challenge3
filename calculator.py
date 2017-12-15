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



class Salary(object):
    #bftax is salary before the pitax
    def __init__(self,bftax,soinsurp,basel,baseh):
        self._bftax = bftax
        self._soinsur = 0.0
        self._pitax = 0.0
        self._aftax = 0.0
        self._soinsurp = soinsurp
        self._basel = basel
        self._baseh = baseh

    def get_soinsur(self):
        if self._bftax <= self._basel:
            return self._basel * self._soinsurp
        elif self._bftax >= self._baseh:
            return self._baseh * self.soinsurp
        else:
            return self.bftax * self.soinsurp
    
    def get_pitax(self):
        taxbase = self._bftax - self._soinsur - 3500
        if taxbase <= 0:
            return 0
        elif taxbase > 0 and taxbase <= 1500:
            return taxbase * 0.03
        elif taxbase > 1500 and taxbase <= 4500:
            return (taxbase * 0.1 - 105)
        elif taxbase > 4500 and taxbase <= 9000:
            return (taxbase * 0.2 - 555)
        elif taxbase > 9000 and taxbase <= 35000:
            return (taxbase * 0.25 - 1005)
        elif taxbase > 35000 and taxbase <= 55000:
            return (taxbase * 0.3 - 2755)
        elif taxbase > 55000 and taxbase <= 80000:
            return (taxbase * 0.35 - 5505)
        else:
            return (taxbase * 0.45 - 13505)

    def get_aftax(self):
        return self._bftax - self._insur - self._pitax                          
if __name__ == '__main__':
    
