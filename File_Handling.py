def rename_file():
    readfileandfolder()
    file_name = input("NEter name of your file:")
    
    
    
    
    option = int(input("Enter your choice:"))
    if option ==1:
        create_file()
        
    if option ==2:
        read_file()
    
    if option ==3:
        update_file()
        
    if option ==4:
        delete_file()
        
    if option ==5:
        reanme_file()
        
    if option ==0:
        break
        
    