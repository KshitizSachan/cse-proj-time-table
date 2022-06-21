from pickle import GET
from platform import node
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
"""
@Author = Karthik Avinash
"""
#_____________________________________________________________________________COURSES CLASS___________________________
class node_for_courses:
    def __init__(self,code,name,branch,semester,credit,faculty,faculty_id,theory,tutorial,lab):
            obj_for_linked_list_for_traversing_courses.insert(code,name,branch,semester,credit,faculty,faculty_id,theory,tutorial,lab)
        
class node_for_courses_for_all:
    def __init__(self,code,name,branch,semester,credit,faculty,faculty_id,theory,tutorial,lab):
        self.code=code
        self.name=name
        self.semester=semester
        obj_for_sem.insert(semester,branch)
        self.credit=credit
        self.faculty=faculty
        self.faculty_id=faculty_id
        obj_for_facultys.insert(faculty,faculty_id)
        self.branch=branch
    #Number of minutes
        self.theory=theory*60
        self.tutorial=tutorial*60
        self.lab=lab*60
        self.next=None

class linked_list_for_traversing_courses:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None

    def insert(self,code,name,branch,semester,credit,faculty,faculty_id,theory,tutorial,lab):
                new_node_to_insert_tutorial=None
                new_node_to_insert_lab=None
                new_node_to_insert_theory=None
                if lab:
                    new_node_to_insert_lab=node_for_courses_for_all(code+"_LAB",name,branch,branch+"_"+semester,credit,faculty,faculty_id,0,0,lab)
                if tutorial:
                    new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,faculty_id,0,tutorial,0)
                if theory:
                    
                    new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",name,branch,branch+"_"+semester,credit,faculty,faculty_id,theory,0,0)

                if branch=='CSE':
                    if self.head_for_CSE==None :
                        if lab:
                            self.head_for_CSE=new_node_to_insert_lab
                            if theory:
                                self.head_for_CSE.next=new_node_to_insert_theory
                                if tutorial:
                                    self.head_for_CSE.next.next=new_node_to_insert_tutorial
                            else:
                                if tutorial:
                                    self.head_for_CSE.next=new_node_to_insert_tutorial
                        else:
                            if theory:
                                self.head_for_CSE=new_node_to_insert_theory
                                new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",name,branch,branch+"_"+semester,credit,faculty,faculty_id,0,0,0)
                                if tutorial:
                                    self.head_for_CSE.next=new_node_to_insert_tutorial
                                    new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,faculty_id,0,0,0)
                            else:
                                if tutorial:
                                    self.head_for_CSE=new_node_to_insert_tutorial
                                    new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,faculty_id,0,0,0)
                        return

                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_theory
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab
                    
                if branch=='DSAI':
                    if self.head_for_DSAI==None :
                        if new_node_to_insert_lab:
                            self.head_for_DSAI=new_node_to_insert_lab
                            if new_node_to_insert_theory:
                                self.head_for_DSAI.next=new_node_to_insert_theory
                                if new_node_to_insert_tutorial:
                                    self.head_for_DSAI.next.next=new_node_to_insert_tutorial
                            else:
                                if new_node_to_insert_tutorial:
                                    self.head_for_DSAI.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_theory:
                                self.head_for_DSAI=new_node_to_insert_theory
                                if new_node_to_insert_tutorial:
                                    self.head_for_DSAI.next=new_node_to_insert_tutorial
                            else:
                                if new_node_to_insert_tutorial:
                                    self.head_for_DSAI=new_node_to_insert_tutorial
                        return

                    temp=self.head_for_DSAI
                    while temp.next:
                        temp=temp.next
                    if new_node_to_insert_lab:
                        temp.next=new_node_to_insert_lab
                        if new_node_to_insert_theory:
                            temp.next.next=new_node_to_insert_theory
                            if new_node_to_insert_tutorial:
                                temp.next.next.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_tutorial:
                                temp.next.next=new_node_to_insert_tutorial
                    else:
                        if new_node_to_insert_theory:
                            temp.next=new_node_to_insert_theory
                            if new_node_to_insert_tutorial:
                                temp.next.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_tutorial:
                                temp.next=new_node_to_insert_tutorial
                    return

                if branch=='ECE':
                    if self.head_for_ECE==None :
                        if new_node_to_insert_lab:
                            self.head_for_ECE=new_node_to_insert_lab
                            if new_node_to_insert_theory:
                                self.head_for_ECE.next=new_node_to_insert_theory
                                if new_node_to_insert_tutorial:
                                    self.head_for_ECE.next.next=new_node_to_insert_tutorial
                            else:
                                if new_node_to_insert_tutorial:
                                    self.head_for_ECE.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_theory:
                                self.head_for_ECE=new_node_to_insert_theory
                                if new_node_to_insert_tutorial:
                                    self.head_for_ECE.next=new_node_to_insert_tutorial
                            else:
                                if new_node_to_insert_tutorial:
                                    self.head_for_ECE=new_node_to_insert_tutorial
                        return

                    temp=self.head_for_ECE
                    while temp.next:
                        temp=temp.next
                    if new_node_to_insert_lab:
                        temp.next=new_node_to_insert_lab
                        if new_node_to_insert_theory:
                            temp.next.next=new_node_to_insert_theory
                            if new_node_to_insert_tutorial:
                                temp.next.next.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_tutorial:
                                temp.next.next=new_node_to_insert_tutorial
                    else:
                        if new_node_to_insert_theory:
                            temp.next=new_node_to_insert_theory
                            if new_node_to_insert_tutorial:
                                temp.next.next=new_node_to_insert_tutorial
                        else:
                            if new_node_to_insert_tutorial:
                                temp.next=new_node_to_insert_tutorial
                    return              

