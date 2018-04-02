#!/usr/bin/python3
import sys
from email.parser import Parser

if len(str(sys.argv[1])) > 1:

 print (str(sys.argv[1]))

 with open(str(sys.argv[1])) as fp:
     headers = Parser().parse(fp)

 if "yourdomain-name-or-part the email-from-or-to.hu" in headers['to']:
  print (headers['to'])
  cimekto = headers['to'].split()
  i = 0
  tocim = ""

  while i < len(cimekto):
     if "yourdomain-name-or-part the email-from-or-to.hu" in cimekto[i]:
         tocim = cimekto[i]
     i += 1

  tocim = tocim.translate({ord(c): None for c in '<>,'})
  print('To: %s' % tocim)
  f = open("import.sh","a")
  line = "zmmailbox -z -m "+tocim+" addMessage /inbox "+sys.argv[1]+"\n"
  f.write(line)
  f.close()
