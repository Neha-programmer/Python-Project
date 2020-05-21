dict={}
while True:
    print("---------Birthday App---------")
    print("1.Show Birthday")
    print("2.Add to Birthday List")
    print("3.Print list of Birthday")
    print("4.Exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        if(len(dict.keys()))==0:
            print("Nothing to show")
        else:
            name=input("Enter name to look for birthday")
            birthday=dict.get(name,"No data found")
            print(birthday)
    elif choice==2:
        name=input("Enter Friend's Name")
        date=input("Enter Birthdate")
        dict[name]=date
        print("Birthday Added")
    elif choice==3:
        if (len(dict.keys()))!=0:
            for i in dict:
                print(i,":",dict[i])
        else:
            print("Add Birthday to list")
    elif choice==4:
        break
    else:
        print("Choice a valid option")