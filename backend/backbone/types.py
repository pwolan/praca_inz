from django.db import models


class LogType(models.TextChoices):
    LOGIN = 'LOGIN', 'Login'
    CREATE = 'CREATE', 'Create'
    DELETE = 'DELETE', 'Delete'
    IMPORT = 'IMPORT', 'Import' # import 
    ADD_PARENT = 'ADD_PARENT', 'Add Parent' # Add parent to child
    HISTORY = 'HISTORY', 'History' # Who accessed history
    ADD_PERMISSION = 'ADD_PERMISSION', 'Add Permission' # Add temporary permission
    SIGN = 'SIGN', 'Sign' # Sign consent
    WARNING = 'WARNING', 'Warning'
    ERROR = 'ERROR', 'Error'
    INFO = 'INFO', 'Info'

class ConsentType(models.TextChoices):
    INFORMATION = 'INFORMATION', 'Information'
    BIOMETRIC = 'BIOMETRIC', 'Biometric'
    # etc.

class AccessType(models.IntegerChoices):
    NONE = 0, 'None'
    PARTIAL = 1 , 'Partial'
    FULL = 2 , 'Full'

class PermissionState(models.TextChoices):
    SLEEP = 'SLEEP', 'Sleep'
    ACTIVE = 'ACTIVE', 'Active'
    NOTIFY = 'NOTIFY', 'Notify'
    USED = 'USED', 'Used'