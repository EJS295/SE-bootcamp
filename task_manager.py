

###########################Login Section##########################################################



#open user.txt for reading 
f = open('user.txt', 'r')



#===============use a dictionary to store a list of usernames and passwords from the file =============#




#I learned how to create an empty dictionary object from
#https://www.geeksforgeeks.org/initialize-an-empty-dictionary-in-python/

#create empty Dictionary 'login_dic'
login_dic = {}

# read line from file and each line is stored as a String in user_info
user_info = f.readline()

#until reading empty line
while user_info  != "" :

    
    
    # Split user_info where there is comma and space.
    user_info_list = user_info.split(', ')


    #user_info_list[0] = user_name
    user_name = user_info_list[0]

    #user_info_list[1] = user_password
    user_password = user_info_list[1]

    #remove '\n' from user_password
    user_password = user_password.strip('\n')
    
    #add user information to Dictionary'login_dic'
    login_dic.update({user_name : user_password})

    # read next line from file and store as a String in user_info
    user_info = f.readline()




#===============user login =========================#


#ask the user to enter their user name and store in String 'entered_user_name'
entered_user_name = input("Please enter your username. : ")


#use while loop to validate user name and password.



#I learned to check if key exists in dictionary
#from https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp


#I learned to use while false
#from https://stackoverflow.com/questions/22377668/python-while-false-loop


#until the user enters the rignt user name
while not entered_user_name in login_dic :

    print("The username you entered does not exist.")
    #ask the user to enter their user name again
    entered_user_name = input("Please enter your username. : ")


#ask the user to enter password
entered_password = input("Please enter password : ")

#until the user enters the right password
while not entered_password in login_dic.values() :
    
    print("The password you entered is incorrect.")
    #ask the user to enter password again
    entered_password = input("Please enter password : ")






#close file 'user.txt'
f.close()



#===============menu =========================#


# menu for admin only #

