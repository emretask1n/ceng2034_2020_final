#EmreTaşkın-170709060

import os
import requests
import uuid

#1
child = os.fork()
if child == 0:
	print("Child process id",os.getpid())





#2
url= ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1Ko%C3%A7man%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg"]

child = os.fork()
if child == 0:
	def download_file(url, file_name=None):
		r = requests.get(url, allow_redirects=True)
		file = file_name if file_name else str(uuid.uuid4())
		open(file, 'wb').write(r.content)
	for i in url:
		download_file(i)

#3
#The wait() method of os module in Python enables a parent process to synchronize with the child process. i.e, To wait till the child process exits and then proceed.
#We can avoid the orphan process with this syscall.

child = os.fork()
if child == 0:
	os.system("ping -c 4 google.ca")
	print("child finished")
	os._exit(0)
os.wait()
os.system("ping -c 2 github.com")
print("parent finished")


#4
#!/usr/bin/python
import os
from multiprocessing import Pool
import hashlib
 
def hashing(filename):
	hasher = hashlib.md5()
	with open(filename, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
	print(hasher.hexdigest())


with Pool(2) as p:
	print(p.map(hashing, ['4fbe5b7a-4e20-417a-a85b-b7b7a52b997d' ,'943f3cf3-2de3-41d2-89f6-8e2f4a176d92', 'afbc8728-9f43-41b0-85f4-ee18b316c02c', 'bb6c5c19-4fde-4c61-ae16-fe093cba6f87', 'ddc53410-7a6d-4d84-8b03-064de2176bd5']))





