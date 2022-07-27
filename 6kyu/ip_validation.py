#https://www.codewars.com/kata/515decfd9dcfc23bb6000006
import re
def is_valid_IP(strng):
    if re.fullmatch(
            r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}'
            r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
            r'', strng):
        return True
    else:
        return False

print(is_valid_IP('12.255.56.1'))