if entered_user_name == "admin" :


    #presenting the menu to the user and the user enters their choice
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
s - View statistics 
e - Exit
: ''')

   # the user input is coneverted to lower case.
    menu = menu.lower()



    #if the user want to register a new user
    if menu == 'r':

        #open file 'user.txt' to add a new user
        fr = open('user.txt', 'a')

        #ask the user to enter a username that they want to register and store it to string 'new_user_name'
        new_user_name = input("Please enter a username that you want to register. : ")

        #ask the user to enter password  and store it to string 'new_password'
        new_password = input("Please enter password. : ")

        #ask the user to re-enter password and store it to string 'confirmed_password'
        confirmed_password = input("Please enter password again: ")
        


        #until new_password and confirmed_password are same
        while  new_password != confirmed_password : 
            
            print ("Passwords do not match.")

            #ask the user to enter password again
            confirmed_password = input("Please enter password again. : ")
            
            
        #add new user's information in user.txt
        fr.write("\n" + new_user_name + ", " + new_password)

        #close file 'user.txt'
        fr.close()




    #if the user want to add a task
    elif menu == 'a':

        #open file 'tasks.txt' to add a task
        fa = open('tasks.txt', 'a')
      

        #I learned how to ge a string format of the current date from
        #https://stackoverflow.com/questions/3316882/how-do-i-get-a-string-format-of-the-current-date-time-in-python
        
        #inport datetime
        from datetime import datetime
        
        #current date and time
        now = datetime.now() 

        #I learned how to return short name of the month from
        #https://pynative.com/python-get-month-name-from-number/
        today = now.strftime("%d %b %Y")
        
        #ask the user to enter a username who the task is assigned to and store it to string 'user_name_a'
        user_name_a= input("Please enter a username whom the task is assigned to. : ")

        #ask the user to enter a title and store it to string 'title_task_a'
        title_task_a = input("Please type a task title. : ")

        #ask the user to enter description of the task and store it to string 'description_task_a'
        description_task_a = input("Please type the description of the task. : ")

        #ask the user to enter due date and store it to string 'due_date'
        due_date = input("When is the due date? : ")


        #add task information in tasks.txt
        fa.write("\n" + user_name_a + ", " + title_task_a + ", " + description_task_a + ", " + today + ", " + due_date + ", " + "No")

        #close file 'tasks.txt'
        fa.close()
        
       


    #if the user wants to view all the tasks 
    elif menu == 'va':


        #open tasks.txt for reading 
        fva = open('tasks.txt', 'r')
    

        # read line from file and each line is stored as a String in tasks
        tasks = fva.readline()

        # Split tasks where there is comma and space.
        tasks_list = tasks.split(", ")
        

        #until new line is blank line
        while len(tasks_list) > 2 :
        
            #store all the elements in List 'tasks_list' to each string

            #store user name in user_name_t
            user_name_t = tasks_list[0]
            
            #store task title in title_t
            title_t = tasks_list[1]

            #store task description in description_t
            description_t = tasks_list[2]

            #store current date in today_t
            today_t = tasks_list[3]

            #store due date in due_date_t
            due_date_t = tasks_list[4]

            #store complete condition in complete_t

            complete_t = tasks_list[5]

            #strip '\n' from complete_t to avoid printing an empty line
            complete_t = complete_t.strip('\n')

            #print all the information of each task
            print("__________________________________________________________________________________________\n")

            print(f"Task:                {title_t}")
            print(f"Assigned to:         {user_name_t}")
            print(f"Date assigned:       {today_t}")
            print(f"Due date:            {due_date_t}")
            print(f"Task Complete?:      {complete_t}")
            print(f"Task description: \n\t{description_t}\n")

            print("__________________________________________________________________________________________\n")


            # read next line from file and  store as a String in tasks
            tasks = fva.readline()

            # Split tasks where there is comma and space.
            tasks_list = tasks.split(", ")
           
        #close file 'tasks.txt'
        fva.close()




    #if the user wants to view only their tasks 
    elif menu.lower() == 'vm':
        

        #open tasks.txt for reading 
        fvm = open('tasks.txt', 'r')
    

        #read line from file and each line is stored as a String in my_tasks
        my_tasks = fvm.readline()

        #Split tasks where there is comma and space
        my_tasks_list = my_tasks.split(", ")
        


        #until new line is blank line
        while len(my_tasks_list) > 2 :
            
            #if the entered user name & user name in the file are same
            if  entered_user_name == my_tasks_list[0] :


                #store user name in my_name
                my_name = my_tasks_list[0]

                #store task title in my_title
                my_title = my_tasks_list[1]

                #store task description in my_description
                my_description = my_tasks_list[2]

                #store current date in my_today
                my_today = my_tasks_list[3]

                #store due date in my_due_date
                my_due_date = my_tasks_list[4]

                #store complete condition in my_complete
                my_complete = my_tasks_list[5]

                #strip '\n' from my_complete to avoid printing an empty line
                my_complete = my_complete.strip('\n')



                #print all the information of each task
                print("__________________________________________________________________________________________\n")

                print(f"Task:                {title_t}")
                print(f"Assigned to:         {user_name_t}")
                print(f"Date assigned:       {today_t}")
                print(f"Due date:            {due_date_t}")
                print(f"Task Complete?:      {complete_t}")
                print(f"Task description: \n\t{description_t}\n")

                print("__________________________________________________________________________________________\n")

                # read next line from file and  store as a String in my_tasks
                my_tasks = fvm.readline()

                #Split tasks where there is comma and space
                my_tasks_list = my_tasks.split(", ")

            else : #if the entered user name & user name in the file are different

                # read next line from file and  store as a String in my_tasks
                my_tasks = fvm.readline()

                #Split tasks where there is comma and space
                my_tasks_list = my_tasks.split(", ")
        
        
           
        #close file 'tasks.txt'
        fvm.close()




    #if admin wants to see stastics
    elif menu == 's' :


        #=====count the number of users==========#


        #open user.txt for reading 
        fs = open('user.txt', 'r')

        user_number = 0

        # read line from file and each line is stored as a String in user_num
        user_num = fs.readline()
        # Split user_num where there is comma and space.
        user_num_list = user_num.split(', ')

        #until reading empty line
        while len(user_num_list) == 2 :

            user_number += 1
        
            # read line from file and each line is stored as a String in user_num
            user_num = fs.readline()
            # Split user_num where there is comma and space.
            user_num_list = user_num.split(', ')
            
        #close user.txt
        fs.close()

        #=====count the number of tasks==========#



        #open tasks.txt for reading 
        fs_t = open('tasks.txt', 'r')
    

        #read line from file and each line is stored as a String in task_num_s
        task_num_s = fs_t.readline()

        #Split task_num_s where there is comma and space
        task_num_s_list = task_num_s.split(", ")
        
        task_numbers = 0


        #until new line is blank line
        while len(task_num_s_list) > 2 :
            
            task_numbers += 1

             #read line from file and each line is stored as a String in task_num_s
            task_num_s = fs_t.readline()

             #Split task_num_s where there is comma and space
            task_num_s_list = task_num_s.split(", ")
        
      
        
           
        #close file 'tasks.txt'
        fs_t.close()
    
        print(f"The total number of users : {user_number}\n")
        print(f"The total number of tasks : {task_numbers}")




    #if admin wants to exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()



    #if the user have made a wrong choice
    else:
        print("You have made a wrong choice, Please Try again")
        

# menu for all users except 'admin' #


else: # all users except 'admin'

    
    #presenting the menu to the user and the user enters their choice
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''')

   # the user input is coneverted to lower case.
    menu = menu.lower()



    #if the user want to add a task
    if menu == 'a':

        #open file 'tasks.txt' to add a task
        fa = open('tasks.txt', 'a')
      

        #I learned how to ge a string format of the current date from
        #https://stackoverflow.com/questions/3316882/how-do-i-get-a-string-format-of-the-current-date-time-in-python
        
        #inport datetime
        from datetime import datetime
        
        #current date and time
        now = datetime.now() 

        #I learned how to return short name of the month from
        #https://pynative.com/python-get-month-name-from-number/
        today = now.strftime("%d %b %Y")
        
        #ask the user to enter a username who the task is assigned to and store it to string 'user_name_a'
        user_name_a= input("Please enter a username whom the task is assigned to. : ")

        #ask the user to enter a title and store it to string 'title_task_a'
        title_task_a = input("Please type a task title. : ")

        #ask the user to enter description of the task and store it to string 'description_task_a'
        description_task_a = input("Please type the description of the task. : ")

        #ask the user to enter due date and store it to string 'due_date'
        due_date = input("When is the due date? : ")


        #add task information in tasks.txt
        fa.write("\n" + user_name_a + ", " + title_task_a + ", " + description_task_a + ", " + today + ", " + due_date + ", " + "No")

        #close file 'tasks.txt'
        fa.close()


       
    #if the user wants to view all the tasks 
    elif menu == 'va':


        #open tasks.txt for reading 
        fva = open('tasks.txt', 'r')
    

        # read line from file and each line is stored as a String in tasks
        tasks = fva.readline()

        # Split tasks where there is comma and space.
        tasks_list = tasks.split(", ")
        

        #until new line is blank line
        while len(tasks_list) > 2 :
        
            #store all the elements in List 'tasks_list' to each string

            #store user name in user_name_t
            user_name_t = tasks_list[0]
            
            #store task title in title_t
            title_t = tasks_list[1]

            #store task description in description_t
            description_t = tasks_list[2]

            #store current date in today_t
            today_t = tasks_list[3]

            #store due date in due_date_t
            due_date_t = tasks_list[4]

            #store complete condition in complete_t

            complete_t = tasks_list[5]

            #strip '\n' from complete_t to avoid printing an empty line
            complete_t = complete_t.strip('\n')

            #print all the information of each task
            print("__________________________________________________________________________________________\n")

            print(f"Task:                {title_t}")
            print(f"Assigned to:         {user_name_t}")
            print(f"Date assigned:       {today_t}")
            print(f"Due date:            {due_date_t}")
            print(f"Task Complete?:      {complete_t}")
            print(f"Task description: \n\t{description_t}\n")

            print("__________________________________________________________________________________________\n")


            # read next line from file and  store as a String in tasks
            tasks = fva.readline()

            # Split tasks where there is comma and space.
            tasks_list = tasks.split(", ")
           
        #close file 'tasks.txt'
        fva.close()




    #if the user wants to view only their tasks 
    elif menu.lower() == 'vm':
        

        #open tasks.txt for reading 
        fvm = open('tasks.txt', 'r')
    

        #read line from file and each line is stored as a String in my_tasks
        my_tasks = fvm.readline()

        #Split tasks where there is comma and space
        my_tasks_list = my_tasks.split(", ")
        


        #until new line is blank line
        while len(my_tasks_list) > 2 :
            
            #if the entered user name & user name in the file are same
            if  entered_user_name == my_tasks_list[0] :


                #store user name in my_name
                my_name = my_tasks_list[0]

                #store task title in my_title
                my_title = my_tasks_list[1]

                #store task description in my_description
                my_description = my_tasks_list[2]

                #store current date in my_today
                my_today = my_tasks_list[3]

                #store due date in my_due_date
                my_due_date = my_tasks_list[4]

                #store complete condition in my_complete
                my_complete = my_tasks_list[5]

                #strip '\n' from my_complete to avoid printing an empty line
                my_complete = my_complete.strip('\n')



                #print all the information of each task
                print("__________________________________________________________________________________________\n")

                print(f"Task:                {title_t}")
                print(f"Assigned to:         {user_name_t}")
                print(f"Date assigned:       {today_t}")
                print(f"Due date:            {due_date_t}")
                print(f"Task Complete?:      {complete_t}")
                print(f"Task description: \n\t{description_t}\n")

                print("__________________________________________________________________________________________\n")

                # read next line from file and  store as a String in my_tasks
                my_tasks = fvm.readline()

                #Split tasks where there is comma and space
                my_tasks_list = my_tasks.split(", ")

            else : #if the entered user name & user name in the file are different

                # read next line from file and  store as a String in my_tasks
                my_tasks = fvm.readline()

                #Split tasks where there is comma and space
                my_tasks_list = my_tasks.split(", ")
        
        
           
        #close file 'tasks.txt'
        fvm.close()





    #if the user wants to exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()




    #if the user have made a wrong choice
    else:
        print("You have made a wrong choice, Please Try again")
        





