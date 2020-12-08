my_data= open("delhi.txt","w")
my_simla = open("simla.txt", "w") 
my_other= open("other.txt", "w")
my_file5 = open("question3.txt", 'r')
my_list = my_file5.readlines()
i=0
while i<len(my_list):
    if "delhi" in my_list[i]:
        my_data.write(my_list[i])
    elif "shimla" in my_list[i]:
        my_simla.write(my_list[i])
    else:
        my_other.write(my_list[i])
    i=i+1
my_data.close()
my_simla.close()
my_other.close()