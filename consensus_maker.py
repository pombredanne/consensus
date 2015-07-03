from consensus_list import consensus_list

from urllib.request import urlopen, ProxyHandler, build_opener, install_opener
from hashlib import sha256
from datetime import datetime
import os

install_opener(build_opener(ProxyHandler({'http': '127.0.0.1:8118'})))

with open('consensus_hashes.txt', 'w') as f:
	f.write("This overview was created on: " + str(datetime.now()).split().pop(0) + "\n")
	f.write("Packages are described as follows:\n\n")
	f.write("name | version | platform\n")
	f.write("Retrieved from: <url>\n")
	f.write("Digest: sha256_digest | filename \n\n")
	f.write(str("".join(["-" for _ in range(100)])) + "\n\n")
	
	for (name, version, platform, url) in consensus_list:
		filename = url.split("/").pop()
		print("Downloading: " + name + " \t| " + filename)
		try:
			digest = sha256(urlopen(url).read()).hexdigest()
			f.write(name + " | " + version + " | " + platform + "\n")
			f.write("Retrieved from: " + url + "\n")
			f.write("Digest: " + digest + " | " + filename + "\n\n")
		except:
			print("FAILED to download " + filename + " at: " + url)
			print(filename + " is NOT in the consensus.")

os.system("gpg --clearsign consensus_hashes.txt")

