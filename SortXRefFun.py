# Get the segment's starting address
ea = ScreenEA()
# Loop through all the functions
j=0
matrix = []
for function_ea in Functions(SegStart(ea), SegEnd(ea)):
    i =0
    for xref in XrefsTo(function_ea, flags=0):
       #print xref.type, XrefTypeName(xref.type),                          'from', hex(xref.frm), 'to', hex(xref.to)
         i = i + 1
    matrix.append([function_ea , i])

matrix.sort(key=lambda x: x[1])
for line in matrix:
    print hex(line[0]),': ',GetFunctionName(line[0]) ,'refs: ', line[1]
