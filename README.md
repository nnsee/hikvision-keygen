# Key generator to reset a Hikvision IP camera's admin password
### Details
This is a script to exploit older Hikvision devices' weak password reset key generation. More details and a write-up can be found in [this post](https://neonsea.uk/blog/2018/08/01/hikvision-keygen.html).
### Requirements
This script requires Python 3.6+ and `numpy`:
```
# pip install numpy
```
### Usage
Generate a reset key using:
```
./keygen.py <ip>
```
You can then use the key to reset the admin password using Hikvision's [Search Active Devices Protocol tool](https://www.hikvision.com/en/Support/Downloads/Tools).