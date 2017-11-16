from pprint import pprint as pp
import subprocess # to execute shell cammands

ip = subprocess.check_output('ifconfig')
pp(ip.decode("ascii"))
subprocess.call("cat /Users/skn/Pyhton/password.txt", shell=True)