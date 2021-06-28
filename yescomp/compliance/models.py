from django.db import models
from os import name
from django.db import models
from .validators import validate_file_extension

#login
class yes_complaines_login(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
#template 
class templates(models.Model):
    musterroll_template=models.FileField(blank=False, null=False)
    registerwages_template=models.FileField(blank=False, null=False)
#main table     
class File1(models.Model):
    clientname=models.CharField(max_length=100)
    contractorname=models.CharField(max_length=100)
    site_projectname=models.CharField(max_length=100)
    locationofwork=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    appropriategovt=models.CharField(max_length=100)
    zoneapplicable=models.CharField(max_length=100)
    industryapplicable=models.CharField(max_length=100)
    mmyy=models.CharField(max_length=100)
    salarytype=models.CharField(max_length=100)
    poagreementslagreementworkorder=models.FileField(blank=False, null=False)
    poagreementslagreementworkorder_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")
    labourLicenseUnderCLRA=models.FileField(blank=True, null=True)
    labourLicenseUnderCLRA_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    musterroll=models.FileField(blank=False, null=False,validators=[validate_file_extension])
    registerofwages=models.FileField(blank=False, null=False,validators=[validate_file_extension])
    bankstatement=models.FileField(blank=False, null=False)

    musterroll_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")
    registerofwages_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")
    bankstatement_status =models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    EPFchallan=models.FileField(blank=True, null=True)
    EPFchallan_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    EPFecr=models.FileField(blank=True, null=True)
    EPFecr_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    EPFarrearchallan=models.FileField(blank=True, null=True)
    EPFarrearchallan_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    EPFarrearecr=models.FileField(blank=True, null=True)
    EPFarrearecr_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    ESIdoubleverificationchallan=models.FileField(blank=True, null=True)
    ESIdoubleverificationchallan_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    ESIcontributionhistory=models.FileField(blank=True, null=True)
    ESIcontributionhistory_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    ESIsupplementarychallanarrear=models.FileField(blank=True, null=True)
    ESIsupplementarychallanarrear_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    ESIarrearcontributionhistory=models.FileField(blank=True, null=True)
    ESIarrearcontributionhistory_status=models.CharField(max_length=100,blank=True, null=True,default="uncompiled")

    WCpolicy=models.FileField(blank=True,null=True)
    WCpolicy_status=models.CharField(blank=True,max_length=100,null=True,default="uncompiled")
    status=models.BooleanField()

#Messsage
class update(models.Model):
    client_id=models.ForeignKey(File1,on_delete=models.CASCADE)
    clientname=models.CharField(max_length=100,blank=False,null=False)
    description=models.CharField(max_length=100,blank=False,null=False)

   #### DD muster roll & regwages dates check     
class dataframetable(models.Model):
     message=models.CharField(max_length=100,blank=False,null=True)
     noofcountsofdaysheshehavebeenworked=models.CharField(max_length=100,blank=False,null=True)
     reportworkingdays=models.CharField(max_length=100,blank=False,null=True)

 #### DD muster roll dates check   
class dataframe_DD_table(models.Model):
     message=models.CharField(max_length=100,blank=False,null=True)
     noofcountsofdaysheshehavebeenworked=models.CharField(max_length=100,blank=False,null=True)
     summaryofdays=models.CharField(max_length=100,blank=False,null=True)
    
