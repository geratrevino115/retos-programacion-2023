## Cambio de lenguaje 

leet = {
    #diccionario minusculas
    "a":"4",  "b":"|3",  "c":"[", "d":")", "e":"3", "f":"|=", "g":"&", "h":"#", "i":"1",
    "j":",_|", "k":">|", "l":"1", "m":"/\\/\\", "n":"^/", "o":"0", "p":"|*", "q":"(_,)", "r":"I2",
    "s":"5", "t":"7", "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"j", "z":"2",
    #diccionario numeros
    "0":"o", "1":"L", "2":"R", "3":"E", "4":"A", "5":"S", "6":"b", "7":"T", "8":"B", "9":"g",
    #diccionario mayusculas
    "A":"@", "B":"8", "C":"<", "D":"1)", "E":"€", "F":"|*", "G":"6", "H":"4", "I":"|", "J":"¿", "K":"|{",
    "L":"][", "M":"^^", "N":"?", "O":"<>", "P":"|?", "Q":"(0,)", "R":"|2", "S":"§", "T":"+", "U":"µ", "V":"\|",
    "W":"uu", "X":")(", "Y":"¥", "Z":"2", ' ':' '}

def traductor(texto: str, leunguaje: dict):

    codec = ""

    for letra in texto:
        if letra in leunguaje:
            codec += leunguaje[letra]

    return codec


if __name__ == "__main__":
    texto = input("Texto: ")
    
    n_texto = traductor(texto, leet)

    print(f"Tu nuevo texto es: {n_texto}")

