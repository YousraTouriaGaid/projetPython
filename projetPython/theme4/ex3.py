digit = {
   '0': [" _ ",
         "| |",
         "|_|"],
   '1': [" _ ",
         "  |",
         "  |"],  
   '.': ["   ",
         "   ",
         " . "]
   
    
}

chiffre =input("entrer un chifre de 0 a 9")
#print (digit[chiffre])
for i in digit[chiffre]:
   # for i in digit[chiffre]:
        print(i)