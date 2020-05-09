FAHRENHEIT = 'fahrenheit'
RANKINE = 'rankine'
KELVIN = 'kelvin'

TEMPERATURE_TYPES = {
    FAHRENHEIT,
    RANKINE,
    KELVIN,
}

ABSOLUTE_ZERO_TEMPERATURE = 273.15

def convertCelsiusToType(temperature, toType):
    # check if conversion to given type is available
    if not toType in TEMPERATURE_TYPES:
        raise Exception(f'Conversion from celsius to {toType} is not available.')
    
    if toType == FAHRENHEIT:
        return convertCelsiusToFahrenheit(temperature)
    
    if toType == RANKINE:
        return convertCelsiusToRankine(temperature)
    
    if toType == KELVIN: 
        return convertCelsiusToKelvin(temperature)


def convertCelsiusToFahrenheit(temperature):
    return temperature * 9 / 5 + 32


def convertCelsiusToRankine(temperature):
    return (temperature + ABSOLUTE_ZERO_TEMPERATURE) * 9 / 5


def convertCelsiusToKelvin(temperature):
    return temperature + ABSOLUTE_ZERO_TEMPERATURE

celsius = 32
toType = KELVIN
converted = convertCelsiusToType(celsius, toType)

print(f'{celsius} degrees celsius is {converted} degrees {toType}')      
         