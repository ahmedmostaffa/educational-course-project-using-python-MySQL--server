import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
    user='root', host='127.0.0.1',port='3307', database='course')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
def course_Insert_data():
    L=[]
    co_id=int(input('Enter the course id:'))
    L.append(co_id)
    stream_name=input('Enter the stream name :')
    L.append(stream_name)
    c_name=input('please enter course oppo in this stream :')
    L.append(c_name)
    course_data=(L)
    sql="INSERT INTO course_details (co_id,stream_name,c_name) values (%s,%s,%s)"
    cursor.execute(sql,course_data)
    conn.commit()

def course_view():
    print('select search from the following options :')
    print('1-course id')
    print('2-stream')
    print('3-all')
    ch=int(input('enter the choice :'))
    if ch==1:
        s=int(input('course id:'))
        c=(s,)
        sql='SELECT * from course_details where co_id=%s'
        cursor.execute(sql,c)
    elif ch==2:
        s=int(input('enter stream name:'))
        c=(s,)
        sql='SELECT * from course_details where c_name=%s'
        cursor.execute(sql,c)
    elif ch==3:
        sql='SELECT * from course_details'
        cursor.execute(sql)
    result=cursor.fetchall()
    print('The details of the course is the following:')
    for name in result:
        print(name)


def remove_course_data():
    c_i=int(input('please enter the course id want to be deleted'))
    c_d=(c_i,)
    sql='DELETE from course_details where co_id=%s'
    cursor.execute(sql,c_d)
    conn.commit()

def show_menu_project():
    print('please Enter 1 : To add course')
    print('please Enter 2 : To view course')
    print('please Enter 3 : To remove course')
    try:
        input_user=int(input('please select an option : '))
    except ValueError:
        exit("\nHy! That's Not A Number" )
    else:
        if input_user==1:
            course_Insert_data()
        elif input_user==2:
            course_view()
        elif input_user==3:
            remove_course_data()
        else:
            print('Enter correct option.... ')    



    




show_menu_project()