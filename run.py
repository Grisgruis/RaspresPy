import urllib
import fcntl, socket, struct
import json
import os, glob
import time, subprocess
import sys
 
try:
     from html import escape
except ImportError:
     from cgi import escape
 
# Get Mac Adress
def getHwAddr(ifname):
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
     return ':'.join(['%02x' % ord(char) for char in info[18:24]])

# Get Vars
def getVars():
        print 'Retrieving data from server..'
        if len(sys.argv) > 1:
        	network = sys.argv[1]
        else:
        	network = 'wlan0'

        print 'Getting mac adress from network adapter ' + network
        response     = urllib.urlopen('http://raspres.local/info/' + escape(getHwAddr(network)))
        data         = json.loads(response.read())
        return data
 
# Get device vars
data            = getVars()
launched        = False
 
while ('check_often' in data):         
        if launched == False:
                print 'Launching MacAddress'   
                urllib.urlretrieve(str(data['file']), filename='mymac.pptx')
                os.system('soffice -show mymac.pptx --norestore &')
                launched = True        
       
        time.sleep(5)
        data = getVars()
else:  
        print 'Found on server'
        if launched == True:
                print 'Closing Impress..'
                impressPID = os.system('pkill soffice.bin')

        print 'Setting up Video..'
        url            = str(data['url'])
        os.system('youtube '+ url)