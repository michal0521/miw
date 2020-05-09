FAHRENHEIT = 'fahrenheit'
RANKINE = 'rankine'
KELVIN = 'kelvin'

TEMPERATURE_TYPES = {
    FAHRENHEIT,
    RANKINE,
    KELVIN,
}

ABSOLUTE_ZERO = 273.15

def convertCelsiusToType(temperature, toType=FAHRENHEIT):
    if not isinstance(temperature, int):
        raise Exception(f'Temperature has to be a digit')
    
    if not isinstance(toType, str):
        raise Exception(f'Conversion type has to be a string')
    
    # check if conversion to given type is available
    if not toType in TEMPERATURE_TYPES:
        raise Exception(f'Conversion from celsius to {toType} is not available')
    
    if toType == FAHRENHEIT:
        return convertCelsiusToFahrenheit(temperature)
    
    if toType == RANKINE:
        return convertCelsiusToRankine(temperature)
    
    if toType == KELVIN: 
        return convertCelsiusToKelvin(temperature)


def convertCelsiusToFahrenheit(temperature):
    return temperature * 9 / 5 + 32


def convertCelsiusToRankine(temperature):
    return (temperature + ABSOLUTE_ZERO) * 9 / 5


def convertCelsiusToKelvin(temperature):
    return temperature + ABSOLUTE_ZERO

celsius = 17
toType = FAHRENHEIT
try:
    converted = convertCelsiusToType(celsius, toType)

    print(f'{celsius} degrees celsius is {converted} degrees {toType}')      
except Exception as error:
    print(f'Couldn\'t convert the temperature: {error}.')

         