#_______________________________________________________________________________FACULTY CLASS_____________
class node_for_faculty_name:
    def __init__(self,f_name,id):
        self.faculty_name=f_name
        self.faculty_id=id
        self.next=None
        self.faculty_tt=[['Monday','*','*','*','*','*'],
                        ['Tuesday','*','*','*','*','*'],  
                        ['Wednesday','*','*','*','*','*'],
                        ['Thursday','*','*','*','*','*'],
                        ['Friday','*','*','*','*','*']]

class linked_list_for_faculty_name:
    def __init__(self):
        self.head_for_faculty_names=None
    
    def insert(self,f_name,id):
        new_node=node_for_faculty_name(f_name,id)
        if self.head_for_faculty_names==None:
            self.head_for_faculty_names=new_node
            return
        count=0
        temp=self.head_for_faculty_names
        while(temp):
            if temp.faculty_name==f_name:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_faculty_names
            while temp.next:
                temp=temp.next
            temp.next=new_node

#_____________________________________________________________________________SEMESTER CLASS___________
class node_for_semisters:
    def __init__(self,sem,branch):
        self.sem=sem
        self.branch=branch
        self.sem_tt=[['Monday1','*','*','*','*','*'],
                        ['Tuesday1','*','*','*','*','*'],  
                        ['Wednesday1','*','*','*','*','*'],
                        ['Thursday1','*','*','*','*','*'],
                        ['Friday1','*','*','*','*','*']]
        self.next=None

class linked_list_to_travese_semester():
    def __init__(self):
        self.head_for_semesters=None
    
    def insert(self,sem,branch):
        new_node=node_for_semisters(sem,branch)
        if self.head_for_semesters==None:
            self.head_for_semesters=new_node
            return
        count=0
        temp=self.head_for_semesters
        while(temp):
            if temp.sem==sem:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_semesters
            while(temp.next):
                temp=temp.next
            temp.next=new_node

