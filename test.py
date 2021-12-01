from paramiko import SSHClient
import paramiko
paramiko.util.log_to_file('paramiko.log')
client = SSHClient()
client.load_system_host_keys()
client.connect("192.168.122.11",22,"devnet","devnet123",allow_agent=False,look_for_keys=False)
stdin, stdout, stderr = client.exec_command('ifconfig')
print(stdout.read())
client.close()
