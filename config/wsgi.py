import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv  

load_dotenv('/home/hostdev/www/Portfolio-Website/.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
