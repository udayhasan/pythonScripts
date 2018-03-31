import os

off_jump="012b"
off_ldstbr="06b"
off_other="03b"

ldstbr_list=["lw", "sw", "beq", "bne"]
other_list=["add", "sub", "inv", "invert", "lsl", "lsr", "and", "or", "slt", "xor"]

def instruction(ins):
    code=""
    if(ins=="lw"):
        code="0000"
    elif(ins=="sw"):
        code="0001"
    elif(ins=="add"):
        code="0010"
    elif(ins=="sub"):
        code="0011"
    elif(ins=="inv" or ins=="invert"):
        code="0100"
    elif(ins=="lsl"):
        code="0101"
    elif(ins=="lsr"):
        code="0110"
    elif(ins=="and"):
        code="0111"
    elif(ins=="or"):
        code="1000"
    elif(ins=="slt"):
        code="1001"
    elif(ins=="xor"):
        code="1010"
    elif(ins=="mov"):
        code="1011"
    elif(ins=="addi"):
        code="1100"
    elif(ins=="subi"):
        code="1101"
    elif(ins=="srl"):
        code="1110"
    elif(ins=="sra"):
        code="1111"
    else:
        code="error"
        print "ERROR! Please, correct INSTRUCTION!"

    return code

def address(add):
    code=""
    if(add=="r0"):
        code="000"
    elif(add=="r1"):
        code="001"
    elif(add=="r2"):
        code=="010"
    elif(add=="r3"):
        code="011"
    else:
        code="error"
        print "ERROR! Please, correct SOURCE/DESTINATION/WRITE_ADDRESS!"

    return code

def offset(off, ins):
    code=""
    val=int(off)
    if(ins=="j"):
        code=format(val, off_jump)
    elif(ins in ldstbr_list):
        code=format(val, off_ldstbr)
    elif(ins in other_list):
        code=format(val, off_other)
    else:
        code="error"
        print "ERROR! Please, correct OFFSET"

    return code

def jump_func(data):
	code=""
	code=instruction(data[0])+offset(data[1], data[0])
	print code
	return code

def ldstbr_func(data):
	code=""
	code=instruction(data[0])+address(data[2])+address(data[1])+offset(data[3], data[0])
	print code
	return code

def data_processing_func(data):
	code=""
	code=instruction(data[0])+address(data[2])+address(data[3])+address(data[1])+offset(0, data[0])
	print code
	return code

if __name__=="__main__":
    fname=raw_input("Name of instruction file: ")
    fname_new=fname.split(".")
    fname2=fname_new[0]+".bin"
    
    f1=open(fname, "r")
    rd=f1.read()
    rd=rd.lower()
    f1.close()
    dt=rd.split("\n")
    dt.pop(len(dt)-1)

    for line in dt:
        data=""
        put=""
        ins=""
        data=line.split(" ")
        print data
        ins=instruction(data[0])

        if(ins=="jump"):
        	put=jump_func(data)
        elif(ins in ldstbr_list):
        	put=ldstbr_func(data)
        else:
        	put=data_processing_func(data)

        f2=open(fname2, "a")
        f2.write(put)
        f2.write("\n")
        f2.close


        

       

