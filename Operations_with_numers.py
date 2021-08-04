first_num = float(input("Zadej první číslo: "))
sec_num = float(input("Zadej druhé číslo: "))
symbol = input("Zadej operaci, kterou chceš provést: ")

def operation():
    """ Tato funkce vyhodnocuje operaci mezi dvěmi čísly"""
    if symbol == "+":
        result = first_num + sec_num
    
    if symbol == "-":
        result = first_num - sec_num
    
    if symbol == "/":
        result = first_num / sec_num
    
    if symbol == "*":
        result = first_num * sec_num

    return result


print(f"""
První číslo: {first_num}
Druhé číslo: {sec_num}
Operátor: {symbol}
{first_num} {symbol} {sec_num} = {operation()}
""")