import urllib
import fcntl, socket, struct
import json
import os, glob
import time, subprocess
 
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
        response     = urllib.urlopen('http://secret-mountain-2856.herokuapp.com/info/' + escape(getHwAddr('eth0')))
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
       
        if data['type'] == 'video':
                print 'Downloading Video..'
                file            = str(data['file'])
                filename        = str(data['filename'])
                urllib.urlretrieve(file, filename=filename)
                #os.system('omxplayer -o hdmi -b --loop ' + filename)
                os.system('/home/pi/RaspresPy/hello_video.bin /home/pi/RaspresPy/'+filename)
        elif data['type'] == 'presentation':
                print 'Downloading Presentation..'
                file            = str(data['file'])
                filename        = str(data['filename'])
                urllib.urlretrieve(file, filename='Videos/'+filename)
                os.system('soffice -show Videos/'+filename+' --norestore &')