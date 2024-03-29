from pathlib import Path

APP_ID = 'Rundsoft.foogie.desktop.2023.4.4-dev'

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = BASE_DIR / 'resources'
ICONS_DIR = RESOURCES_DIR / 'icons'
SOURCES_DIR = BASE_DIR / 'oldsrc'
LAYOUTS_DIR = SOURCES_DIR / 'gui'

API_VERSION = 1

SERVER_URL = f"http://127.0.0.1:8000/api/v{API_VERSION}/"
AUTH_URL = SERVER_URL + "auth/"
REGISTER_URL = AUTH_URL + "sign-up/"
LOGIN_URL = AUTH_URL + "sign-in/"
LOGOUT_URL = AUTH_URL + "sign-out/"
ME_URL = AUTH_URL + "me/"
USERS_URL = SERVER_URL + "users/"
PAYMENTS_URL = SERVER_URL + "payments/"
GAMES_URL = SERVER_URL + 'games/'
BUILDS_URL = SERVER_URL + 'builds/'
PLATFORMS_URL = SERVER_URL + 'platforms/'
COMPANIES_URL = SERVER_URL + 'companies/'
LIBRARY_URL = SERVER_URL + 'library/'
CART_URL = SERVER_URL + 'cart/'
WISHLIST_URL = SERVER_URL + 'wishlist/'
