<table>
	<tbody>
		<tr>
			<th> <b>APT-GET</b> </th>
		</tr>
		<tr>
			<td>
				<table>
					<thead>
						<tr>
							<th align="left">Option</th>
							<th align="left">Description</th>
							<th align="left">Usage</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td align="left">update</td>
							<td align="left">Search For Updates</td>
							<td align="left"><em><code>&gt; sudo apt-get update</code></em></td>
						</tr>
						<tr>
							<td align="left">upgrade</td>
							<td align="left">Install All Updates</td>
							<td align="left"><em><code>&gt; sudo apt-get upgrade</code></em></td>
						</tr>
						<tr>
							<td align="left">autoremove</td>
							<td align="left">CleanPackage Files</td>
							<td align="left"><em><code>&gt; sudo apt-get autoremove</code></em></td>
						</tr>
					</tbody>
				</table>
			</td>
		</tr>
	</tbody>
</table>

| Description | Usage | Examples |
|:---|:---|:---|
|Super User| sudo  | Run Program SU _`sudo /path/to/my/program`_ |
|Sources| /etc/apt/sources.list | List All Packages _`> cat /etc/apt/sources.list`_ |
|Look For Updates| __sudo apt-get update__ |  |
|Install All Updates| __sudo apt-get upgrade__|  |
|Clean Package Files| __sudo apt-getautoremove__ |  |
|Install Sources| __sudo apt-get install__ _`<program name>`_ | `sudo apt-get install apache2`<br/>`sudo apt-get install postgresql` <br/> `sudo apt-get install memcached` |
|User Information|  |  |

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
