# ZimbraStoreImporter
This small python script makes the import script to process left alone Zimbra STORE
If you have only the Zimbra STORE files (/opt/zimbra/store) and you want to import the emails back to a working Zimbra instalation you can do it with ep.py
It makes a shell script witch can be run from the Zimbra command line.

INSTALL:
You need Python3 with basic libraries and email library

USE:
Make a backup of your Zimbra Store files.
Adjust the ep.py for your needs. In the initial release it search for incoming emails where your domain name is in the 'To' fields

Run the script with find: 
 find <path to your Zimbra Store files > -name '*.msg' -exec ./ep.py {} \;
Make the import.sh executable 'chmod 777 import.sh' Copy it under /opt/zimbra/backup for example.
Under zimbra command line (su zimbra) run the script. I suggest to run the script in a 'screen'
Large amount of emails import could last days.
  
