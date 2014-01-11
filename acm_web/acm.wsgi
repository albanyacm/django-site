import os
import sys	
sys.path.append('/var/www/ualbanyacm')
sys.path.append('/var/www/ualbanyacm/acm_web')
os.environ['DJANGO_SETTINGS_MODULE'] = 'acm_web.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()