#/usr/bin/env python
import string, sys
from pybitcointools import *

count = 0
vanity = str(sys.argv[1])

while True:
	print "Searching... %s" % count
	seed = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(128))
	pk = sha256(seed)
	pk_wif = encode_privkey(decode_privkey(pk), 'wif', -7)
	if vanity in privtoaddr(pk, magicbyte='76'):
		print "\nSeed: %(seed)s \nPrivate Key (SHA256): %(pk)s \nPrivate Key (WIF): %(pk_wif)s \nAddress: %(addr)s" % {'seed': seed, 'pk': pk, 'pk_wif': pk_wif, 'addr': privtoaddr(pk, magicbyte='76')}
		break
	count += 1
