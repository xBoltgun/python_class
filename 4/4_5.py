def decode_bits(bits):
    bits = bits.strip('0')
    len0=0
    len1=0
    min0=9999999
    min1=9999999
    fre=bits[0]
    for i in bits:
        if i=='0' :
            if i==fre :
                len0+=1
            else:
                min1=min(min1,len1)
                len1=0
                len0+=1
        else:
            if i==fre :
                len1+=1
            else:
                min0=min(min0,len0)
                len0=0
                len1+=1
        fre=i
    len=min(min0,min1)
    if min0==9999999 and min1==9999999:
        if len0==0 and len1!=0:
            len=len1
        elif len1==0 and len0!=0:
            len=len0
        else:
            len=min(len0,len1)
        
    return bits[::len].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decode_morse(morseCode):
    morseCode=morseCode.replace('   ','#').replace('0','')
    temp=''
    ans=''
    for x in morseCode:
        if x!=' ' :
            if x=='#':
                if temp != '':
                    ans=ans+MORSE_CODE[temp]
                temp=''
                ans+=' '
            else:
                temp=temp+x
        else:
            #print(temp)
            if temp != '':
                ans=ans+MORSE_CODE[temp]
            temp=''
    if temp != '':
                ans=ans+MORSE_CODE[temp]
    return ans