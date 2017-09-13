from django.contrib import admin

# Register your models here.
from .models import Tilaus

import sys
reload(sys)
sys.setdefaultencoding('utf8')

admin.site.register(Tilaus)

