
from datetime import datetime
import datetime


#########################define functions#########################################

#define a function that is called when the user selects 'r' to register a user
def reg_user(entered_user_name) :


    #open file 'user.txt' to add a new user
    fr = open('user.txt', 'r+')

    #create empty Dictionary 'users'
    users = {}
    # read line from file and each line is stored as a String in user_info
    user_info = fr.readline()

    #until reading empty line
    while user_info  != "" :
       
        user_info_list = user_info.split(', ')
        user_name = user_info_list[0]
        user_password = user_info_list[1]
        user_password = user_password.strip('\n')
        #add user information to Dictionary'users'
        users.update({user_name : user_password})
        user_info = fr.readline()

    #until the user enters user_name which is not already in 'users.txt'
    while entered_user_name in users :

        print("The username you entered already exists.")
        entered_user_name = input("Please enter a username you want to register. : ")

    new_password = input("Please enter password. : ")
    confirmed_password = input("Please enter password again: ")
        
    #until new_password and confirmed_password are same
    while  new_password != confirmed_password : 
            
        print ("Passwords do not match.")
        confirmed_password = input("Please enter password again. : ")
            
    #add new user's information in user.txt
    fr.write("\n" + entered_user_name + ", " + new_password)
    fr.close()
    #call a function call_main
    call_main()

#define a function that is called when the user selects 'a' to add a task
def add_task() :

    #open file 'tasks.txt' to add a task
    fa = open('tasks.txt', 'a')
    from datetime import datetime
    #current date and time
    now = datetime.now() 
    today = now.strftime("%d %b %Y")
    user_name_a= input("Please enter a username whom the task is assigned to. : ")
    title_task_a = input("Please type a task title. : ")
    description_task_a = input("Please type the description of the task. : ")
    due_date = input("Please enter the due date [Day Month abbreviation Year with spaces] ex: 7 Mar 2023     : ")

    #add task information in tasks.txt
    fa.write("\n"+user_name_a + ", " + title_task_a + ", " + description_task_a + ", " + today + ", " + due_date + ", " + "No")
    fa.close()
    call_main()

#define a function that is called when the user selects 'va' to view all the tasks listed in 'tasks.txt'
def view_all():

    #open tasks.txt for reading 
    fva = open('tasks.txt', 'r+')
    tasks = fva.readline()
    # Split tasks where there is comma and space.
    tasks_list = tasks.split(", ")

    #until new line is blank line
    while len(tasks_list) > 2 :

        user_name_t = tasks_list[0]
        title_t = tasks_list[1]
        description_t = tasks_list[2]
        today_t = tasks_list[3]
        due_date_t = tasks_list[4]
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

        tasks = fva.readline()
        tasks_list = tasks.split(", ")

    fva.close()
    call_main()


