APP_LABEL = 'photos'
APP_DATABASE = 'photo_db'

class DatabaseRouter(object):
    """
    A router to control all database operations on models in the CTG assessment application.
    """

    def lookup_database_for_app_label(self, app_label):
        if app_label == APP_LABEL:
            return APP_DATABASE
        return None

    def lookup_database_for_model(self, model):
        return self.lookup_database_for_app_label(model._meta.app_label)


    def db_for_read(self, model, **hints):
        return self.lookup_database_for_model(model)


    def db_for_write(self, model, **hints):
        return self.lookup_database_for_model(model)


    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label == APP_LABEL or obj2._meta.app_label == APP_LABEL:
    #        return True
    #     return None

    def allow_relation(self, obj1, obj2, **hints):
        print ('ALLOW?: ' + obj1._meta.app_label + ' - ' + obj2._meta.app_label)
        if obj1._meta.app_label == APP_LABEL and obj2._meta.app_label == APP_LABEL:
            # allow if both models in ctg database
            print ('true')
            return True
        elif obj1._meta.app_label != APP_LABEL and obj2._meta.app_label != APP_LABEL:
            # if neither is in ctg database we don't care
            print ('none')
            return None
        else:
            # but if one is then disallow a cross database link
            print ('false')
            return False


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print('app:' + app_label + ', db:' + db)
        if app_label == APP_LABEL:
            return db == APP_DATABASE
        elif db == APP_DATABASE:
            # do not save anything in ctg database that is not from ctg model
            return False

        return None
