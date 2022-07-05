from pickle import GET
from platform import node
from .models import data
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import data
#_______________________________________________________INITIALIZATIONS___________________________
#ELECTIVES ARE NOT HAVING LABS?
cse=0
dsai=0
ece=0
cse_th=0
dsai_th=0
ece_th=0
cse_tut=0
dsai_tut=0
ece_tut=0
cse_lab=0
dsai_lab=0
ece_lab=0
number_of_ece_labs=2
number_of_cse_labs=2
number_of_dsai_labs=2
elective_courses=[]

#________________________________INITIAL PLACE WHERE ALL NODES ARE SENT___________________________
class node_for_courses:
    def __init__(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name=None,capacity=30):
            obj_for_class_rooms.insert(branch+'_'+semester,50)
            if branch[0]=='C': 
                global cse
                cse=1
                global cse_th
                global cse_tut
                global cse_lab
                if theory:cse_th=1
                if tutorial:cse_tut=1
                if lab:cse_lab=1
            if branch[0]=='D':
                global dsai
                dsai=1
                global dsai_th
                global dsai_tut
                global dsai_lab
                if theory:dsai_th=1
                if tutorial:dsai_tut=1
                if lab:dsai_lab=1
            if branch[0]=='E':
                global ece
                ece=1
                global ece_th
                global ece_tut
                global ece_lab
                if theory:ece_th=1
                if tutorial:ece_tut=1
                if lab:ece_lab=1
            global elective_courses
            if name=='elective' :
                if code not in elective_courses:
                    elective_courses.append(code)
                obj_for_linked_list_for_electives.insert(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity)
            else:
                if lab_name:
                    #obj_for_lab_rooms.insert(lab_name,capacity)
                    pass
                if theory:
                    obj_for_linked_list_for_traversing_courses.insert(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity)
                if tutorial:
                    obj_for_linked_list_for_traversing_tutorials.insert(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity)
                if lab:
                    obj_for_linked_list_for_traversing_labs.insert(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity)

