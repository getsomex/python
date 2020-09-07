import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'a'

pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

password = 'mishaaaa%&21'
check = pattern2.fullmatch(password)

print(check)
