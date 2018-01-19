def find_function_arg(addr):
    addr = idc.PrevHead(addr)
    if GetMnem(addr) == 'push' and idc.GetOpType(addr,0) == 5: #o_imm for constant
      preAddr= idc.PrevHead(addr)
      if GetMnem(preAddr) == 'push' and 5 == idc.GetOpType(preAddr,0):
         return True  
    return False

def decrypt(i):
	arr='AaCcdDeFfGhiKLlMmnNoOpPrRsSTtUuVvwWxyZz32.\EbgjHI _YQB:"/@'
	return arr[i]
	
def GetString(addr):
    result=''
    addr = idc.PrevHead(addr)
    addrString = GetOperandValue(addr,0)
    addrSize = idc.PrevHead(addr)
    size   = GetOperandValue(addrSize,0)
    i=0
    while (i < size):
          value = idc.Word(addrString)
          result += decrypt(value)
          i+=1
          addrString+=2
    idc.MakeComm(addr, result)
          	
for x in XrefsTo(0x004012A0, flags=0):
  ref = find_function_arg(x.frm)
  if(ref):
     GetString(x.frm)
  print "Ref Addr: 0x%x , the Address is : %s" % ((x.frm),ref)