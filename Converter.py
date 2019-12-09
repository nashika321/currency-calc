rates = {
    "usd" : {
        "value" : 1,
        "symbol" : '$'
    },
    "htg" : {
        "value" : 96.15,
        "symbol" : 'G'
    },
    "can" : {
        "value" : 1.25,
        "symbol" : '$'
    },
    "eur" : {
        "value" : 0.85,
        "symbol" : '€'
    },
    "brl" : {
        "value" : 4.14,
        "symbol" : 'R$'
    },
    "jmd" : {
        "value" : 134,
        "symbol" : 'J$'
    },
    "bbd" : {
        "value" : 2,
        "symbol" : 'Bds$'
    
    }
}
#Logic
#print("200 jmd to CAD = %.3f" % ((200 / rates["inr"]) * rates["cad"]))
#print("3 eur to USD = %.3f" % (3 / rates["inr"]))

userQuery = {
    'currencyValue' : '',
    'fromCurrency' : '',
    'toCurrency' : ''
