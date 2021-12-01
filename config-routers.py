import telnetlib

router1 = {
    "port": 5001,
    "secret": b"trabajo1",
    "username": b"devnet",
    "password": b"devnet123",
    "ip_address": b"192.168.122.11",
    "mask_address": b"255.255.255.0",
}

router2 = {
    "port": 5002,
    "secret": b"trabajo1",
    "username": b"devnet",
    "password": b"devnet123",
    "ip_address": b"192.168.122.12",
    "mask_address": b"255.255.255.0",
}

HOST = "localhost"
routers = [router1, router2]

for router in routers:
    tn = telnetlib.Telnet(HOST, port=router["port"])
    tn.write(b"\r")
    tn.write(b"\r")
    tn.write(b"\r")
    tn.write(b"\r")
    tn.write(b"\r")

    tn.write(b"conf term\r")

    tn.write(b"ip domain-name cisco\r")
    tn.write(b"enable secret " + router["secret"] + b"\r")
    tn.write(
        b"username " + router["username"] + b" password " + router["password"] + b"\r"
    )
    tn.write(b"in f0/0\r")

    tn.write(b"ip add " + router["ip_address"] + b" " + router["mask_address"] + b"\r")
    tn.write(b"no sh\r")
    tn.write(b"exit\r")

    tn.write(b"crypto key generate rsa general-keys modulus 2048\r")

    tn.write(b"line vty 0 4\r")
    tn.write(b"login local\r")
    tn.write(b"transport input ssh\r")
    tn.write(b"exit\r")

    tn.write(b"exit\r")

    tn.write(b"wr\r")
    tn.write(b"\r")
    print("router configured ...")
