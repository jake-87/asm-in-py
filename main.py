from parse import parse
try:
    import cfg
    cfg.breakvar = 0
    cfg.data = [0]*100
    cfg.exitcode = 0
except:
    print("Error: varables cannot be imported. Make sure that  cfg.py exists and is in the same directory as main.py")
lines = []
f = open("myfile.txt", "w+")
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
for x in enumerate(code):
    if cfg.breakvar == 1:
      break
    else:
      parse(code,i,cfg.data)
    i=i+1
    f.write(str(code[i]))
    f.write(" ")
if cfg.breakvar==0:
    while True:
        pass
f.close()
print("Exited with code ",cfg.exitcode)
