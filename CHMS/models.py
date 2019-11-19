# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblBasesForDiagnosis(models.Model):
    idtbl_bases_for_diagnosis = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tbl_bases_for_diagnosis'


class TblCattle(models.Model):
    idtbl_cattle = models.AutoField(db_column='idtbl_Cattle', primary_key=True)  # Field name made lowercase.
    date_of_birth = models.CharField(db_column='Date_of_birth', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tbl_status_idtbl_status = models.ForeignKey('TblStatus', models.DO_NOTHING, db_column='tbl_Status_idtbl_Status')  # Field name made lowercase.
    tbl_cattle_gender_idtbl_cattle_gender = models.ForeignKey('TblCattleGender', models.DO_NOTHING, db_column='tbl_cattle_gender_idtbl_cattle_gender')
    tbl_heard_idtbl_heard = models.ForeignKey('TblHeard', models.DO_NOTHING, db_column='tbl_heard_idtbl_heard')
    tbl_normal_sign_idtbl_normal_sign = models.ForeignKey('TblNormalSign', models.DO_NOTHING, db_column='tbl_normal_sign_idtbl_Normal_Sign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle'


class TblCattleDesease(models.Model):
    idtbl_cattle_desease = models.AutoField(db_column='idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease'


class TblCattleDeseaseHasTblDiseaseSysmptom(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_disease_sysmptom_idtbl_disease_sysmptom = models.ForeignKey('TblDiseaseSysmptom', models.DO_NOTHING, db_column='tbl_disease_sysmptom_idtbl_Disease_sysmptom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_disease_sysmptom'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_disease_sysmptom_idtbl_disease_sysmptom'),)


class TblCattleDeseaseHasTblDrug(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_drug_idtbl_drug = models.ForeignKey('TblDrug', models.DO_NOTHING, db_column='tbl_Drug_idtbl_Drug')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_drug'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_drug_idtbl_drug'),)


class TblCattleGender(models.Model):
    idtbl_cattle_gender = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tbl_cattle_gender'


class TblDetection(models.Model):
    idtbl_detection = models.IntegerField(db_column='idtbl_Detection', primary_key=True)  # Field name made lowercase.
    tbl_detectioncol = models.CharField(db_column='tbl_Detectioncol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_detection'


class TblDiseaseSysmptom(models.Model):
    idtbl_disease_sysmptom = models.AutoField(db_column='idtbl_Disease_sysmptom', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_disease_sysmptom'


class TblDistrict(models.Model):
    idtbl_district = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    tbl_province_tbl_provincecol = models.ForeignKey('TblProvince', models.DO_NOTHING, db_column='tbl_province_tbl_provincecol')

    class Meta:
        managed = False
        db_table = 'tbl_district'


class TblDrug(models.Model):
    idtbl_drug = models.AutoField(db_column='idtbl_Drug', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_drug'


class TblFarm(models.Model):
    idtbl_farm = models.AutoField(db_column='idtbl_Farm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    tbl_location_idtbl_location = models.ForeignKey('TblLocation', models.DO_NOTHING, db_column='tbl_location_idtbl_location')

    class Meta:
        managed = False
        db_table = 'tbl_farm'


class TblHeard(models.Model):
    idtbl_heard = models.AutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    tbl_farm_idtbl_farm = models.ForeignKey(TblFarm, models.DO_NOTHING, db_column='tbl_farm_idtbl_Farm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_heard'


class TblInfectionSource(models.Model):
    idtbl_cause = models.AutoField(primary_key=True)
    desciption = models.CharField(db_column='Desciption', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_infection_source'


class TblInfectionSourceHasTblCattleDesease(models.Model):
    tbl_infection_source_idtbl_cause = models.ForeignKey(TblInfectionSource, models.DO_NOTHING, db_column='tbl_infection_source_idtbl_cause', primary_key=True)
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_cattle_Desease_idtbl_Cattle_Desease')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_infection_source_has_tbl_cattle_desease'
        unique_together = (('tbl_infection_source_idtbl_cause', 'tbl_cattle_desease_idtbl_cattle_desease'),)


class TblLocation(models.Model):
    idtbl_location = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tbl_district_idtbl_district = models.ForeignKey(TblDistrict, models.DO_NOTHING, db_column='tbl_district_idtbl_district')

    class Meta:
        managed = False
        db_table = 'tbl_location'


class TblLogin(models.Model):
    idtbl_login = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', unique=True, max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_login'


class TblNormalSign(models.Model):
    idtbl_normal_sign = models.AutoField(db_column='idtbl_Normal_Sign', primary_key=True)  # Field name made lowercase.
    temparature_min = models.FloatField(db_column='Temparature_min')  # Field name made lowercase.
    temperature_max = models.FloatField(db_column='Temperature_max')  # Field name made lowercase.
    respiration_min = models.IntegerField(db_column='Respiration_min')  # Field name made lowercase.
    respiration_max = models.IntegerField(db_column='Respiration_max')  # Field name made lowercase.
    pulse_max = models.IntegerField(db_column='Pulse_max')  # Field name made lowercase.
    pulse_min = models.IntegerField(db_column='Pulse_min')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_normal_sign'


class TblNotifications(models.Model):
    idtbl_notifications = models.AutoField(db_column='idtbl_Notifications', primary_key=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=45)  # Field name made lowercase.
    submission_date = models.CharField(db_column='Submission_date', max_length=45)  # Field name made lowercase.
    tbl_user_level_idtbl_user_level = models.IntegerField(db_column='tbl_User_level_idtbl_User_level')  # Field name made lowercase.
    read = models.IntegerField(db_column='Read')  # Field name made lowercase.
    broadcasted = models.IntegerField(db_column='Broadcasted')  # Field name made lowercase.
    tbl_farm_idtbl_farm = models.ForeignKey(TblFarm, models.DO_NOTHING, db_column='tbl_Farm_idtbl_Farm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_notifications'


class TblProvince(models.Model):
    tbl_provincecol = models.CharField(primary_key=True, max_length=45)
    province = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tbl_province'


class TblReadings(models.Model):
    idtbl_readings = models.AutoField(primary_key=True)
    tempareture = models.FloatField()
    respiration_count = models.IntegerField()
    heart_count = models.IntegerField()
    tbl_cattle_idtbl_cattle = models.ForeignKey(TblCattle, models.DO_NOTHING, db_column='tbl_Cattle_idtbl_Cattle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_readings'


class TblStatus(models.Model):
    idtbl_status = models.AutoField(db_column='idtbl_Status', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_status'


class TblUser(models.Model):
    idtbl_user = models.AutoField(db_column='idtbl_User', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(db_column='Email_address', max_length=200)  # Field name made lowercase.
    owner = models.IntegerField()
    image_url = models.CharField(max_length=45, blank=True, null=True)
    tbl_farm_idtbl_farm = models.ForeignKey(TblFarm, models.DO_NOTHING, db_column='tbl_Farm_idtbl_Farm')  # Field name made lowercase.
    tbl_login_idtbl_login = models.ForeignKey(TblLogin, models.DO_NOTHING, db_column='tbl_login_idtbl_login')

    class Meta:
        managed = False
        db_table = 'tbl_user'
