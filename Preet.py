from django.shortcuts import *
from datetime import date
from django.http import JsonResponse
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import xml.etree.ElementTree as ET
from myconnection import *
from django.views.decorators.csrf import csrf_exempt
def adminlogin(request):
    return render(request, 'adminlogin.html')
def checkadminlogin(request):
    email=request.GET['email']
    password=request.GET['password']
    conn=myconnection.connect('')
    cr=conn.cursor()
    query="select * from admin where email='"+email+"' and password='"+password+"'"
    cr.execute(query)
    result=cr.fetchone()
    if result==None:
        return render(request,'adminlogin.html',{"message":'invalid email/password'})
    else:
        request.session['adminemail']=email
        return render(request,'dashboard.html')
def viewfilteruser(request):

    value=request.GET['value']
    x = []
    if(value!=''):
        if request.session.has_key('adminemail'):
            conn = myconnection.connect('')
            cr = conn.cursor()
            query = "select * from entery"
            cr.execute(query)
            result = cr.fetchall()
            d= []
            for data in result:
                if (value in data[15]):
                    d.append(data[0])
                    d.append(data[1])
                    d.append(data[2])
                    d.append(data[3])
                    d.append(data[4])
                    d.append(data[5])
                    d.append(data[6])
                    d.append(data[7])
                    d.append(data[6])
                    d.append(data[9])
                    d.append(data[10])
                    d.append(data[11])
                    d.append(data[12])
                    d.append(data[13])
                    d.append(data[14])
                    x.append(d)

    else:
        d = []
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        x.append(d)
    return JsonResponse(x,safe=False)
def home(request):
    return render(request, 'UserEntery.html')
def scan(request):
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    x = []
    while True:
        y = 0
        check = 0
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            # print("Data", obj.data)

            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
            root = ET.fromstring(obj.data)
            for child in root.iter('*'):
                # print(child.tag, child.attrib)
                x.append(child.attrib)
                print(child.attrib)
                uid=child.attrib['uid']
                name = child.attrib['name']
                gender = child.attrib['gender']
                yob = child.attrib['yob']
                gname = child.attrib['gname']
                co = child.attrib['co']
                house = child.attrib['house']
                street = child.attrib['street']
                vtc = child.attrib['vtc']
                po = child.attrib['po']
                dist = child.attrib['dist']
                subdist = child.attrib['subdist']
                state = child.attrib['state']
                pc = child.attrib['pc']
                dob = child.attrib['dob']
                today = date.today()
                conn = myconnection.connect('')
                cr = conn.cursor()
                query = "select * from entery"
                cr.execute(query)
                result = cr.fetchall()
                list = []
                for row in result:
                    print(row)
                    print(row[0])
                    if(row[0]==uid):
                        print("data Present")
                        x.pop()
                    else:
                        check=1
                if(check==1):
                    query = "insert into entery values('" + uid + "','" + str(
                            name) + "','" + str(gender) + "','" + yob + "','" + str(
                            gname) + "','" + str(co) + "','" + str(house) + "','" + str(
                            street) + "','" + str(vtc) + "','" + str(po) + "','" + str(
                            dist) + "','" + str(subdist) + "','" + str(state) + "','" + \
                               pc + "','" + str(dob) + "','" + str(today) + "')"
                    cr.execute(query)
                    conn.commit()

                if (child == ""):
                    break

            if (obj.data != ""):
                y = 1
                break

        if (y == 1):
            break
    return JsonResponse(x, safe=False)
@csrf_exempt
def add(request):
    check=0
    uid=request.POST['textbox1']
    name=request.POST['textbox2']
    gender=request.POST['textbox3']
    yob=request.POST['textbox4']
    gname=request.POST['textbox5']
    co=request.POST['textbox6']
    house= request.POST['textbox7']
    street = request.POST['textbox8']
    vtc = request.POST['textbox9']
    po = request.POST['textbox10']
    dist = request.POST['textbox11']
    subdist = request.POST['textbox12']
    state = request.POST['textbox13']
    pc = request.POST['textbox14']
    dob = request.POST['textbox15']
    today = str(date.today())
    conn = myconnection.connect('')
    cr = conn.cursor()
    query = "select * from entery"
    cr.execute(query)
    result = cr.fetchall()
    list = []
    for row in result:
        print(row)
        print(row[0])
        if (row[0] == uid):
            print("data Present")
        else:
            check = 1
    if (check == 1):
        query = "insert into entery values('" + uid + "','" + str(
            name) + "','" + str(gender) + "','" + yob + "','" + str(
            gname) + "','" + str(co) + "','" + str(house) + "','" + str(
            street) + "','" + str(vtc) + "','" + str(po) + "','" + str(
            dist) + "','" + str(subdist) + "','" + str(state) + "','" + \
                pc + "','" + str(dob) + "','" + str(today) + "')"
        cr.execute(query)
        conn.commit()

    return HttpResponse("success")