#_________________________________________NODES FOR LABS__________________________________________________
class node_for_labs:
    def __init__(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.semester=semester
        obj_for_sem.insert(semester,branch)
        self.credit=credit
        self.faculty=faculty
        self.faculty_id=1
        obj_for_facultys.insert(faculty,self.faculty_id)
        self.branch=branch
        self.lab_name=lab_name
        self.id=theory
        self.lab_code=None
    #Number of minutes
        self.check=theory
        self.theory=0
        self.tutorial=0
        self.lab=lab*60
        self.next=None

i=1
#____________________________________________LINKED LIST FOR LABS______________________________________________
class linked_list_for_traversing_labs:
    def __init__(self):
        global i
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None

    def insert(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name=None,capacity=30):
                global i
                new_node_to_insert_lab1=node_for_labs(code+"_LAB_1",name,branch,branch+"_"+semester,credit,faculty,i,0,lab,lab_name,capacity)
                new_node_to_insert_lab2=node_for_labs(code+"_LAB_2",name,branch,branch+"_"+semester,credit,faculty,i,0,lab,lab_name,capacity)
                i+=1
                if branch=='CSE':
                    if self.head_for_CSE==None :
                        if lab:
                            self.head_for_CSE=new_node_to_insert_lab1
                            self.head_for_CSE.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return
                if branch=='DSAI':
                    if self.head_for_DSAI==None :
                        if lab:
                            self.head_for_DSAI=new_node_to_insert_lab1
                            self.head_for_DSAI.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return
                if branch=='ECE':
                    if self.head_for_ECE==None :
                        if lab:
                            self.head_for_ECE=new_node_to_insert_lab1
                            self.head_for_ECE.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return

#_________________________________________________NODE FOR TUTORIAL_________________________________________________
class node_for_tutorial:
    def __init__(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.semester=semester
        obj_for_sem.insert(semester,branch)
        self.credit=credit
        self.faculty=faculty
        self.faculty_id=1
        obj_for_facultys.insert(faculty,self.faculty_id)
        self.branch=branch
        self.lab_name=lab_name
    #Number of minutes
        self.theory=0
        self.tutorial=tutorial*60
        self.lab=0
        self.next=None

#______________________________________________LINKED LIST FOR TUTORIALS__________________________________________
class linked_list_for_traversing_tutorial:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None

    def insert(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity):
                new_node_to_insert_tutorial=node_for_tutorial(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,theory,tutorial,lab,lab_name=None,capacity=30)
                if branch=='CSE':
                    if self.head_for_CSE==None :
                        self.head_for_CSE=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return
                if branch=='DSAI':
                    if self.head_for_DSAI==None :
                        if tutorial:
                            self.head_for_DSAI=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return
                if branch=='ECE':
                    if self.head_for_ECE==None :
                        if tutorial:
                            self.head_for_ECE=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return

#_______________________________________________NODE FOR THEORY AND ELECTIVES_____________________________________________
class node_for_courses_for_all:
    def __init__(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.semester=semester
        obj_for_sem.insert(semester,branch)
        self.credit=credit
        self.faculty=faculty
        self.lab_name=lab_name
        obj_for_facultys.insert(faculty,id=1)
        self.branch=branch
        self.lab_name=lab_name
    #Number of minutes
        self.theory=theory*60
        self.tutorial=tutorial*60
        self.lab=lab*60
        self.next=None

#_______________________________________________LINKED LIST FOR THEORY_______________________________________________
class linked_list_for_traversing_courses:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None

    def insert(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name=None,capacity=30):
                new_node_to_insert_tutorial=None
                new_node_to_insert_lab=None
                new_node_to_insert_theory=None
                if theory:
                    new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",name,branch,branch+"_"+semester,credit,faculty,theory,0,0,lab_name,capacity)
                if branch=='CSE':
                    if self.head_for_CSE==None :
                        if lab:
                            self.head_for_CSE=new_node_to_insert_lab
                            if theory:
                                self.head_for_CSE=new_node_to_insert_theory
                                if tutorial:
                                    self.head_for_CSE.next=new_node_to_insert_tutorial
                            else:
                                if tutorial:
                                    self.head_for_CSE=new_node_to_insert_tutorial
                        else:
                            if theory:
                                self.head_for_CSE=new_node_to_insert_theory
                                new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",name,branch,branch+"_"+semester,credit,faculty,0,0,0,lab_name,capacity)
                                if tutorial:
                                    self.head_for_CSE.next=new_node_to_insert_tutorial
                                    new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,0,0,0,lab_name,capacity)
                            else:
                                if tutorial:
                                    self.head_for_CSE=new_node_to_insert_tutorial
                                    new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,0,0,0,lab_name,capacity)
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

#____________________________________________LINKED LIST FOR ELECTIVES_______________________________________________
class linked_list_for_electives:
    def __init__(self):
        self.head=None
    def insert(self,code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name,capacity):
        new_node_to_insert_lab=None
        new_node_to_insert_theory=None
        new_node_to_insert_tutorial=None
        if theory:
            new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",name,branch,branch+"_"+semester,credit,faculty,theory,0,0,lab_name,capacity)
        if tutorial:
            new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",name,branch,branch+"_"+semester,credit,faculty,0,tutorial,0,lab_name,capacity)
        if lab:
            new_node_to_insert_lab=node_for_courses_for_all(code+"_LAB",name,branch,branch+"_"+semester,credit,faculty,0,0,lab,lab_name,capacity)        
        
        if self.head==None:
            if new_node_to_insert_lab:
                self.head=new_node_to_insert_lab
                if new_node_to_insert_theory:
                    self.head.next=new_node_to_insert_theory
                    if new_node_to_insert_tutorial:
                        self.head.next.next=new_node_to_insert_tutorial
                else:
                    if new_node_to_insert_tutorial:
                        self.head.next=new_node_to_insert_tutorial
            else:
                if new_node_to_insert_theory:
                    self.head=new_node_to_insert_theory
                    if new_node_to_insert_tutorial:
                        self.head.next=new_node_to_insert_tutorial
                else:
                    if new_node_to_insert_tutorial:
                        self.head=new_node_to_insert_tutorial
            return

        temp=self.head
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

#_____________________________________LINKED LIST FOR MERGING THEORY, TUTORIAL, LAB SESSIONS___________________________________
class linked_list_for_merged_codes:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None

    def change_order(self):
        if cse:
            temp=None
            temp1=obj_for_linked_list_for_traversing_labs.head_for_CSE
            temp2=obj_for_linked_list_for_traversing_tutorials.head_for_CSE
            temp3=obj_for_linked_list_for_traversing_courses.head_for_CSE
            if temp1:
                self.head_for_CSE=temp1
                if temp2:
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=temp2
                    if temp3:
                        temp=self.head_for_CSE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:
                    if temp3:
                        temp=self.head_for_CSE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
            else:
                if temp2:
                    self.head_for_CSE=temp2
                    if temp3:
                        temp=self.head_for_CSE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:self.head_for_CSE=temp3

        if dsai:
            temp1=obj_for_linked_list_for_traversing_labs.head_for_DSAI
            temp2=obj_for_linked_list_for_traversing_tutorials.head_for_DSAI
            temp3=obj_for_linked_list_for_traversing_courses.head_for_DSAI
            if temp1:
                self.head_for_DSAI=temp1
                if temp2:
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=temp2
                    if temp3:
                        temp=self.head_for_DSAI
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:
                    if temp3:
                        temp=self.head_for_DSAI
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
            else:
                if temp2:
                    self.head_for_DSAI=temp2
                    if temp3:
                        temp=self.head_for_DSAI
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:self.head_for_DSAI=temp3

        if ece:
            temp1=obj_for_linked_list_for_traversing_labs.head_for_ECE
            temp2=obj_for_linked_list_for_traversing_tutorials.head_for_ECE
            temp3=obj_for_linked_list_for_traversing_courses.head_for_ECE
            if temp1:
                self.head_for_ECE=temp1
                if temp2:
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=temp2
                    if temp3:
                        temp=self.head_for_ECE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:
                    if temp3:
                        temp=self.head_for_ECE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
            else:
                if temp2:
                    self.head_for_ECE=temp2
                    if temp3:
                        temp=self.head_for_ECE
                        while(temp.next):
                            temp=temp.next                    
                        temp.next=temp3
                else:self.head_for_ECE=temp3
        
#________________________________________________NODE FOR FACULTY_______________________________________________
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

#_______________________________________________LINKED LIST FOR FACULTY NAME_______________________________________
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

#________________________________________________NODE FOR SEMESTER________________________________________________
class node_for_semisters:
    def __init__(self,sem,branch):
        self.sem=sem
        self.branch=branch
        self.sem_tt=[['Monday1','*','*','*','*','*'],
                        ['Tuesday1','*','*','*','*','*'],  
                        ['Wednesday1','*','*','*','*','*'],
                        ['Thursday1','*','*','*','*','*'],
                        ['Friday1','*','*','*','*','*']]
        self.sem_tt_new=[['Monday1','*','*','*','*','*'],
                        ['Tuesday1','*','*','*','*','*'],  
                        ['Wednesday1','*','*','*','*','*'],
                        ['Thursday1','*','*','*','*','*'],
                        ['Friday1','*','*','*','*','*']]
        self.next=None

#____________________________________________LINKED LIST TO TRAVERSE SEMESTERS______________________________________
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
            

#____________________________________________NODE FOR LAB ROOMS________________________________________
class node_for_linked_list_for_lab_rooms:
    def __init__(self,name,capacity,branch):
        self.name=name
        self.capacity=capacity
        self.branch=branch
        self.tt=[['Monday','*','*','*','*','*'],
                ['Tuesday','*','*','*','*','*'],  
                ['Wednesday','*','*','*','*','*'],
                ['Thursday','*','*','*','*','*'],
                ['Friday','*','*','*','*','*']]
        
        self.next=None
        
#_____________________________________________LINKED LIST FOR TRAVERSING LAB ROOMS___________________________
class linked_list_for_traversing_lab_rooms:
    def __init__(self):
        self.head_for_CSE_rooms=None
        self.head_for_ECE_rooms=None
    def insert(self,name,capacity,branch):
        new_lab=node_for_linked_list_for_lab_rooms(name,capacity,branch)
        if branch=='CSE':
            if self.head_for_CSE_rooms==None:
                self.head_for_CSE_rooms=new_lab
                return
            count=0
            temp=self.head_for_CSE_rooms
            while(temp):
                if temp.name==name:
                    count+=1
                    break
                temp=temp.next
            if count==0:
                temp=self.head_for_CSE_rooms
                while(temp.next):
                    temp=temp.next
                temp.next=new_lab
        if branch=='ECE':
            if self.head_for_ECE_rooms==None:
                self.head_for_ECE_rooms=new_lab
                return
            count=0
            temp=self.head_for_ECE_rooms
            while(temp):
                if temp.name==name:
                    count+=1
                    break
                temp=temp.next
            if count==0:
                temp=self.head_for_ECE_rooms
                while(temp.next):
                    temp=temp.next
                temp.next=new_lab
            

#____________________________________________NODE FOR CLASS ROOMS________________________________________
class node_for_linked_list_for_class_rooms:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        self.classroom_tt=[['Monday','*','*','*','*','*'],
                ['Tuesday','*','*','*','*','*'],  
                ['Wednesday','*','*','*','*','*'],
                ['Thursday','*','*','*','*','*'],
                ['Friday','*','*','*','*','*']]
        self.next=None
        
#_____________________________________________LINKED LIST FOR TRAVERSING CLASS ROOMS___________________________
class linked_list_for_traversing_class_rooms:
    def __init__(self):
        self.head_for_class_rooms=None
    def insert(self,name,capacity):
        new_lab=node_for_linked_list_for_class_rooms(name,capacity)
        if self.head_for_class_rooms==None:
            self.head_for_class_rooms=new_lab
            return
        count=0
        temp=self.head_for_class_rooms
        while(temp):
            if temp.name==name:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_class_rooms
            while(temp.next):
                temp=temp.next
            temp.next=new_lab

#_______________________________________________________PLOTTING FUNCTION DECISION MAKING________________________________________
def plotting():
    obj_for_linked_list_for_merged_codes.change_order()
    for i in range(3):
        variable_for_sem_generalized_head=None
        variable_for_classroom_generalized_head=None
        if i==0:
            if cse==0:break
            temp1=obj_for_linked_list_for_merged_codes.head_for_CSE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==1:
            if dsai==0:break
            temp1=obj_for_linked_list_for_merged_codes.head_for_DSAI
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==2:
            if ece==0:break
            temp1=obj_for_linked_list_for_merged_codes.head_for_ECE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
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

                #Fetching classroom.
                temp4=variable_for_classroom_generalized_head
                while(temp4):
                    if (temp1.semester)==temp4.name:
                        break
                    temp4=temp4.next
                
                #Fetching lab every time.
                temp5=None
                if temp1.lab_name=='CSE_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                if temp1.lab_name=='ECE_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                #Changing timetable.
                if temp1.branch+"_Sem_3_A"==temp1.semester or temp1.branch+"_Sem_3_B"==temp1.semester or temp1.branch+"_Sem_4_A"==temp1.semester or temp1.branch+"_Sem_4_B"==temp1.semester or temp1.branch+"_Sem_7_A"==temp1.semester or temp1.branch+"_Sem_7_B"==temp1.semester or temp1.branch+"_Sem_8_A"==temp1.semester or temp1.branch+"_Sem_8_B"==temp1.semester:
                    if temp1.theory:
                        time=0
                        for _ in range(10):
                            for i in range(5):
                                for j in range(6):
                                    if j==1 or j==4:
                                        if time>=temp1.theory:
                                            break
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                            if j==2 or j==3 or j==5 or j==6 and time+60<=temp1.theory:
                                                temp2.faculty_tt[i][j]=temp1.semester
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                time+=60
                                                break
                                            if time+90<=temp1.theory and (temp1.theory/60)%2!=0:
                                                time+=90
                                                temp2.faculty_tt[i][j]=temp1.semester
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                break
                                    if _>=8:
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                            temp2.faculty_tt[i][j]=temp1.semester
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            if j==2 or j==3 or j==5 or j==6:
                                                time+=60
                                                break
                                            time+=90
                                            break
                                    if _>=7 and time+60<temp1.theory:
                                        if j==2 or j==3:continue
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            temp2.faculty_tt[i][j]=temp1.semester
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
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
                                    if j==2 or j==3 or j==5:
                                        if time>temp1.tutorial:
                                            break
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester:
                                                    break

                                            if j==2 or j==3 or j==5 or j==6 and time+60<=temp1.tutorial and time<temp1.tutorial:
                                                temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                time+=60
                                                break
                                            
                                            if time+90<=temp1.tutorial and time<temp1.tutorial:
                                                time+=90
                                                temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                break

                                    if _>=7 and time+60<temp1.tutorial:
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
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
                                            if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                                if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp5.tt[i][j]=='*':
                                                        temp5.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code
                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        time+=60
                                                        break
                                                    temp5=temp5.next

                                        elif time+90<=temp1.lab and (j==1 or j==4):
                                            if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                                if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp5.tt[i][j]=='*':
                                                        temp5.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code
                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        time+=90
                                                        break
                                                    temp5=temp5.next

                                    elif j==2:
                                        if temp2.faculty_tt[i][j]==temp2.faculty_tt[i][j+1]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][j-1]==temp1.semester:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][j]=='*' and temp6.tt[i][j]=='*':
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp2.faculty_tt[i][j+1]=temp1.semester+"_LAB"

                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt[i][j+1]=temp1.code

                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp6.name

                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        temp4.classroom_tt[i][j+1]=temp1.code

                                                        temp6.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp6.tt[i][j+1]=temp1.semester+"_"+temp1.code

                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            # If one batch has a lab already....
                                            elif temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1] and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                #Check if the existing value in that place exists in the lab sessions linked list.
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                #get the right lab
                                                while(temp6):
                                                    if temp6.tt[i][j]=='*':
                                                        break
                                                    temp6=temp6.next
                                                
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                    temp2.faculty_tt[i][j+1]=temp1.semester+"_LAB"

                                                    temp3.sem_tt[i][j]+="/"+temp1.code
                                                    temp3.sem_tt[i][j+1]+="/"+temp1.code

                                                    temp3.sem_tt_new[i][j]+="/"+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+="/"+temp1.code+temp6.name

                                                    temp4.classroom_tt[i][j]+="/"+temp1.code
                                                    temp4.classroom_tt[i][j+1]+="/"+temp1.code
                                                    
                                                    temp6.tt[i][j]=temp1.semester+"_"+temp1.code
                                                    temp6.tt[i][j+1]=temp1.semester+"_"+temp1.code

                                                    time+=120
                                                    break
                if temp1.branch+"_Sem_5_A"==temp1.semester or temp1.branch+"_Sem_5_B"==temp1.semester or temp1.branch+"_Sem_6_A"==temp1.semester or temp1.branch+"_Sem_6_B"==temp1.semester:
                    if temp1.theory:
                        time=0
                        for _ in range(10):
                            for i in range(5):
                                for j in range(6):
                                    if j==1 :
                                        if time>=temp1.theory:
                                            break
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                            if time+90<=temp1.theory and (temp1.theory/60)%2!=0:
                                                time+=90
                                                temp2.faculty_tt[i][j]=temp1.semester
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                break
                                    if _>=7 and time+60<temp1.theory:
                                        if j==2 or j==3:
                                            if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                                temp2.faculty_tt[i][j]=temp1.semester
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                time+=60
                                                break
                                                                                        
                    elif temp1.tutorial:
                        time=0
                        for _ in range(10):    
                            for i in range(5):
                                for j in range(6):
                                    if j==2 or j==3:
                                        if time>temp1.tutorial:
                                            break
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester:
                                                    break

                                            if time+60<=temp1.tutorial and time<temp1.tutorial:
                                                temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                time+=60
                                                break
                                            
                                            if time+90<=temp1.tutorial and time<temp1.tutorial and (j==1 or j==4):
                                                time+=90
                                                temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                                temp3.sem_tt[i][j]=temp1.code
                                                temp3.sem_tt_new[i][j]=temp1.code
                                                temp4.classroom_tt[i][j]=temp1.name
                                                break

                                    if _>=7 and time+60<temp1.tutorial:
                                        if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][j]=temp1.semester+"_TUT"
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
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
                                            if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                                if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp5.tt[i][j]=='*':
                                                        temp5.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp5.name
                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        time+=60
                                                        break
                                                    temp5=temp5.next

                                        elif time+90<=temp1.lab and (j==1 or j==4):
                                            if temp2.faculty_tt[i][j]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                                if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp5.tt[i][j]=='*':
                                                        temp5.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp5.name
                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        time+=90
                                                        break
                                                    temp5=temp5.next

                                    elif j==4:
                                        if temp2.faculty_tt[i][j]==temp2.faculty_tt[i][j+1]=='*' and time<temp1.lab:
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][j-1]==temp1.semester:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp5.tt[i][j]=='*' and temp5.tt[i][j]=='*':
                                                        temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp5.name
                                                        temp4.classroom_tt[i][j]=temp1.code
                                                        temp5.tt[i][j]=temp1.semester+"_"+temp1.code
                                                        temp2.faculty_tt[i][j+1]=temp1.semester+"_LAB"
                                                        temp3.sem_tt[i][j+1]=temp1.code
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp5.name
                                                        temp4.classroom_tt[i][j+1]=temp1.code
                                                        temp5.tt[i][j+1]=temp1.semester+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp5=temp5.next
                                            else:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                #Check if the existing value in that place exists in the lab sessions linked list.
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                #get the right lab
                                                while(temp6):
                                                    if temp6.tt[i][j]=='*':
                                                        break
                                                    temp6=temp6.next

                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][j]=temp1.semester+"_LAB"
                                                    temp2.faculty_tt[i][j+1]=temp1.semester+"_LAB"

                                                    temp3.sem_tt[i][j]+="/"+temp1.code
                                                    temp3.sem_tt[i][j+1]+="/"+temp1.code

                                                    temp3.sem_tt_new[i][j]+="/"+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+="/"+temp1.code+temp6.name

                                                    temp4.classroom_tt[i][j]+="/"+temp1.code
                                                    temp4.classroom_tt[i][j+1]+="/"+temp1.code

                                                    temp6.tt[i][j]=temp1.semester+"_"+temp1.code
                                                    temp6.tt[i][j+1]=temp1.semester+"_"+temp1.code

                                                    time+=120
                                                    break
                temp1=temp1.next

