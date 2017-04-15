# http://www.pythonchallenge.com/pc/def/map.html

import string

s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

form_str = "abcdefghijklmnopqrstuvwxyz"
post_str = "cdefghijklmnopqrstuvwxyzab"
rule = str.maketrans(form_str, post_str)


print(s.translate(rule))
print('map'.translate(rule))
