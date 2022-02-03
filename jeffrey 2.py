nterms=int(input("enter a number:"))
n1,n2,=0,1
count=0
if nterms<=0:
    print("please enter a positive integer")
elif nterms==1:
    print("Fibonocci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonocci Sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
                  
