import napalm
from tabulate import tabulate

driver_ios = napalm.get_network_driver("ios")

devices = [
    {
        "host": "192.168.122.11",
        "system": "ios",
        "type": "router",
        "username": "devnet",
        "password": "devnet123",
        "secret": "tarea1",
    },
    {
        "host": "192.168.122.12",
        "system": "ios",
        "type": "router",
        "username": "devnet",
        "password": "devnet123",
        "secret": "tarea1",
    },
]

network_devices = []

for device in devices:
    network_devices.append(
        driver_ios(
            device["host"],
            device["username"],
            device["password"],
            optional_args={"secret": device["secret"]},
        )
    )

table_header = ["hostname", "vendor", "model", "uptime", "serial_number"]
table_body = []
for device in network_devices:
    device.open()
    device_facts = device.get_facts()
    device_info = []
    for att in table_header:
        device_info.append(device_facts[att])
    table_body.append(device_info)
print(tabulate(table_body, table_header))
