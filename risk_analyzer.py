file_name = input("Enter file name : ")
file_size = int(input("enter file size : "))
entropy = input("Enter Entropy : (Low / High : )").lower()

source_trusted = input("Is this source trusted (Yes / No):").lower()

print("File name: ",file_name)
print("Size : ", file_size, "MB" )
print("Trusted source : ",source_trusted)

#if(file_size > 500):
#    if(source_trusted == "no"):
#        print("High Risk")
#    else:
#        print("Medim Risk")        
#else:
#    print("Low Risk")
risk_score = 0

if file_size > 500:
    risk_score += 1

if file_size == "no":
    risk_score += 2

if file_size == "high":
    risk_score += 2

if file_size >= 4:
    print("High Risk")

elif risk_score >= 2:
     print("Medium Risk")

else:
    print("Low Risk")




