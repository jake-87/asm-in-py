import cfg
def parse(code,i,data):
  if code[i] == "mov":
    mov(code,i,data)
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
