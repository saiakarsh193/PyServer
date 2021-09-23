import os

DEF_HOST_IP = '192.168.29.145'
DEF_PORT = 2004
DEF_BUFFER_SIZE = 4096

def isIP(ip):
    ind = ip.split('.')
    if not len(ind) == 4:
        return False
    for val in ind:
        if not val.isdigit():
            return False
    return True

def parseParams(path):
    params = {'HOST_IP': DEF_HOST_IP, 'PORT': DEF_PORT, 'BUFFER_SIZE': DEF_BUFFER_SIZE}
    if(os.path.isfile(path)):
        with open(path, 'r') as f:
            lines = f.read().split('\n')
        for line in lines:
            [par, val] = line.split(':')
            par = par.strip()
            val = val.strip()
            if(par == 'HOST_IP' and isIP(val)):
                params[par] = val
            elif((par == 'PORT' or par == 'BUFFER_SIZE') and val.isdigit()):
                params[par] = int(val)
    return [params['HOST_IP'], params['PORT'], params['BUFFER_SIZE']]
