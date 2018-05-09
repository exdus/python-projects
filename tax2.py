def calculate_tax(d):
    d1={}#Dictionary for calculated tax
    income=0#Value to deduct tax from(Value in income dictionary)

    """cheking for Key pairs"""
    while True:
        try:
            d1=d.keys()
            for keys in d.keys():
                income=d[keys]
                if (income >=0) and (income<=1000):
                    tax=(0*income)
                    d[keys]=tax#Updtae  the key after taxation
                elif (income > 1000) and (income <= 10000):
                    tax = (0.1 * (income-1000))
                    d[keys]=tax#Updtae  the key after taxation
                elif (income > 10000) and (income <= 20200):
                    tax = ((0.1*(10000-1000)) + (0.15*(income-10000)))
                    d[keys]=tax#Updtae  the key after taxation
                elif (income > 20200) and (income <= 30750):
                    tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(income-20200)))
                    d[keys]=tax#Updtae  the key after taxation
                elif (income > 30750) and (income <= 50000):
                    tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(income-30750)))
                    d[keys]=tax#Updtae  the key after taxation
                elif (income > 50000):
                    tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(50000-30750)) + (0.3*(income-50000)))
                    d[keys]=tax#Updtae  the key after taxation

                    """updating d1 dictionary"""
                    d[keys]=tax

                return d1
                break
        except(AttributeError,TypeError):
            raise ValueError('The input provided is not A dictionary')
d2={'Alex': 700,'Njuguna': 20500,'Kinuthia': 70000,'Anex': 700,'Ngori': 20500,'jumaa': 70000}
calculate_tax(d2)
