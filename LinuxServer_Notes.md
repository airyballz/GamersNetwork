* test

| Description | Usage Desc | Example | Example |
|---|---|---|---|
|Run as Super user| __sudo__ _`<command name>`_ | _`sudo apt-get update`_ | _`sudo apt-get upgrade`_ |

|username|encryptpasswd|userid|groupid|userdesc|userhome|usershell|
|---|:---:|---|---|---|---|---|
|vagrant|x|1000|1000|*empty*|/home/vagrant|/bin/bash|
		
## COMMON COMMANDS
* Run as Super user
	- __sudo__ _`<command name>`_
		+ `sudo apt-get update`
		+ `sudo apt-get upgrade`
* List Packages
	- __cat /etc/apt/sources.list__
* Look for Updates
	- __sudo apt-get update__
* Install Updates
	- __sudo apt-get upgrade__
* Remove Uneeded Packages
	- __sudo apt-getautoremove__
* Install Sources
	- __sudo apt-get install__ _`<program name>`_
		+ `sudo apt-get install apache2`
		+ `sudo apt-get install postgresql`
		+ `sudo apt-get install memcached`
* User Information 
	- __> cat /etc/passwd__ _`[username:encryptpasswd:userid:groupid:userdesc:userhome:usershell]`_
		+ vagrant:x:1000:1000:vagrant,,,:/home/vagrant:/bin/bash <br/>				
		```
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
