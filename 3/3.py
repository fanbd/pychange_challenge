"""
http://www.pythonchallenge.com/pc/def/equality.html
"""

import re
f = open('a.txt')
ans = ''
tmp = f.read()
pattern = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"
for match in re.findall(pattern, tmp):
    ans += match[4]

print(ans)



"""
import urllib.request as ur
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"


def main():
    response = ur.urlopen(url)
    body = response.read()

    pattern = "[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]"

    result = re.findall(pattern, body.decode())
    print(result)


if __name__ == '__main__':
    main()
"""
