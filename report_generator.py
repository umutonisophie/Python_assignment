
def calculate_average(Backend,Frontend,Design):
    average=(Backend+Frontend+Design)/3
    return average 



def grade(avg):
    if avg>=80:
       return "A"
    elif avg>=70:
         return "B"
    elif avg>=60:
         return "C"
    elif avg>=50:
         return "D" 
         
    else:
         return "E" 


def student_report_dictionary(name,Backend,Frontend,Design):
    avg=calculate_average(Backend,Frontend,Design)
    final_grade= grade(avg)

    report={
     "name":name,"Backend":Backend,"Frontend":Frontend,"Design":Design,"average":int(avg),"grade":final_grade
}  
    return report
  
name=input("Enter your name:")
Backend=int(input("Enter your backend marks:"))
Frontend=int(input("Enter your frontend marks:"))
Design=int(input("Enter your desing marks:"))



print(student_report_dictionary(name,Backend,Frontend,Design) )



