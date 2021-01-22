# age ist ein string in diesem moment
age:str = input("Geben Sie Ihr Alter ein: ")
# hier weisen wir age neu zu und konvertieren den Wert in einen Integer, wir gehe
# einfach mal davon aus dass die user:in eine zahl eingegeben hat
#
# Da wir hier den datentyp genau kenn (integer), können wir age:int schreiben
age:int = int(age)

grad_der_behinderung:str = input("Geben Sie Ihren Behindertengrad ein: ")
grad_der_behinderung:int = int(grad_der_behinderung)

verschwendete_zeit:str = input("Wie lange sind Sie schon im Unternehmen tätig?: ")
verschwendete_zeit:int = int(verschwendete_zeit)

# standardwert, wir weisen ihn neu zu je nachdem welche vorraussetungen erfüllt sind
urlaubstage:int = 26

if age < 18:
    urlaubstage:int = 30
elif age > 55:
    urlaubstage:int = urlaubstage + 2

if grad_der_behinderung > 50:
    urlaubstage:int = urlaubstage + 5

print(urlaubstage)
