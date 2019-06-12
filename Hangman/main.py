from string import ascii_lowercase
from words import get_random_word

def get_attempts_allowed():
    # Get number of attempts allowed
    while True:
        attempt_count = input('Enter turn count 1-5 = ') or None
        try:
            attempt_count = int(attempt_count)
            if 1 <= attempt_count <= 5:
                return attempt_count
            else:
                print('{0} is out of 1-5 range'.format(attempt_count))
        except e:
            print('{0} is not int and batween 1-5 range'.format(attempt_count))

get_try_count = get_attempts_allowed()
print('Try count is = {0}'.format(get_try_count))