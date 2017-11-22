## COMMON COMMANDS
* Run as Super user
	- _> sudo_ __`<enter command name>`__ >
* List Packages
	- _> cat /etc/apt/sources.list_
* Look for Updates
	- _> sudo apt-get update_
* Install Updates
	- _> sudo apt-get upgrade_
* Remove Uneeded Packages
	- _> sudo apt-getautoremove_
* Install Sources
	- _> sudo apt-get install_ __`<enter program name>`__<br/>
		```
		ewfseafdvfsdvc \n add
		```
		```	
		sudo apt-get install apache2
		sudo apt-get install postgresql
		sudo apt-get install memcached
		```
* User Information 
	- _`> cat /etc/passwd   [username:encryptpasswd:userid:groupid:userdesc:userhome:usershell]`_<br/>	
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