#_________________________________________________________________________TRAVERSING FUNCTION____________
def plotting():
    for i in range(3):
        variable_for_sem_generalized_head=None
        if i==0:
            temp1=obj_for_linked_list_for_traversing_courses.head_for_CSE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
        if i==1:
            temp1=obj_for_linked_list_for_traversing_courses.head_for_DSAI
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
        if i==2:
            temp1=obj_for_linked_list_for_traversing_courses.head_for_ECE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            #Holding node.
        while temp1:
                time=0
                #Fetching faculty.
                temp2=obj_for_facultys.head_for_faculty_names
                while temp2:
                    if temp1.faculty==temp2.faculty_name:
                        break
                    temp2=temp2.next
                
                #Fetching semester.
                temp3=variable_for_sem_generalized_head
                while temp3:
                    if temp1.semester==temp3.sem:
                        break
                    temp3=temp3.next
                if temp1.code=='ENV_STUDY_TH': 
                    print('After traversing!')
                    print(temp2.faculty_name)
                    print(temp3.sem)
                #Changing timetable.
                if temp1.theory:
                    time=0
                    for _ in range(10):
                        for i in range(5):
                            for j in range(6):
                                if time>=temp1.theory:
                                    break
                                if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.theory:
                                    if j==2 or j==3 or j==5 or j==6 and time+60<=temp1.theory:
                                        temp2.faculty_tt[i][j]=temp1.semester
                                        temp3.sem_tt[i][j]=temp1.code
                                        time+=60
                                        break
                                    if time+90<=temp1.theory and (temp1.theory/60)%2!=0:
                                        time+=90
                                        temp2.faculty_tt[i][j]=temp1.semester
                                        temp3.sem_tt[i][j]=temp1.code
                                        break
                                if _>=3 and time+60<temp1.theory:
                                    if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*':
                                        temp2.faculty_tt[i][j]=temp1.semester
                                        temp3.sem_tt[i][j]=temp1.code
                                        if j==2 or j==3 or j==5 or j==6:
                                            time+=60
                                            break
                                        time+=90
                                        break
                                    
                elif temp1.tutorial:
                    time=0
                    for _ in range(10):    
                        for i in range(5):
                            for j in range(6):
                                if time>temp1.tutorial:
                                    break
                                if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.tutorial:
                                    if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester:
                                            break
                                    if j==2 or j==3 or j==5 or j==6 and time+60<=temp1.tutorial and time<temp1.tutorial:
                                        temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                        temp3.sem_tt[i][j]=temp1.code
                                        time+=60
                                        break
                                    
                                    if time+90<=temp1.tutorial and time<temp1.tutorial:
                                        time+=90
                                        temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                        temp3.sem_tt[i][j]=temp1.code
                                        break

                                if _>=3 and time+60<temp1.tutorial:
                                    if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.tutorial:
                                        temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                        temp3.sem_tt[i][j]=temp1.code
                                        if j==2 or j==3 or j==5 or j==6:
                                            time+=60
                                        else: time+=90
                                        break
                                    
                elif temp1.lab:
                    time=0
                    for _ in range(10):
                        for i in range(5):
                            for j in range(6):
                                if time>=temp1.lab:
                                    break
                                if _>=7 :
                                    if time+60<=temp1.lab and (j==2 or j==3 or j==5 or j==6):
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.lab:
                                            temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                            temp3.sem_tt[i][j]=temp1.code
                                            time+=60
                                            break
                                    elif time+90<=temp1.lab and (j==1 or j==4):
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.lab:
                                            temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                            temp3.sem_tt[i][j]=temp1.code
                                            time+=90
                                            break
                                        
                                else:
                                    if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]=='*' and time<temp1.lab:
                                        if j==2 and temp2.faculty_tt[i][j+1]==temp3.sem_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                            if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester:
                                                break
                                            temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp2.faculty_tt[i][j+1]=temp1.semester+"_LAB"
                                            temp3.sem_tt[i][j+1]=temp1.code
                                            time+=120
                                            break
                                        if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester:
                                            break
                                
                temp1=temp1.next

