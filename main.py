data = [0] * 100
from parse import parse
try:
    import cfg
    cfg.breakvar = 0
except:
    print("Error: varable cannot be imported. Make sure that  cfg.py exists.")
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
while len(code)>i:
    if cfg.breakvar == 1:
      break
    else:
      parse(code,i,data)
      print(code[i])
    i=i+1
if cfg.breakvar==0:
    while True:
        pass
else:
    print("EOF")