#define a function that is called when the user selects 'va' to view all the tasks listed in 'tasks.txt'
def view_mine (username_m) :
        
    fvm = open('tasks.txt', 'r')
    #create empty Dictionary 'vm_dic'
    vm_dic ={}
    my_tasks = fvm.readline()
    my_tasks_list = my_tasks.split(", ")    
    task_num = 0

    #until new line is blank line
    while len(my_tasks_list) > 2 :
            
            #if the entered user name & user name in the file are same
        if  username_m == my_tasks_list[0] :

            task_num += 1 
            my_name = my_tasks_list[0]
            my_title = my_tasks_list[1]
            my_description = my_tasks_list[2]
            my_today = my_tasks_list[3]
            my_due_date = my_tasks_list[4]
            my_complete = my_tasks_list[5]
            my_complete = my_complete.strip('\n')

            vm_dic.update({task_num : my_tasks_list})
            
            print("__________________________________________________________________________________________\n")
            
            print(f"Task No. {task_num}")
            print(f"Task:                {my_title}")
            print(f"Assigned to:         {my_name}")
            print(f"Date assigned:       {my_today}")
            print(f"Due date:            {my_due_date}")
            print(f"Task Complete?:      {my_complete}")
            print(f"Task description: \n\t{my_description}\n")

            print("__________________________________________________________________________________________\n")

            my_tasks = fvm.readline()
            my_tasks_list = my_tasks.split(", ")

        else : #if the entered user name & user name in the file are different
            my_tasks = fvm.readline()
            my_tasks_list = my_tasks.split(", ")
    
    fvm.close()
    #open tasks.txt for reading 
    fvm_e= open('tasks.txt', 'r')
    fvm_e.seek(0)
    #open output.txt for writing 
    fo = open('output.txt', 'w+')
    # read line from file and each line is stored as a String in my_tasks_e
    my_tasks_e = fvm_e.readline()
    my_tasks_e_list = my_tasks_e.split(", ")

    #store 'yes' or 'no' in task_complete
    task_complete = my_tasks_e_list[5]
    task_complete = task_complete.strip('\n')
    task_complete = task_complete.lower()

    my_task_num = 1

    entered_task_num = input('''Select a Task number you want to edit
or enter -1 to return to the main menu 
: ''')
    entered_task_num_1 = int(entered_task_num)

    try :
        #if the user enters a positive number
        if entered_task_num_1 > 0 :

            option = input('''Select one of the following options below
c - mark the task as complete
e - edit the task
: ''')

            option.lower()
        #if the user enters '-1'
        else :

            call_main()

    except ValueError:

        print("You did not enter the right number.")


    #until new line is blank line
    while len(my_tasks_e_list) > 2 and entered_task_num != '-1' :
        #check the task has been already completed
        if option == 'e' and username_m == my_tasks_e_list[0] and int(entered_task_num) == my_task_num :

            task_complete = my_tasks_e_list[5]
            task_complete = task_complete.strip('\n')
            task_complete = task_complete.lower()


            if task_complete == 'yes': #if the task has been completed

                print("The task has been completed already. You can not edit it anymore.\n\n")
                
                break

            else: #if the task has not been completed


                edit_option = input('''Select one of the following options below
n - edit the username of the person to whom the task is assigned 
d - edit the due date of the task 
: ''')
                edit_option.lower()
                break

        #if the task read from the line is not the task that the user wants to edit
        elif option == 'e' and username_m == my_tasks_e_list[0] and int(entered_task_num) != my_task_num  :

            my_tasks_e = fvm_e.readline()
            my_tasks_e_list = my_tasks_e.split(", ")
            my_task_num += 1
        #if the username read from the line is not same with the current user
        elif option == 'e' and username_m != my_tasks_e_list[0] :

            my_tasks_e = fvm_e.readline()
            my_tasks_e_list = my_tasks_e.split(", ")

        else:
            break

    fvm_e.close()

    #open tasks.txt for reading 
    fvm = open('tasks.txt', 'r')
    fvm.seek(0)
    my_tasks_r = fvm.readline()
    my_tasks_r_list = my_tasks_r.split(", ")
    task_complete_condition = my_tasks_r_list[5]
    task_complete_condition = task_complete_condition.strip('\n')
    task_complete_condition = task_complete_condition.lower()

    my_task_num = 1


    #until new line is blank line
    while len(my_tasks_r_list) > 2 and entered_task_num != '-1' :
        
        #if the user wants to mark the task as complete & the task read from the line is the right task to edit
        if option== 'c' and username_m == my_tasks_r_list[0] and int(entered_task_num) == my_task_num : 

            #change 'No' to 'Yes'
            my_tasks_r_list[5] = "Yes\n"
            #join the list 'my_tasks_r_list' to string 'changed_line'
            changed_line = ", ".join(my_tasks_r_list)
            #write 'changed_line' into 'output.txt'file
            fo.write(changed_line)

            my_tasks_r = fvm.readline()
            my_tasks_r_list = my_tasks_r.split(", ")
            my_task_num += 1

        #if the task read from the line is not the right task to edit
        elif option == 'c' and username_m == my_tasks_r_list[0] and int(entered_task_num) != my_task_num :
            
            my_task_num += 1
            #write the line read from the line into 'output.txt'file
            fo.write(my_tasks_r)
            my_tasks_r = fvm.readline()
            my_tasks_r_list = my_tasks_r.split(", ")

        #if the username read from the line is not same with the current user
        elif option == 'c' and username_m != my_tasks_r_list[0] and int(entered_task_num) != my_task_num :
            
            my_task_num += 1
            fo.write(my_tasks_r)
            my_tasks_r = fvm.readline()
            my_tasks_r_list = my_tasks_r.split(", ")
            
        #if it is the right task to edit
        elif option == 'e' and username_m == my_tasks_r_list[0] and int(entered_task_num) == my_task_num :

            task_complete_condition = my_tasks_r_list[5]
            task_complete_condition = task_complete_condition.strip('\n')
            task_complete_condition = task_complete_condition.lower()

            #if the task is already completed, do not ask the user to choose 'edit_option'
            if task_complete_condition == 'yes':

                my_task_num += 1
                fo.write(my_tasks_r)
                my_tasks_r = fvm.readline()
                my_tasks_r_list = my_tasks_r.split(", ")


            else: #if the task is not completed, ask the user to choose 'edit_option'

                #if the user wants to enter the new name of the person to whom the task in assigned
                if  edit_option == 'n' :

                    changed_name = input ("Please enter the new name of the person to whom the task is assigned.:   ")
                    #store the new name into the list 
                    my_tasks_r_list[0] = changed_name
                    changed_line = ", ".join(my_tasks_r_list)
                    #write the edited information into file
                    fo.write(changed_line)
                    my_tasks_r = fvm.readline()
                    my_tasks_r_list = my_tasks_r.split(", ")
                    my_task_num += 1

                #if the user wants to edit the due date
                elif edit_option == 'd' :

                    changed_date = input ("Please enter the new due date [Day Month abbreviation Year with spaces] ex: 7 Mar 2023     :")
                    #store the new due date into the list 
                    my_tasks_r_list[4] = changed_date
                    changed_line = ", ".join(my_tasks_r_list)
                    #write the edited information into file
                    fo.write(changed_line)
                    my_tasks_r = fvm.readline()
                    my_tasks_r_list = my_tasks_r.split(", ")
                    my_task_num += 1
     
        #if it is not the right task
        elif option == 'e' and username_m == my_tasks_r_list[0] and int(entered_task_num) != my_task_num  :

            my_task_num += 1
            fo.write(my_tasks_r)
            my_tasks_r = fvm.readline()
            my_tasks_r_list = my_tasks_r.split(", ")
        #if it is not the right username
        elif option == 'e' and username_m != my_tasks_r_list[0] and int(entered_task_num) != my_task_num : 

            my_task_num += 1
            fo.write(my_tasks_r)
            my_tasks_r = fvm.readline()
            my_tasks_r_list = my_tasks_r.split(", ")
           
    fo.close()
    fvm.close()

    fvm_w = open('tasks.txt', 'w+')
    fo_r = open('output.txt', 'r')
    #read all lines from 'output.txt'
    lines = fo_r.readlines()
    #write all lines to 'tasks.txt'
    fvm_w.writelines(lines)

    fvm_w.close()
    fo_r.close()
    call_main()


