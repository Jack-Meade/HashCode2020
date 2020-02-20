import random

def give_me_number(first_line):
    i = random.randint(0,int(first_line.split()[1]))+2
    if i %2 !=0:
        i+=1
    return i
#f_libraries_of_the_world.txt
#d_tough_choices.txt
with open("input/c_incunabula.txt",'r')as pp:
    all_lines=pp.read()
    all_lines=all_lines.split('\n')
    #print(all_lines)
    first_line = all_lines[0]
    #print(first_line)
    second_line = all_lines[1]
    #print(second_line)
    libs = all_lines[2:]
    #i = give_me_number(first_line)
    
    
    total_scanny_bois = 0
    sign_bois = {}
    out_bois ={}
    boob =first_line.split()[2]
    print(boob)
    while total_scanny_bois <= int(boob):
        i = give_me_number(first_line)
        #print(libs[i].split())
        #print(i)
        if libs[i][1]!=' ':
            total_scanny_bois += int(libs[i][1])
        if i not in sign_bois:
            sign_bois[i]=[libs[i][0],libs[i][1],libs[i][2]]
            out_bois[i]=[i,
                random.randint(1,int(libs[i].split()[0]))
                , libs[i+1].split()
                ]

        
    total_signed = len(sign_bois.keys())
    list_of_signed_up = list(sign_bois.keys())

with open("output/weewoo11.txt", "a+")as pp:
    #print(total_signed)
    #print(list_of_signed_up)
    #print(list_of_signed_up)
    print(libs[2])
    yeet=False
    pp.write(str(total_signed)+"\n")
    for i in list_of_signed_up:
        print(i)
        #print(out_bois[i][1])
        con = {}
        conney ={}
        k =0
        pp.write(str(out_bois[i][0]//2)+" "+str(out_bois[i][1])+"\n")

        while k < out_bois[i][1]:
            dude = random.randint(0,len(libs[i+1].split())-1)
            #print(dude)
            if dude not in conney:
                conney[dude]=True
                con[out_bois[i][2][dude]]=True
                k+=1
            if len(conney.keys()) == len(libs[i+1])-1:
                k += 10000000000000
       
        pp.write(' '.join(map(str,list(con.keys()))) + "\n")

            
        yeet=True

        
    

"""
        z=0
        while z < out_bois[i][1]-1:
            zr = random.randint(0,int(libs[i].split()[0])-1)
            
            if zr not in conney:
                conney[zr]=True
                #if zr < len(libs[i+1].split()):
                con[libs[i+1].split()[zr]]=True
                z +=1
   """  