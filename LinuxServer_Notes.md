## COMMON COMMANDS
* Run as Super user _`> sudo (program)`_ <br/>

* List Packages _`> cat /etc/apt/sources.list`_ <br/>

* Look for Updates _`> sudo apt-get update`_ <br/>

* Install Updates _`> sudo apt-get upgrade`_ <br/>

* Remove Uneeded Packages _`> sudo apt-get autoremove`_ <br/>

* Install Sources _`> sudo apt-get install (program)`_
	```	
	examples: 
	> sudo apt-get install apache2
	> sudo apt-get install postgresql
	> sudo apt-get install memcached
	```
* User Information _`> cat /etc/passwd`_
	- _username:encryptpasswd:userid:groupid:userdesc:userhome:usershell_
```	
examples: 
	vagrant:x:1000:1000:vagrant,,,:/home/vagrant:/bin/bash		
		username = vagrant
		encrypt_passwd = x
		userid = 1000
		groupid = 1000
		user_desc = *empty*
		userhome = /home/vagrant
		usershell = /bin/bash
	root:x:0:0:root:/root:/bin/bash
		username = root
		encryptpasswd = *x*
		userid = 0
		groupid = 0
		userdesc = root
		userhome = /root:
		usershell = /bin/bash
```
## PACKAGES
	- Apache HTTP Server
		+ apache2
	- PostgreSQL
		+ postgresql
	- Memcache
		+ memcached
## CREATING NEW USERS
	- sudo adduser

