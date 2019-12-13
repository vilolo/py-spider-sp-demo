import re

str = 'adsfasdf url("asfasdfsadf")adsfasdf'

res = re.match(r".*\"(.*)\"",str)
print(res[1])