import subprocess
import shutil

integration_token = input('integration token: ')

shutil.copy('secrets/secrets_sample.py', 'secrets.py')

with open('secrets.py') as f:
  origin = f.read()
  replace = origin.replace('INTEGRATION_TOKEN =', f'INTEGRATION_TOKEN = "{integration_token}"')

with open('secrets.py', mode='w') as f:
  f.write(replace)


pip_list = subprocess.Popen(['pip', 'list'], stdout=subprocess.PIPE)
grep_requests = subprocess.Popen(['grep', 'requests'], stdin=pip_list.stdout, stdout=subprocess.PIPE)
pip_list.stdout.close()
if grep_requests.communicate()[0].decode() == '':
  subprocess.run(['pip', 'install', 'requests'])


print('All green.')
