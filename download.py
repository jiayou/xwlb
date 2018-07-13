# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 17:58:49 2018

@author: jiayou
"""

import sys
import subprocess
from datetime import datetime, timedelta


count =  int(sys.argv[1])

if len(sys.argv) > 2:
    start_date = datetime.strptime(sys.argv[2], '%Y%m%d')
else:
    start_date = datetime.now()


def curl(url, filename):
    subprocess.call("curl "+url+" > "+filename, shell=True)


for N in range(count):
    D = start_date - timedelta(days=N)
    url = 'http://mrxwlb.com/'+str(D.year)+'%e5%b9%b4'+str(D.month)+'%e6%9c%88'+str(D.day)+'%e6%97%a5%e6%96%b0%e9%97%bb%e8%81%94%e6%92%ad%e6%96%87%e5%ad%97%e7%89%88/'
    curl(url, r"./pages/"+D.strftime('%Y%m%d'))
    
    
