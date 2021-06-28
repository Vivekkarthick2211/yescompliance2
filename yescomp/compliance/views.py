from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.

def mainfunc():
    return Response("hello")


from django.db import connection
from rest_framework.fields import JSONField
from yescomp.settings import DATABASES
import MySQLdb

#conn=MySQLdb.connect("http://127.0.0.1.8000","root",
                #  "rootvi","djangodb")

from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import  File1, dataframe_DD_table, dataframetable, update

from .serializers import FileSerializer2, Fileupdate, MyModel, tempSerializer,yes

from .models import yes_complaines_login

from django.utils.encoding import smart_str
from werkzeug.utils import secure_filename
from rest_framework import  viewsets


import pandas as pd
import numpy as np

from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer


#########  UPDATE ############
# @api_view(['put'])
# def update(request,id):
#     query=task1.objects.get(id=id)
#     serializers_class=get_db(instance=query,data=request.data,partial=True)
#     if serializers_class.is_valid():
#         serializers_class.save()
#     return Response(serializers_class.data)


class loginViewset(viewsets.ModelViewSet):
    queryset=yes_complaines_login.objects.all()
    serializer_class=yes

    def list(self,request):
        user_name=request.GET['user_name']
        query=yes_complaines_login.objects.filter(user_name=user_name)
        serializer_class=yes(query,many=True)
        return Response(serializer_class.data)



class FileView(viewsets.ModelViewSet):
    
    queryset=File1.objects.all()
    serializer_class=FileSerializer
    def list(self,request):
        status = request.GET['status']
        
        print(status)
        queryset=File1.objects.filter(status=status)
        serializer_class=FileSerializer(queryset,many=True)
            # if serializer_class.is_valid():
            #     serializer_class.save()
        return Response (serializer_class.data)
            # else:
            #     return response ("no data")
### compiled status
# 

class FileView2(viewsets.ModelViewSet):
    
    queryset=File1.objects.all()
    serializer_class=FileSerializer
    def list(self,request):
        id = request.GET['id']
        queryset=File1.objects.filter(id=id)
        serializer_class=FileSerializer2(queryset,many=True)
            # if serializer_class.is_valid():
            #     serializer_class.save()
        return Response (serializer_class.data)   