def plotting_for_electives():
        temp1=obj_for_linked_list_for_electives.head
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
                temp3=obj_for_class_rooms.head_for_class_rooms
                
                if temp1.theory:
                    time=0
                    for _ in range(10):
                        for i in range(5):
                            for j in range(6):
                                if j==1 or j==4:
                                    if time>=temp1.theory:
                                        break
                                    if temp2.faculty_tt[i][j]=='*' and time<temp1.theory:
                                        temp3=obj_for_class_rooms.head_for_class_rooms
                                        while(temp3):
                                            if temp3.classroom_tt[i][j]=='*':
                                                temp2.faculty_tt[i][j]=temp1.code
                                                temp3.classroom_tt[i][j]=temp1.code
                                                if time+90<=temp1.theory:
                                                    time+=90
                                                break
                                            temp3=temp3.next 
                                        
                                if _>=8:
                                    if temp2.faculty_tt[i][j]=='*' and time<temp1.theory:
                                        temp3=obj_for_class_rooms.head_for_class_rooms
                                        while(temp3):
                                            if temp3.classroom_tt[i][j]=='*':
                                                temp2.faculty_tt[i][j]=temp1.code
                                                temp3.classroom_tt[i][j]=temp1.code
                                                if j==2 or j==3 or j==5 or j==6:
                                                    time+=60
                                                    break
                                                time+=90
                                                break
                                            temp3=temp3.next 
                                        
                                if _>=7 and time+60<temp1.theory:
                                    if j==2 or j==3:continue
                                    if temp2.faculty_tt[i][j]=='*':
                                        temp3=obj_for_class_rooms.head_for_class_rooms
                                        while(temp3):
                                            if temp3.classroom_tt[i][j]=='*':
                                                temp2.faculty_tt[i][j]=temp1.code
                                                temp3.classroom_tt[i][j]=temp1.code
                                                if j==2 or j==3 or j==5 or j==6:
                                                    time+=60
                                                    break
                                                time+=90
                                                break
                                            temp3=temp3.next 
                                        
                                    
                elif temp1.tutorial:
                    time=0
                    for _ in range(10):    
                        for i in range(5):
                            for j in range(6):
                                if j==2 or j==3 or j==5:
                                    if time>temp1.tutorial:
                                        break
                                    if temp2.faculty_tt[i][j]=='*' and time<temp1.tutorial:
                                        if j-1!=0 and temp2.faculty_tt[i][j-1]!='*':
                                                break

                                        if j==2 or j==3 or j==5 or j==6 and time+60<=temp1.tutorial and time<temp1.tutorial:
                                            temp3=obj_for_class_rooms.head_for_class_rooms
                                            while(temp3):
                                                if temp3.classroom_tt[i][j]=='*':
                                                    temp2.faculty_tt[i][j]=temp1.code
                                                    temp3.classroom_tt[i][j]=temp1.code
                                                    time+=60
                                                    break
                                                temp3=temp3.next
                                            break 
                                        
                                        if time+90<=temp1.tutorial and time<temp1.tutorial:
                                            temp3=obj_for_class_rooms.head_for_class_rooms
                                            while(temp3):
                                                if temp3.classroom_tt[i][j]=='*':
                                                    temp2.faculty_tt[i][j]=temp1.code
                                                    temp3.classroom_tt[i][j]=temp1.code
                                                    time+=90
                                                    break
                                                temp3=temp3.next 

                                if _>=7 and time+60<temp1.tutorial:
                                    if temp2.faculty_tt[i][j]=='*' and time<temp1.tutorial:
                                        temp3=obj_for_class_rooms.head_for_class_rooms
                                        while(temp3):
                                            if temp3.classroom_tt[i][j]=='*':
                                                temp2.faculty_tt[i][j]=temp1.code
                                                temp3.classroom_tt[i][j]=temp1.code
                                                if j==2 or j==3 or j==5 or j==6:
                                                    time+=60
                                                    break
                                                time+=90
                                                break
                                            temp3=temp3.next 
                temp1=temp1.next
