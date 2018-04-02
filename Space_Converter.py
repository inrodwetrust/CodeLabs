# this defines all the ratios from alt distances into miles
def convert_to_mi(measurement, amount):
    if measurement == 'km':
        return amount * 1.60934
    elif measurement == 'ft':
        return amount / 5280
    elif measurement == 'm':
        return amount / 1609.34

# this defines all the ratios from alt distances into kilometers
def convert_to_km(measurement, amount):
    if measurement == 'mi':
        return amount * 1.60934
    elif measurement == 'ft':
        return amount * 0.0003048
    elif measurement == 'm':
        return amount * 0.001

# this defines all the ratios from alt distances into feet
def convert_to_ft(measurement, amount):
    if measurement == 'mi':
        return amount * 5280
    elif measurement == 'km':
        return amount * 3280.84
    elif measurement == 'm':
        return amount * 3.28084

# this defines all the ratios from alt distances into meters
def convert_to_m(measurement, amount):
    if measurement == 'mi':
        return amount * 1609.34
    elif measurement == 'km':
        return amount * 1000
    elif measurement == 'ft':
        return amount * 0.3048

# this collects input for what conversion to execute
def responses():
    frm_meas = input("What measurement do you want to convert from? Enter as 'mi, km, ft, or m': ")
    amount = float(input('What is the amount you want to convert?: '))
    to_meas = input("What measurement do you want to convert to? Enter as 'mi, km, ft, or m': ")
    return frm_meas, to_meas, amount


# this defines how the output will print
print('You have activated the Space Converter.')
while True:
    frm_meas, to_meas, amount = responses()
    if to_meas == 'km':
        result = convert_to_km(frm_meas, amount)
    elif to_meas == 'mi':
        result = convert_to_mi(frm_meas, amount)
    elif to_meas == 'ft':
        result = convert_to_ft(frm_meas, amount)
    elif to_meas == 'm':
        result = convert_to_m(frm_meas, amount)
    else:
        print("No comprendo!")
        continue

    print("{} {} is {} {}".format(amount, frm_meas, result, to_meas))
    Quit = input('Would you like to convert another Space, but not time, continuum? Yes or No?: ').lower

    if Quit == 'no':
        print('Goodbye!')
        exit()
