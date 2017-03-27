MESSAGE = raw_input('enter string')

PLAINTEXT = ""

DECIMALS_LIST = MESSAGE.split(raw_input('enter replacement key'))
print DECIMALS_LIST

for DECIMAL in DECIMALS_LIST:
     DECIMAL = int(DECIMAL)
     PLAINTEXT = PLAINTEXT + chr(DECIMAL)

print "Plaintext: " + PLAINTEXT
