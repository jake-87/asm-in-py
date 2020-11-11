import cfg
def parse(code,i,data):
  if code[i] == "mov":
    mov(code,i,data)
  if code[i] ==  "int":
    interrupt(code,i,data)
datadict = {
  "eax":0,
  "ebx":1,
  "ecx":2,
  "edx":3,
  "var1":4,
  "var2":5,
  "var3":6,
  "var4":7
}
def mov(code,i,data):
  cfg.data[datadict.get(code[i+1])] = code[i+2]
def interrupt(code,i,data):
  #print("interupt~~")
  #print(code[i+1])
  if code[i+1] == "0x80" or "128":
    #print(data[0])
    if str(data[0]) == "4" or 4:
      doprint(code,i,data)
    if str(data[0]) == "1":
      cfg.breakvar = 1
      cfg.exitcode = data[1]
def doprint(code,i,data):
  #print(len(data[2])," is len(data[2])")
  #print(data[3], " is  data[3]")
  if str(len(cfg.data[2])) == str(cfg.data[3]):
    print(cfg.data[2])
