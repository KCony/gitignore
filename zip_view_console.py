import util as u

# From https://stackoverflow.com/questions/11180845/is-there-a-library-to-convert-integer-to-first-second-third
def ordinal(x):
    ordinals = [
        "first", "second", "third", "fourth", "fifth",
        "sixth", "seventh", "eighth", "ninth", "tenth",
        "eleventh", "twelfth"]
    return ordinals[x-1]

def print_auth_error():
    print('Authentication error. Please use "login" command to perform authentication')

def print_access_error():
    print('You are not authorized to access the requested command')

def print_profiles(profiles):
    print('Profile(s) data:')
    print(profiles)

def print_login_error():
    print('Invalid username entered. Username cannot be empty.')

def print_request_login():
    print('Enter your username => ', end='')

def print_request_password():
    print('Enter your password => ', end='')

def print_request_firstname():
    print('Enter your first name => ', end='')

def print_request_lastname():
    print('Enter your last name => ', end='')

def print_prompt():
    print("Command ('reg', 'login', 'profile', 'loc', 'zip', 'dist', 'end') => ", end='')

def print_command(command):
    print(command)

def print_invalid_command():
    print("Invalid command, ignoring")

def print_newline():
    print()

def print_exit():
    print("Done")

def print_request_single_zip():
    print('Enter a ZIP Code to lookup => ', end='')

def print_zip(zipcode):
    print(zipcode)

def print_location(zipcode, location):
    print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: {}'.
      format(zipcode, location[2], location[3], location[4],
             u.format_location((location[0], location[1]))))

def print_invalid_zip():
    print('Invalid or unknown ZIP Code')
    
def print_request_city():
    print('Enter a city name to lookup => ', end='')

def print_city(city):
    print(city)

def print_request_state():
    print('Enter the state name to lookup => ', end='')

def print_state(state):
    print(state)

def print_zip_found(city, state, zipcodes):
    print('The following ZIP Code(s) found for {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))

def print_zip_not_found(city, state):
    print('No ZIP Code found for {}, {}'.format(city, state))

def print_request_zip(ord):
    assert ord <= 12
    print(f'Enter the {ordinal(ord)} ZIP Code => ', end='')

def print_invalid_distance(zip1, zip2):
    print('The distance between {} and {} cannot be determined'.
              format(zip1, zip2))

def print_distance(zip1, zip2, dist, units):
    print('The distance between {} and {} is {:.2f} {}'.
              format(zip1, zip2, dist, units))
