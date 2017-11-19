import sys

def echo(s):
    sys.stdout.write(s)

plain = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print "Plain text"
for x in plain:
    echo(x), echo(' ')
print ''
print ''
print "Cipher text"
for x in plain:
    echo(chr(ord(x)-2)), echo(' ')
print ''
print ''

plainText = "This is an extremely secret message and should be encoded."

upper = plainText.upper()

print "Secret message"
for c in upper:
    if ord(c) == 32:
        echo(' ')
    else:
        echo(chr(ord(c)-2))