#define a function that is called when the user selects 'gr' to generate reports 'user_overview.txt' & 'task_overview.txt'
def generate_reports():

    from datetime import datetime
    import datetime

    fgr = open('tasks.txt', 'r')
    fgr_user = open('user_overview.txt','w+')
    tasks_gr = fgr.readline()
    tasks_gr_list = tasks_gr.split(", ")

    #generate an empty ditionary which will store information about each user
    each_user_count= {}

    total_num = 0
    total_completed_num = 0
    total_uncompleted_num = 0
    total_overdue_num = 0

    d = datetime.datetime.today()
    user_name_gr = tasks_gr_list[0]

    from datetime import datetime
    
    while len(tasks_gr_list) > 2 :

        total_num += 1

        #username : user_name_gr
        user_name_gr = tasks_gr_list[0]

        complete_gr = tasks_gr_list[5]
        complete_gr = complete_gr.strip('\n')
        complete_gr = complete_gr.lower()

        due_date_gr = tasks_gr_list[4] 
        #I learned how to convert string time to number
        #https://java2blog.com/convert-month-name-to-number-python/#:~:text=The%20month%20name%20can%20be,to%20the%20strptime()%20function.
        date_object = datetime.strptime(due_date_gr, "%d %b %Y")

        #if username is in a dictionary 'each_user_count'
        if user_name_gr not in  each_user_count :#if username is not in a dictionary 

            each_user_count.update({user_name_gr : [1,0,0,0]})
            #each_user_count[user_name_gr][0] : The total number of tasks assigned to that user
            #each_user_count[user_name_gr][1] :The total number of tasks assigned to that user that have been completed
            #each_user_count[user_name_gr][2] : The total number of tasks assigned to that user that have not been completed
            #each_user_count[user_name_gr][3] : The total number of tasks asssinged to that user that are overdue


            if complete_gr == 'yes':
                each_user_count[user_name_gr][1] += 1

            elif complete_gr == 'no' :
                each_user_count[user_name_gr][2] += 1

                if date_object < d :
                    each_user_count[user_name_gr][3] += 1

        else: #if user_name_gr is in a dictionary

             #if the task is completed
            if complete_gr == 'yes':
                
                each_user_count[user_name_gr][0] += 1
                each_user_count[user_name_gr][1] += 1

            elif complete_gr == 'no' :
                each_user_count[user_name_gr][0] += 1
                each_user_count[user_name_gr][2] += 1

                if date_object < d : #if it is overdue
                    each_user_count[user_name_gr][3] += 1

        
        tasks_gr = fgr.readline()
        tasks_gr_list = tasks_gr.split(", ")

    
    #write user_overview report
    for name in each_user_count.keys() :

        fgr_user.write(f"=======   {name} overview ======= \n")
        fgr_user.write(f"The total number of tasks assigned to {name} :  {each_user_count[name][0]}\n")

        total_percentage = each_user_count[name][0] / total_num * 100
        total_percentage = int(total_percentage)
        fgr_user.write(f"The percentage of the total number of tasks that have been assigned to  {name} : {total_percentage}%\n")

        complete_percentage = each_user_count[name][1] / each_user_count[name][0] * 100
        complete_percentage = int(complete_percentage)
        fgr_user.write(f"The percentage of the tasks assigned to {name} that have been completed: {complete_percentage}% \n")


        not_percentage = each_user_count[name][2] / each_user_count[name][0] * 100
        not_percentage = int(not_percentage)
        fgr_user.write(f"The percentage of the tasks assigned to {name} that must still be completed: {not_percentage}% \n")


        over_percentage = each_user_count[name][3] / each_user_count[name][0] * 100
        over_percentage = int(over_percentage)
        fgr_user.write(f"The percentage of the tasks assigned to  {name} that have not yet been completed and are overdue : {over_percentage}%\n")

    fgr_user.close()

    #write task_overview report
    for name in each_user_count.keys() :

        total_completed_num +=each_user_count[name][1]
        total_uncompleted_num += each_user_count[name][2]
        total_overdue_num += each_user_count[name][3]


    fgr_tasks = open('task_overview.txt','w+')
    fgr_tasks.write(f"======= task overview ======= \n")
    fgr_tasks.write(f"The total number of tasks : {total_num} \n")
    fgr_tasks.write(f"The total number of completed tasks : {total_completed_num} \n")
    fgr_tasks.write(f"The total number of uncompleted tasks : {total_uncompleted_num} \n")
    fgr_tasks.write(f"The total number of uncompleted tasks and overdue : {total_overdue_num} \n")

    fgr_tasks.close()

    

    fgr.close()

