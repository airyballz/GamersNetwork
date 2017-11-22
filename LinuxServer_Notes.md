## COMMON COMMANDS
* Run as Super user
	- __sudo__ _`<command name>`_<br/>
	`sudo apt-get update`<br/>
	`sudo apt-get upgrade`<br/>
* List Packages
	- __cat /etc/apt/sources.list__
* Look for Updates
	- __sudo apt-get update__
* Install Updates
	- __sudo apt-get upgrade__
* Remove Uneeded Packages
	- __sudo apt-getautoremove__
* Install Sources
	- __sudo apt-get install__ _`<program name>`_<br/>
	+`sudo apt-get install apache2`<br/>
	+`sudo apt-get install postgresql`<br/>
	+`sudo apt-get install memcached`<br/>
* User Information 
	- __> cat /etc/passwd__ _`[username:encryptpasswd:userid:groupid:userdesc:userhome:usershell]`_
		```linux
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
			usershell = /bin/bash ```
* New User _`> sudo adduser`_<br/>

## PACKAGES
	- Apache HTTP Server
		+ apache2
	- PostgreSQL
		+ postgresql
	- Memcache
		+ memcached
## CREATING NEW USERS
	- New User _`> sudo adduser`_<br/>
