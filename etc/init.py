import subprocess

integration_token = input('integration token: ')

subprocess.run(['cp', 'secrets/secrets_sample.py', './secrets.py'])
subprocess.run(['sed', '-i', '-e', f's/INTEGRATION_TOKEN =/INTEGRATION_TOKEN = "{integration_token}"/', 'secrets.py'])
subprocess.run(['rm', '-rf', 'secrets.py-e'])

pip_list = subprocess.Popen(['pip', 'list'], stdout=subprocess.PIPE)
grep_requests = subprocess.Popen(['grep', 'requests'], stdin=pip_list.stdout, stdout=subprocess.PIPE)
pip_list.stdout.close()
if grep_requests.communicate()[0].decode() == '':
  subprocess.run(['pip', 'install', 'requests'])

print('All green.')