#___________________________________________________________OBJECT CREATION____________________________________________
obj_for_linked_list_for_traversing_courses=None
obj_for_linked_list_for_traversing_labs=None
obj_for_linked_list_for_traversing_tutorials=None
obj_for_linked_list_for_merged_codes=None
obj_for_linked_list_for_electives=None
obj_for_facultys=None
obj_for_sem=None
obj_for_linked_list_for_traversing_lab_rooms=None
obj_for_class_rooms=None
obj_for_linked_list_for_traversing_courses=linked_list_for_traversing_courses()
obj_for_linked_list_for_traversing_labs=linked_list_for_traversing_labs()
obj_for_linked_list_for_traversing_tutorials=linked_list_for_traversing_tutorial()
obj_for_linked_list_for_merged_codes=linked_list_for_merged_codes()
obj_for_linked_list_for_electives=linked_list_for_electives()
obj_for_facultys=linked_list_for_faculty_name()
obj_for_sem=linked_list_to_travese_semester()
obj_for_linked_list_for_traversing_lab_rooms=linked_list_for_traversing_lab_rooms()
obj_for_class_rooms=linked_list_for_traversing_class_rooms()
#__________________________________________________________PRINTING_________________________________________________

obj_for_linked_list_for_traversing_lab_rooms.insert('L201',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L202',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L203',50,'CSE')
# obj_for_linked_list_for_traversing_lab_rooms.insert('L204',50,'ECE')
# obj_for_linked_list_for_traversing_lab_rooms.insert('L205',50,'CSE')
# obj_for_linked_list_for_traversing_lab_rooms.insert('L206',50,'CSE')
# obj_for_class_rooms.insert('ECE_Sem_3',30)# Extra classroom to be used..


























