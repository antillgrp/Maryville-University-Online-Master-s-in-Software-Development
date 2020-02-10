import re
import math


def bool_strIsFloat(string):
    return not re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$', string) is None


def parseToFloatOrNAN(string):
    if bool_strIsFloat(string):
        return float(string)
    else:
        return math.nan


def validFloatInputRequest(strPrompt, strValidationPrompt="", predicateFunctValidator=lambda x: True):
    result = math.nan
    while True:
        print(strPrompt, end="")
        result = parseToFloatOrNAN(input(strValidationPrompt))
        if not math.isnan(result):
            if not callable(predicateFunctValidator):
                # print("predicateFunctValidator is not callable")
                return result
            validation = predicateFunctValidator(result)
            if not isinstance(validation, bool):
                # print("not isinstance(validation, bool)")
                return result
            elif validation:
                break
    return result
