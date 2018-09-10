# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExampleAppExampleModel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    count_of_something = models.IntegerField()
    some_boolean_value = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'example_app_example_model'

class WebPageAnnotationAppWebPageAnnotationModel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    korpus_id = models.IntegerField()
    hit = models.IntegerField()
    task = models.IntegerField()
    ad_mace = models.CharField(max_length=250)
    ad_annotation = models.CharField(max_length=250, default="-")
    cutoff_mace = models.CharField(max_length=250)
    cutoff_annotation = models.CharField(max_length=250, default="-")
    loading_mace = models.CharField(max_length=250)
    loading_annotation = models.CharField(max_length=250, default="-")
    pornographic_mace = models.CharField(max_length=250)
    pornographic_annotation = models.CharField(max_length=250, default="-")
    popup_mace = models.CharField(max_length=250)
    popup_annotation = models.CharField(max_length=250, default="-")
    captcha_mace = models.CharField(max_length=250)
    captcha_annotation = models.CharField(max_length=250, default="-")
    error_mace = models.CharField(max_length=250)
    error_annotation = models.CharField(max_length=250, default="-")

    class Meta:
        managed = True
        db_table = 'web_page_annotation_app_web_page_annotation_model'


class ExampleAppExampleModelCorpusViewerTags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    example_model = models.ForeignKey(ExampleAppExampleModel, models.DO_NOTHING)
    m_tag = models.ForeignKey('ViewerMTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'example_app_example_model_corpus_viewer_tags'
        unique_together = (('example_model', 'm_tag'),)


class ViewerMEntity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key_corpus = models.CharField(max_length=200)
    id_item = models.CharField(max_length=200)
    id_item_internal = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'viewer_m_entity'
        unique_together = (('key_corpus', 'id_item'),)


class ViewerMTag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key_corpus = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'viewer_m_tag'
        unique_together = (('key_corpus', 'name'),)


class ViewerMTagM2MEntity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    m_tag = models.ForeignKey(ViewerMTag, models.DO_NOTHING)
    m_entity = models.ForeignKey(ViewerMEntity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'viewer_m_tag_m2m_entity'
        unique_together = (('m_tag', 'm_entity'),)
