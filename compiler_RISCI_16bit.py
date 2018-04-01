#!/bin/python
import os
os.system("reset")

off_jump="012b"
off_ldstbr="06b"
off_other="03b"

ldstbr_list=["lw", "sw", "beq", "bne"]
other_list=["add", "sub", "inv", "invert", "lsl", "lsr", "and", "or", "slt", "xor", "mov"]

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
    elif(ins=="ham"):
        code="1010"
    elif(ins=="beq"):
        code="1011"
    elif(ins=="bne"):
        code="1100"
    elif(ins=="j"):
        code="1101"
    elif(ins=="xor"):
        code="1110"
    elif(ins=="mov"):
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
        code="010"
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
	code+=instruction(data[0])
	code+=offset(data[1], data[0])
	print code
	return code

def ldstbr_func(data):
	code=""
	code+=instruction(data[0])
	code+=address(data[2])
	code+=address(data[1])
	code+=offset(data[3], data[0])
	print code
	return code

def data_processing_func(data):
	code=""
	code+=instruction(data[0])
	code+=address(data[2])
	code+=address(data[3])
	code+=address(data[1])
	code+=offset(0, data[0])
	print code
	return code

def read_file(fname=""):
	if(fname==""):
		fname=raw_input("Name of instruction file: ")
		fname_new=fname.split(".")
		fname2=fname_new[0]+".bin"

		f1=open(fname, "r")
		rd=f1.read()
		rd=rd.lower()
		f1.close()
	else:
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

		if(data[0]=="j"):
			put=jump_func(data)
		elif(data[0] in ldstbr_list):
			put=ldstbr_func(data)
		else:
			put=data_processing_func(data)

		f2=open(fname2, "a")
		f2.write(put)
		f2.write("\n")
		f2.close
	print "Compilation complete!"
	return 0

def make_file():

	fname=raw_input("Save instruction file as (with extension): ")

	f=open(fname, "w")
	f.close()

	end="0"
	while(end=="0"):
		put=""
		comp=""
		ins=raw_input("Instruction: ")
		put+=ins+" "
		if(ins=="j"):
			put+=raw_input("Offset Value: ")
			f1=open(fname, "a")
			f1.write(put)
			f1.write("\n")
			f1.close()
			end=raw_input("Press '0' to continue or 'Other button then press Enter' to exit: ")
		elif (ins in ldstbr_list):
			put+=raw_input("Destination (R0/R1/R2/R3 etc.): ")
			put+=" "
			put+=raw_input("Source (R0/R1/R2/R3 etc.): ")
			put+=" "
			put+=raw_input("Offset Value: ")
			f1=open(fname, "a")
			f1.write(put)
			f1.write("\n")
			f1.close()
			end=raw_input("Press '0' to continue or 'Other button then press Enter' to exit: ")
		else:
			put+=raw_input("Destination (R0/R1/R2/R3 etc.): ")
			put+=" "
			put+=raw_input("Source1 (R0/R1/R2/R3 etc.): ")
			put+=" "
			put+=raw_input("Source2 (R0/R1/R2/R3 etc.): ")
			f1=open(fname, "a")
			f1.write(put)
			f1.write("\n")
			f1.close()
			end=raw_input("Press '0' to continue or 'Other button then press Enter' to exit: ")
	
	comp=raw_input("Do you want to compile now? Y/n: ")
	if(comp.lower()=="y"):
		read_file(fname)
	else:
		return 0


if __name__=="__main__":
	select=input("1. Make instruction file then compile\n2. Read Instruction from a file\nPlease, select: ")
	if(select==1):
		make_file()
	else:
		read_file()

exit()    
