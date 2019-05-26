from cypher import cypher, decypher

menu_text = "Wybierz operację (szyfrowanie, deszyfrowanie, wyjscie): "

operation = input(menu_text)
while operation.lower() != "wyjscie":
    if operation.lower() == "szyfrowanie":
        text = input("Podaj tekst:")
        print(cypher(text))
        operation = input(menu_text)
    elif operation.lower() == "deszyfrowanie":
        text = input("Podaj tekst:")
        print(decypher(text))
        operation = input(menu_text)
    else:
        print("Błędna operacja!")
        operation = input(menu_text)
print("Koniec")
