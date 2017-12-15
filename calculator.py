#!/usr/bin/env python3

class Config(object):
    def __init__(self,configfile):
        self._configfile = configfile

    @property
    def config(self):
        config = {}
        with open(self._configfile,'r') as file:
            for line in file:
                s = line.split('=')
                fkey = s[0].strip()
                fvalue = s[1].strip()
                config[fkey] = fvalue
        return config 


class UserData(object):
    def __init__(self,userdatafile):
        self._userdatafile = userdatafile
    
    @property 
    def userdata(self):
        userdata = {}
        with open(self._userdatafile) as file:
            for line in file:
                s = line.split(',')
                fkey = s[0].strip()
                fvalue = s[1].strip()
                userdata[fkey] = fvalue
        return userdata
    
      

class Salary(object):
    #bftax is salary before the pitax
    #soinsurp is socail insur pecentage
    #basel is the lowest base
    #baseh is the hightest base
    def __init__(self,bftax,soinsurp,basel,baseh):
        self._bftax = bftax
        self._soinsurp = soinsurp
        self._basel = basel
        self._baseh = baseh
    @property 
    def soinsur(self):
        if self._bftax <= self._basel:
            return self._basel * self._soinsurp
        elif self._bftax >= self._baseh:
            return self._baseh * self._soinsurp
        else:
            return self._bftax * self._soinsurp
    
    @property
    def pitax(self):
        taxbase = self._bftax - self.soinsur - 3500
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
    @property
    def aftax(self):
        return self._bftax - self.soinsur - self.pitax                          
if __name__ == '__main__':
   import sys  
   config = Config('test.cfg')
   userdata = UserData('user.csv')
   print(config.config['JiShuL'])
   print(userdata.userdata['101'])    
    
   
