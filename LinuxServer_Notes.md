# COMMON COMMANDS
* Run as Super user
	- *sudo (command call)*
* Look at package list
	- cat /etc/apt/sources.list
* Look for updates
	- sudo apt-get update
* Install updates
	- *sudo apt-get upgrade*
* Remove Uneeded Packages
	- *sudo apt-get autoremove*
* Install sources
	- *sudo apt-get install (program)*
* User Information
	- *> cat /etc/passwd*
		+ username:encryptpasswd:userid:groupid:userdesc:userhome:usershell
```		EXAMPLES:
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

# PACKAGES
* Apache HTTP Server
	- apache2
* PostgreSQL
	- postgresql
* Memcache
	- memcached

# CREATING NEW USERS
	* sudo adduser