#_____________________________________________________________________PRINTING FACULTY TIMETABLE________
def printing_leactures_time_table():
    temp=obj_for_facultys.head_for_faculty_names
    print("\n\n")
    while(temp):
            print("Faculty Name : ",temp.faculty_name,"\nFaculty id : ",temp.faculty_id,"\n")
            print("%-15s%-15s%-15s%-15s%-15s%-15s"%("Day","9:00-10:30","10:45-11:45","11:45-12:45","1:45-3:15","3:15-4:15"))
            print("_______________________________________________________________________________________________________")
            for i in range(5):
                for j in range(6):
                    print("%-15s"%(temp.faculty_tt[i][j]),end="")
                print()
            print("\n\n")
            temp=temp.next

#___________________________________________________________________PRINTING SEMESTER TIME TABLES______
def printing_students_time_table():
    temp=obj_for_sem.head_for_semesters
    print("________________________________________________CSE BRANCH_____________________________________________\n")
    while(temp):
            print("Semester : ",temp.sem,"\nBranch : ",temp.branch)
            print("%-15s%-15s%-15s%-15s%-15s%-15s"%("Day","9:00-10:30","10:45-11:45","11:45-12:45","1:45-3:15","3:15-4:15"))
            print("_______________________________________________________________________________________________________")
            for i in range(5):
                for j in range(6):
                    print("%-15s"%(temp.sem_tt[i][j]),end="")
                print()
            print("\n\n")
            temp=temp.next

#__________________________________________________________________________OBJECT CREATION____________________________________________

obj_for_linked_list_for_traversing_courses=linked_list_for_traversing_courses()
obj_for_facultys=linked_list_for_faculty_name()
obj_for_sem=linked_list_to_travese_semester()



























def log(request):
    return render(request,'login.html')

def add(request):
    code=request.POST['code']
    name=request.POST['name']
    branch=request.POST['branch'] 
    semester=request.POST['semester']   
    credit=request.POST['credit'] 
    faculty=request.POST['credit']
    faculty_id=request.POST['faculty_id']
    theory=int(request.POST['theory'])
    tutorial=int(request.POST['tutorial'])
    lab=int(request.POST['lab'])
    node_for_courses(code,name,branch,semester,credit,faculty,faculty_id,theory,tutorial,lab)
    return render(request,'getstarted.html')

