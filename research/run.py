import os

print('current working dir [{0}]'.format(os.getcwd()))
print(os.listdir('.'))
w_d = os.path.dirname(os.path.abspath(__file__))
print('change working dir to [{0}]'.format(w_d))
os.chdir(w_d)
print(os.listdir('.'))

print('/data:')
print(os.listdir('/data'))


for l in os.popen('/bin/bash -c "cd {0} && source ./run.sh"'.format(w_d)):
    print(l.strip())
