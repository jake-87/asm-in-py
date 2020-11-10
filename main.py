data =[]
from parse import parse
import cfg
try:
    print(cfg.breakvar)
except:
    print("no breakvar")
lines = []
while True:
    line = input()
    if line != "EOF":
        lines.append(line)
    else:
        break
text = ' '.join(lines)
text=text.replace(","," ")
code=text.split()
i=0
print(len(code))
print(i)
print(cfg.breakvar)
while len(code)>i:
    if cfg.breakvar == 1:
      break
    else:
      parse(code,i,data)
      print(str(cfg.breakvar) + " is breakvar")
if cfg.breakvar==0:
    while True
        pass
else:
    print("EOF")
