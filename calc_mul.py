#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):
                a=float(ai)
                b=float(bi)

                if not a.is_integer() or not b.is_integer():          #小数点以下値がある場合false
                        valid=False
                
#               if 0<a and a<b and b<1000: 　　　変更前
                elif 0<a<1000  and 0<b<1000:             #変更後
                        valid=True

                
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