@api_view(['POST'])
def post(request):
    serializer_class = FileSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
       # formd=formd.filename.replace(" ","_")
       # vivek=pd.read_excel('D:\\django new\\restpython\\django_project\\media\\')
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def post_template(request):
    serializer_class = tempSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
       # formd=formd.filename.replace(" ","_")
       # vivek=pd.read_excel('D:\\django new\\restpython\\django_project\\media\\')
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filter_table(request,id):
    queryset=File1.objects.get(id=id)
    serializer_class=FileSerializer(queryset)
    print(queryset)
    musterroll=serializer_class.data['musterroll']
    regofwages=serializer_class.data['registerofwages']
    muster=pd.read_excel('D:/django new/restpython/django_project/'+musterroll,header=6)
    regwages=pd.read_excel('D:/django new/restpython/django_project/'+regofwages,header=9)
         #preprocessing the Muster excel Dataframe
    muster.rename( columns={'Unnamed: 0':'SI.\nNO','Unnamed: 1':'Sl. No. in Emp. Register','Unnamed: 2':'Names','Unnamed: 3':'Relay # or set work',
                   'Unnamed: 4':'Place of Work','Unnamed: 5':'In Out','Unnamed: 37':'Summary of days','Unnamed: 38':'Remarks No. of hours','Unnamed: 39':'Signature of Register keeper'}, inplace=True )

    muster['Relay # or set work'] =muster['Relay # or set work'].replace(np.nan, '')
    muster['In Out'] = muster['In Out'].replace(np.nan, '')
    muster['Remarks No. of hours'] = muster['Remarks No. of hours'].replace(np.nan, '')
    muster['Signature of Register keeper'] = muster['Signature of Register keeper'].replace(np.nan,'')
    muster=muster.replace(np.nan, 'New Joinee')
        #muster.to_csv('form--d.csv', header=True, index=False)

        #preprocessing the regwages excel Dataframe
    regwages= regwages.iloc[1:]
    regwages.rename( columns={'Unnamed: 16':'Net payment','Unnamed: 17':'Employer Share Pf Welfare','Unnamed: 18':'Receipt by Employee/Bank','Unnamed: 19':'Date of Payment',
                'Unnamed: 20':'Remarks'}, inplace=True )

    regwages=regwages.replace(np.nan, '')
   # regwages.to_csv('D:\\django new\\restpython\\django_project\\form--b.csv', header=True, index=False)
    mad=muster.iloc[:,6:37]
    kabil=regwages.iloc[:,2]

    class tablesdat:
            hh=[]
  
            for kk in range(0,len(mad)):#6
                    li=mad.loc[kk]
    
                    count=0
                    count1=0
                    count2=0
                    count3=0
                    count4=0
   
                    for i in range(0,len(mad.columns)):#31
                        if (li.iloc[i]=="New Joinee"):
                            count=count+1
                        elif (li.iloc[i]=="P"):
                            count1=count1+1
                        elif (li.iloc[i]=="A"):
                            count2=count2+1
                        elif (li.iloc[i]=="FH"):
                            count3=count3+1
                        else:
                            count4=count4+1
                    hh.append(count1+count3)
                    print(hh)

            def myfunc(self):
                    loo=[]
                    hh=[]
                    form_d_sumofdays=muster.iloc[:,37]
                    hh.append(self.hh )
                    for i in range(0,len(form_d_sumofdays)):
                        if (form_d_sumofdays.iloc[i]==hh[0][i]):
                            print(form_d_sumofdays.iloc[i],hh[0][i],"lio")
                            print("ok with datas !!!! " , form_d_sumofdays.iloc[i],hh[0][i])
                            File1.objects.filter(id=id).update(musterroll_status="compiled")
                            dataframe_DD_table.objects.create(message="ok with datas",noofcountsofdaysheshehavebeenworked=hh[0][i],summaryofdays=form_d_sumofdays.iloc[i])
                            loo.append(["ok with datas !!!! " , form_d_sumofdays.iloc[i],hh[0][i]])
                    
                        else:
                            print ("datas mismatch",form_d_sumofdays.iloc[i],hh[0][i])
                            dataframe_DD_table.objects.create(message="data mismatch",noofcountsofdaysheshehavebeenworked=hh[0][i],summaryofdays=form_d_sumofdays.iloc[i])
                            loo.append(["datasmismatch " , form_d_sumofdays.iloc[i],hh[0][i]])
           
                    print(loo)

                    matched_formd_working_days = pd.DataFrame (loo,columns=['message','summary of days','no of counts of days he/she have been worked'])
  
                    return matched_formd_working_days
            def myfunc2(self):
                    hh=[]
                    dataframe=[]
                    lioo=regwages.iloc[:,5]
                    print("*****************************")
                    print(len(lioo))
                    print(lioo)
                    print("*****************************")
                    hh.append(self.hh)
                    print (len(hh[0]))
                    for i in range(0,len(hh[0])):
                        print(i)
                        print(lioo.iloc[i],"  ***   ",hh[0][i])
                        if (lioo.iloc[i]==hh[0][i]):
                            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                         #   print(lioo.iloc[i],"    ",hh[0][i])
                           # data1="hi",lioo.iloc[i],hh[0][i]
                            dataframetable.objects.create(message="ok with datas",noofcountsofdaysheshehavebeenworked=lioo.iloc[i],reportworkingdays=hh[0][i])
                            File1.objects.filter(id=id).update(registerofwages_status="compiled")
                            query_results = dataframetable.objects.all();
                           # context = { 'query_results' : query_results }
                            dataframe.append(["ok with datas !!!! " ,hh[0][i], lioo.iloc[i]])
                           # return Response( context) 
                        else:
                          #  print ("datas mismatch")
                            dataframetable.objects.create(message="data mismatch",noofcountsofdaysheshehavebeenworked=lioo.iloc[i],reportworkingdays=hh[0][i])
                            dataframe.append(["data mismatch " ,hh[0][i],lioo.iloc[i]])
                       # return 
                    matched_formd_working_days = pd.DataFrame (dataframe,columns=['message','noofcountsofdaysheshehavebeenworked','reportworkingdays'])
                    print(matched_formd_working_days)
                    return matched_formd_working_days
    path = r"D:\\django new\\restpython\\django_project\\media\\combined.xlsx"
    writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
    print(muster)
    muster.to_excel(writer,sheet_name='sheet')
    regwages.to_excel(writer,sheet_name='sheet1')
    table=tablesdat()
    table.myfunc().to_excel(writer,sheet_name='sheet2')
    table.myfunc2().to_excel(writer,sheet_name='sheet3')
    response = HttpResponse(content_type='text/excel') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("D:\\django new\\restpython\\django_project\\media\\combined.xlsx")
   # writer = pd.ExcelWriter(response, engine = 'xlsxwriter')
    #muster.to_excel(writer,sheet_name='sheet')
   # regwages.to_excel(writer,sheet_name='sheet1')
    #table=tablesdat()
   # table.myfunc2()
   # 
    #response['X-Sendfile'] = smart_str()
    return response


class calculationViewset(viewsets.ModelViewSet):
    queryset=File1.objects.all()
    serializer_class=FileSerializer

    def list(self,request):
        ### AUDITOR GETTING API 
        return Response 
    
# @api_view(['POST'])

class updatedesc(APIView):


    def post(self,request):
    
        serializer_class = Fileupdate(data=request.data)
        if serializer_class.is_valid():
             serializer_class.save()
             print(serializer_class.data['clientname'])

             client=serializer_class.data['client_id']
             queryset=File1.objects.get(id=client)
             sta={"status":False}
             serializer_class=FileSerializer(instance=queryset,data=sta,partial=True)
            
             if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
             else:
                return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer_class.data)
class getNotify(viewsets.ModelViewSet):
    
    queryset=update.objects.all()
    serializer_class=Fileupdate
        