#define a function that is called when the user selects 'ds' to display statistics
def display_statistics() :


    fgr_user_print = open('user_overview.txt','w+')
    fgr_tasks_print = open('task_overview.txt','w+')
    fgr_user_print.seek(0)
    fgr_tasks_print.seek(0)

    user_overview = fgr_user_print.readline()

    #if the user has not selected to generate reports
    if user_overview == "" :
        #call generate_reports()
        generate_reports()
        fgr_user_print.seek(0)
        fgr_tasks_print.seek(0)

        #read line from 'user_overview.txt' 
        user_overview = fgr_user_print.readline()

        #until the line is blank line, print and read the next line
        while user_overview != "" :
            print(user_overview)
            user_overview = fgr_user_print.readline()

        #read line from 'task_overview.txt' 
        tasks_overview = fgr_tasks_print.readline()

        #until the line is blank line, print and read the next line
        while tasks_overview != "" :
            print(tasks_overview)
            tasks_overview = fgr_tasks_print.readline()

    else :    #if the user has already selected to generate reports

        while user_overview != "" :
            print(user_overview)
            user_overview = fgr_user_print.readline()


        tasks_overview = fgr_tasks_print.readline()
    
        while tasks_overview != "" :
            print(tasks_overview)
            tasks_overview = fgr_tasks_print.readline()


    fgr_user_print.close()
    fgr_tasks_print.close()
    call_main()




