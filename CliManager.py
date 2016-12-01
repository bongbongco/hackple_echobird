# -*- coding: utf-8 -*-
#!/usr/bin/python

import mechanize
import facebook
import json
import os
import sys
import re
from requests import get
from urllib import urlopen, urlencode, quote
from urllib import urlencode
import facebook
from Config import GetTheConfig

reload(sys)
sys.setdefaultencoding('utf-8')


def Html2Image(message):
    webkit2png = "webkit2png -o echobird "
    url = "http://127.0.0.1:5000/talk/"+quote(message)
    os.system(webkit2png + url)

    f= open("echobird-full.png")
    f.close

def main():
    Html2Image(sys.argv[1])
    print "complete"

if __name__ == '__main__':
    main()