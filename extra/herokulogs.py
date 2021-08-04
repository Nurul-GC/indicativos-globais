from subprocess import getoutput
from os import chdir

chdir('..')
log = getoutput('heroku logs --tail')
with open('etc/heroku_logs.txt', '+w') as log_file:
    log_file.write(log)
    print('done..')
