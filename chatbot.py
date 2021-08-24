print("hello world\n\nHei")

spørsmål = 99 

while spørsmål!=0:

    
    print("noe du kan spørre meg om\n0--du lurer ikke på noe\n1--Hva jeg heter\n2--hvor gammel jeg er\n3--hobbyene mine\n4--forskjellig teknologi jeg har drevet med")
    try: 
        spørsmål = int(input("Hva lurer du på ?:"))
        print("forsto du?\n")
    except ValueError: 
        print("skriv et tall ikke bokstaver\n")

    if spørsmål == 1: 
        print("Jeg heter Henrik Handberg\n") 
    elif spørsmål == 2: 
        print("Jeg er 16 år gammel\n")
    elif spørsmål == 3:
        print("jeg driver med bodybuilding\n")
    elif spørsmål == 4: 
        print(" jeg har drevet med html css python visual studio og windows server 2012 r2\n")
    