def log(request):
    return render(request,'login.html')

def add(request):
        code=request.POST['code']
        name=request.POST['name']
        branch=request.POST['branch'] 
        semester=request.POST['semester']   
        credit=request.POST['credit'] 
        faculty=request.POST['faculty']
        theory=request.POST['theory']
        tutorial=int(request.POST['tutorial'])
        lab=int(request.POST['lab'])
        lab_name=(request.POST['lab_name'])
        node_for_courses(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name)
        return render(request,'getstarted.html')
num=0
def ind(request):
    global num
    if num==0:
        datas=data.objects.all()
        for i in datas:
            node_for_courses(i.code,i.name,i.branch,i.semester,i.credit,i.faculty,i.theory,i.tutorial,i.lab,i.lab_name)
        plotting()
        plotting_for_electives()
        num=1
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
    zipped_variable=zip(lists,names)
    temp1=obj_for_facultys.head_for_faculty_names
    while(temp1):
        names.append(temp1.faculty_name)
        lists.append(temp1.faculty_tt)
        temp1=temp1.next
    zipped_variable=zip(lists,names)
    return render(request,'Faculty-time-table.html',{'zipped':zipped_variable})

def student(request):
    #CSE_______________________________________
    #                         (self        ,code         ,name    ,branch ,semester   ,credit ,faculty       ,faculty_id,theory,tutorial,lab)
    #SEM_1
    lists=[]
    sem=[]
    temp1=obj_for_sem.head_for_semesters
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.sem)
        lists.append(temp1.sem_tt_new)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'Student-Time-Table.html',{'zipped':zipped_variable})

def classroom(request):
    lists=[]
    sem=[]
    temp1=obj_for_class_rooms.head_for_class_rooms
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.name)
        lists.append(temp1.classroom_tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'classroom.html',{'zipped':zipped_variable})

def faculty(request):
    lists=[]
    sem=[]
    temp1=obj_for_facultys.head_for_faculty_names
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.faculty_name)
        lists.append(temp1.faculty_tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'faculty.html',{'zipped':zipped_variable})

def lab(request):
    lists=[]
    sem=[]
    zipped_variable=zip(lists,sem)
    temp1=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
    temp2=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
    while(temp1):
        sem.append(temp1.name)
        lists.append(temp1.tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    while(temp2):
        sem.append(temp2.name)
        lists.append(temp2.tt)
        zipped_variable=zip(lists,sem)
        temp2=temp2.next
    return render(request,'lab.html',{'zipped':zipped_variable})