def ind(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def get(request):
    return render(request,'getstarted.html')

def stu(request):
    return render(request,'Student-Time-Table.html')

def fac(request):
    return render(request,'Faculty-time-table.html')

def contact(request):
    return render(request,'Contact.html')

def faculty(request):
    lists=[]
    names=[]
    plotting()
    temp1=obj_for_facultys.head_for_faculty_names
    while(temp1):
        names.append(temp1.faculty_name)
        lists.append(temp1.faculty_tt)
        zipped_variable=zip(lists,names)
        temp1=temp1.next
    return render(request,'Faculty-time-table.html',{'zipped':zipped_variable})

def student(request):
    #CSE_______________________________________
    #                         (self        ,code         ,name    ,branch ,semester   ,credit ,faculty       ,faculty_id,theory,tutorial,lab)
    #SEM_1
    node_for_courses("MA201"       ,"Probability"           ,"CSE"  ,"Sem_3_A"    ,5      ,"X"                ,1         ,3      ,1       ,0  )
    node_for_courses("CS201"       ,"Discrete maths"        ,"CSE"  ,"Sem_3_A"    ,5      ,"Dr. Pramod Mane"  ,1         ,3      ,1       ,0  )
    node_for_courses("CS207"       ,"object oriented prog." ,"CSE"  ,"Sem_3_A"    ,5      ,"Dr. Vivek Raj"    ,1         ,3      ,0       ,2  )
    node_for_courses("EC105"       ,"Computer_Archit"       ,"CSE"  ,"Sem_3_A"    ,5      ,"Dr. Pramod Y"     ,1         ,3      ,0       ,2  )
    node_for_courses("CS202"       ,"Design"                ,"CSE"  ,"Sem_3_A"    ,5      ,"Dr. Malay"        ,1         ,3      ,1       ,2  )
    node_for_courses("HS206"       ,"Psychology"            ,"CSE"  ,"Sem_3_A"    ,5      ,"Y"                ,1         ,3      ,0       ,0  )
    node_for_courses("MA201"       ,"Probability"           ,"CSE"  ,"Sem_3_B"    ,5      ,"X"                ,1         ,3      ,1       ,0  )
    node_for_courses("CS201"       ,"Discrete maths"        ,"CSE"  ,"Sem_3_B"    ,5      ,"Dr. Pawan"        ,1         ,3      ,1       ,0  )
    node_for_courses("CS207"       ,"object oriented prog." ,"CSE"  ,"Sem_3_B"    ,5      ,"Dr. Vivek Raj"    ,1         ,3      ,0       ,2  )
    node_for_courses("EC105"       ,"Computer_Archit"       ,"CSE"  ,"Sem_3_B"    ,5      ,"Dr. Prabhu"       ,1         ,3      ,0       ,2  )
    node_for_courses("CS202"       ,"Design"                ,"CSE"  ,"Sem_3_B"    ,5      ,"Dr. Radhika B.S"  ,1         ,3      ,1       ,2  )
    node_for_courses("HS206"       ,"Psychology"            ,"CSE"  ,"Sem_3_B"    ,5      ,"Y"                ,1         ,3      ,0       ,0  )
    
    node_for_courses("CS309"       ,"Probability"           ,"CSE"  ,"Sem_5_A"    ,5      ,"p"                ,1         ,3      ,1       ,0  )
    node_for_courses("CS303"       ,"Discrete maths"        ,"CSE"  ,"Sem_5_A"    ,5      ,"Dr. Sadhvi"       ,1         ,3      ,1       ,2  )
    node_for_courses("CS304"       ,"object oriented prog." ,"CSE"  ,"Sem_5_A"    ,5      ,"Dr. Jaylakshmi"   ,1         ,3      ,1       ,0  )
    node_for_courses("CS_BASKET"   ,"Computer_Archit"       ,"CSE"  ,"Sem_5_A"    ,5      ,"CS_A"             ,1         ,3      ,1       ,0  )
    node_for_courses("ELECTIVE_1"  ,"Design"                ,"CSE"  ,"Sem_5_A"    ,5      ,"EL_A"             ,1         ,3      ,1       ,0  )
    
    node_for_courses("CS309"       ,"Probability"           ,"CSE"  ,"Sem_5_B"    ,5      ,"p"                ,1         ,3      ,1       ,0  )
    node_for_courses("CS303"       ,"Discrete maths"        ,"CSE"  ,"Sem_5_B"    ,5      ,"Dr. Sadhvi"       ,1         ,3      ,1       ,2  )
    node_for_courses("CS304"       ,"object oriented prog." ,"CSE"  ,"Sem_5_B"    ,5      ,"Dr. Jaylakshmi"   ,1         ,3      ,1       ,0  )
    node_for_courses("CS_BASKET"   ,"Computer_Archit"       ,"CSE"  ,"Sem_5_B"    ,5      ,"CS_B"             ,1         ,3      ,1       ,0  )
    node_for_courses("ELECTIVE_1"  ,"Design"                ,"CSE"  ,"Sem_5_B"    ,5      ,"EL_B"             ,1         ,3      ,1       ,0  )
    

   
    lists=[]
    sem=[]
    plotting()
    temp1=obj_for_sem.head_for_semesters
    while(temp1):
        sem.append(temp1.sem)
        lists.append(temp1.sem_tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    
    return render(request,'Student-Time-Table.html',{'zipped':zipped_variable})