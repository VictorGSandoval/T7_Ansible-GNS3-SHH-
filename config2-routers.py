from paramiko import SSHClient

client = SSHClient()
client.load_system_host_keys()

for x in range(1, 3):
    client.connect("192.168.122.1" + str(x), 22, "devnet", "devnet123",allow_agent=False,look_for_keys=False)
    shell = client.invoke_shell()

    shell.send(b"enable\r")
    shell.send(b"trabajo1\r")
    shell.send(b"conf term\r")
    shell.send(b"int f0/0\r")
    shell.send(b"no sh\r")
    shell.send(b"exit\r")

    shell.send(b"int f0/0.10\r")
    shell.send(b"encapsulation dot1Q 10\r")
    shell.send(b"ip add 192.168.10.1 255.255.255.0\r")
    shell.send(b"exit\r")

    shell.send(b"int f0/0.20\r")
    shell.send(b"encapsulation dot1Q 20\r")
    shell.send(b"ip add 192.168.20.1 255.255.255.0\r")
    shell.send(b"exit\r")

    shell.send(b"ip dhcp excluded-add 192.168.10.1\r")
    shell.send(b"ip dhcp excluded-add 192.168.20.1\r")

    shell.send(b"ip dhcp pool vlan10\r")
    shell.send(b"network 192.168.10.0 255.255.255.0\r")
    shell.send(b"default-router 192.168.10.1\r")
    shell.send(b"exit\r")

    shell.send(b"ip dhcp pool vlan20\r")
    shell.send(b"network 192.168.20.0 255.255.255.0\r")
    shell.send(b"default-router 192.168.20.1\r")
    shell.send(b"end\r")

    shell.send(b"wr me\r")
    shell.send(b"\r")

    shell.close()
    client.close()
