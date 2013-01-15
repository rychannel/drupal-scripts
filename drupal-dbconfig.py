#!/usr/bin/python

import os
import subprocess

proc = subprocess.Popen(["drush @sites sql-conf --show-passwords --yes"], stdout=subprocess.PIPE, shell=True)
out,err = proc.communicate()

out=out.split('\n')

config=[]

for i in out:
	i=i.split(">>")
	del i[0]

	if len(i)>= 1:
		config.append(i[0].strip())

db={}
for x in config:
	x=str(x)
	if x != "Array" and x != "(" and x!= ")":
		x=x.strip()
		x=x.strip("[")
		x=x.split("=>")

		x[0]=x[0].strip()
		x[0]=x[0].strip("]")
		x[1]=x[1].strip()

		print x	
		db[x[0]]=x[1]
	if x == ")":
		print db
		print "yippie"

		### Do things like add db, add user/password here then clear the db
		### dictionary

		db={}
