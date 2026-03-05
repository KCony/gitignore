import logging
import logging.handlers
#import zip_model as model
import zip_model_db as model
import zip_view_console as view
#import util as u
import util_metric as u
import authentication_db as auth
import authorization_db as athrz
import getpass

def process_loc():
    view.print_request_single_zip()
    zipcode = input()
    view.print_zip(zipcode)
    location = model.location_by_zip(zipcode)
    if len(location) > 0:
        view.print_location(zipcode, location)
    else:
        view.print_invalid_zip()


def process_zip():
    view.print_request_city()
    city = input()
    view.print_city(city)
    city = city.strip().title()
    view.print_request_state()
    state = input()
    view.print_state(state)
    state = state.strip().upper()
    zipcodes = model.zip_by_location((city, state))
    if len(zipcodes) > 0:
        view.print_zip_found(city, state, zipcodes)
    else:
        view.print_zip_not_found(city, state)


def process_dist():
    view.print_request_zip(1)
    zip1 = input()
    view.print_zip(zip1)
    # logger_main.info(f'Received the first ZIP {zip1}')
    logger_main.info(f'Received the first ZIP {zip1}')
    view.print_request_zip(2)
    zip2 = input()
    view.print_zip(zip2)
    # logger_main.info(f'Received the second ZIP {zip2}')
    logger_main.info(f'Received the second ZIP {zip2}')

    location1 = model.location_by_zip(zip1)
    location2 = model.location_by_zip(zip2)
    if len(location1) == 0 or len(location2) == 0:
        view.print_invalid_distance(zip1, zip2)
    else:
        dist = u.calculate_distance(location1, location2)
        view.print_distance(zip1, zip2, dist, u.UNITS)


def process_profile():
    result = auth.profile(username)
    view.print_profiles(result)

def process_reg():
    view.print_request_firstname()
    firstname = input()
    view.print_request_lastname()
    lastname = input()
    view.print_request_login()
    login = input()
    logger_main.info(f'Received login {login}')
    view.print_request_password()
    password = getpass.getpass()
    auth.register(firstname, lastname, login, password)
    
def process_login():
    while True:
        view.print_request_login()
        login = input()
        logger_main.info(f'Received login {login}')
        if login == '':
            view.print_login_error()
        else:
            break
    
    view.print_request_password()
    # TODO: replace input() with something more secure
    password = getpass.getpass()
    logger_main.info(f'Received password, not showing it here due to security considerations')
    auth.authenticate(login, password)
    return login
    

# logging.basicConfig(level=logging.ERROR)
rfh = logging.handlers.RotatingFileHandler(
    filename='zip_app.log',
    mode='a',
    maxBytes=250,#5*1024*1024,
    backupCount=9,
    encoding=None,
    delay=0
)
console = logging.StreamHandler()
# logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
#                     handlers=[rfh])
logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s', force=True,
                    level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S", handlers=[console, rfh])
logger_main = logging.getLogger('main')
console.setLevel(logging.INFO)
logger_aux = logging.getLogger('second_logger')

command = ""
username = ''
while command != 'end':
    view.print_prompt()
    command = input()
    # logging.info(f'Received command {command}')
    logger_main.info(f'Received command {command}')
    logger_aux.info(f'Received command {command}')
    view.print_command(command)
    command = command.strip().lower()
    
    if username == '':
        if not athrz.check_authorization(username, command):
            view.print_auth_error()
            continue
    else:
        if not athrz.check_authorization('', command):
            if auth.is_authenticated(username):
                if not athrz.check_authorization(username, command):
                    view.print_access_error()
                    continue
            else:
                view.print_auth_error()
                continue    
    
    if command == 'profile':
        process_profile()
    elif command == 'reg':
        username = process_reg()
    elif command == 'login':
        username = process_login()
    elif command == 'loc':
        process_loc()
    elif command == 'zip':
        process_zip()
    elif command == 'dist':
        process_dist()
    elif command != 'end':
        view.print_invalid_command()
    view.print_newline()
view.print_exit()
for handler in logger_main.handlers:
    logger_main.removeHandler(handler)
    handler.close()
logging.shutdown()
