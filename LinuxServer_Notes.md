## COMMON COMMANDS
* Run as Super user
	-  _`> sudo`_` `**_`[program]`_**<br/>
* List Packages
	- _`> cat /etc/apt/sources.list`_
* Look for Updates
	- _`> sudo apt-get update`_
* Install Updates
	- _`> sudo apt-get upgrade`_
* Remove Uneeded Packages
	- _`> sudo apt-getautoremove`_
* Install Sources
	- _`> sudo apt-get install`_ **`[program]`**<br/>
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