###########################Login Section##########################################################

#open user.txt for reading 
f = open('user.txt', 'r')

#create empty Dictionary 'login_dic'
login_dic = {}

# read line from file and each line is stored as a String in user_info
dic_user_info = f.readline()

#until reading empty line
while dic_user_info  != "" :
    
    # Split user_info where there is comma and space.
    dic_user_info_list = dic_user_info.split(', ')
    dic_user_name = dic_user_info_list[0]
    dic_user_password = dic_user_info_list[1]
    dic_user_password = dic_user_password.strip('\n')
    #add user information to Dictionary'login_dic'
    login_dic.update({dic_user_name : dic_user_password})

    # read next line from file and store as a String in user_info
    dic_user_info = f.readline()






#===============user login =========================#

print("Welcome")
#ask the user to enter their user name and store in String 'entered_user_name'
login_user_name = input("Please enter your username. : ")

#until the user enters the rignt user name
while not login_user_name in login_dic :

    print("The username you entered does not exist.")
    #ask the user to enter their user name again
    login_user_name = input("Please enter your username. : ")

#ask the user to enter password
login_password = input("Please enter password : ")

#until the user enters the right password
while not login_password in login_dic.values() :
    
    print("The password you entered is incorrect.")
    #ask the user to enter password again
    login_password = input("Please enter password : ")

#close file 'user.txt'
f.close()

#===============menu =========================#

def call_main() :

    # menu for admin only #
    if login_user_name == "admin" :


    #presenting the menu to the user and the user enters their choice
        menu = input('''Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics 
e - Exit
: ''')

   # the user input is coneverted to lower case.
        menu = menu.lower()



    #if the user want to register a new user
        if menu == 'r':

            new_user_name = input("Please enter a username that you want to register. : ")

            reg_user(new_user_name)

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':

            view_mine(login_user_name)

        elif menu == 'gr' :
            generate_reports()

        elif menu == 'ds' :
            display_statistics()

        elif menu == 'e' :
            exit

        else :

            print("You did not choose the right option.")

            menu = input('''Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports # new option#
ds - Ddisplay statistics 
e - Exit
: ''')

   # the user input is coneverted to lower case.
            menu = menu.lower()

    else : # menu for the other users 


    #presenting the menu to the user and the user enters their choice
        menu = input('''Select one of the following Options below:
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit
: ''')

        menu = menu.lower()

        if menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':

            view_mine(login_user_name)

        elif menu == 'e' :
            exit

        else :

            print("You did not choose the right option.")

            menu = input('''Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports # new option#
ds - Ddisplay statistics 
e - Exit
: ''')
            menu = menu.lower()



call_main()





