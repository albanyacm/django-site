import os
import sys	
sys.path.append('/var/www/ualbanyacm')
os.environ['DJANGO_SETTINGS_MODULE'] = 'acm_web.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()