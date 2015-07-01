# Consensus
A signed list of hashes of downloads that are otherwise not distributed securely.

There exist many valuable projects that, unfortunately, are not distributed in a secure way.
Using the downloads from these projects is scary, because it is not possible to verify your download. 
Some such projects include:

- Bootstrap
- gpg4usb
- HTTPS Everywhere
- jQuery

To verify the hashes, make sure you have my (Hephaestos) gpg key. It can be found [here](https://raw.githubusercontent.com/hephaest0s/public_key/master/Hephaestos.asc), and has the following fingerprint: 8764 EF6F D5C1 7838 8D10 E061 CF84 9CE5 42D0 B12B.
Once you have the key imported into gpg, run the following command: `gpg --verify consensus_hashes.txt.asc'

If the gpg signature checks out, and the sha256 hash of your download matches the one in our consensus, then this is of course NO GUARANTEE that your download is not malicious. However, it does provide an indicate that there is some consensus about what files are being distributed, and that you have the same files as everyone else.

You are *encouraged* to add additional projects to our list. You can do so by filing an issue linking to the project or, better yet, editing consensus_list.py and creating a pull request.
Projects can be added, only if they do not provide a secure distribution method. Uploading a public signing key that can only be downloaded from the same http-only website is not a secure distribution method.
