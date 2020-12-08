banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i= 0
file_name = open("file_question3.txt","w")
while i<len(banks_list):
    file_name.write(banks_list[i])
    file_name.write("\n")
    i=i+1
file_name.close()
