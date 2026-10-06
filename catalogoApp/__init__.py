from django.db.backends.mysql.base import DatabaseWrapper

def check_database_version_supported(self):
    pass

DatabaseWrapper.check_database_version_supported = check_database_version_supported

original_get_new_connection = DatabaseWrapper.get_new_connection
def get_new_connection(self, connection_params):
    connection = original_get_new_connection(self, connection_params)
    self.features.can_return_columns_from_insert = False
    return connection

DatabaseWrapper.get_new_connection = get_new_connection