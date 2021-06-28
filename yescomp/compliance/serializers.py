
from django.db.models import fields
from rest_framework import serializers


from .models import  dataframetable, templates, update,yes_complaines_login
from .models import File1,update

class tempSerializer(serializers.ModelSerializer):
  class Meta():
    model = templates
    fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File1
    fields = '__all__'

class FileSerializer2(serializers.ModelSerializer):
      class Meta():
          model = File1
          fields = ['clientname','contractorname','site_projectname',
          'locationofwork','state' ,'appropriategovt','zoneapplicable','industryapplicable',
          'mmyy', 'salarytype', 'poagreementslagreementworkorder_status','labourLicenseUnderCLRA_status',
          'musterroll_status','registerofwages_status','bankstatement_status' , 'EPFchallan_status',
          'EPFecr_status', 'EPFarrearchallan_status','EPFarrearecr_status','ESIdoubleverificationchallan_status',
          'ESIcontributionhistory_status',  'ESIsupplementarychallanarrear_status',   'ESIarrearcontributionhistory_status',
           'WCpolicy_status']

# class get_db(serializers.ModelSerializer):
#     class Meta:
#         model=task1
#         fields='__all__'
class yes(serializers.ModelSerializer):
    class Meta:
        model=yes_complaines_login
        fields='__all__'
# class ocr(serializers.ModelSerializer):
#     class Meta:
#         model=ocrregister
#         fields='__all__'
class Fileupdate(serializers.ModelSerializer):
      class Meta():
           model = update
           fields = '__all__'
     
class MyModel(serializers.ModelSerializer):
    class Meta():
          model=dataframetable
          fields='__all__'
       