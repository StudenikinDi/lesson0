calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    info = len(string), string.upper(), string.lower()
    count_calls()
    return info
def is_contains(string, list_to_search):
    count_calls()
    result = True
    for i in range(len(list_to_search)):
        if string.lower() in str(list_to_search[i]).lower():
            result = True
        else:
            result = False
    return result
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)