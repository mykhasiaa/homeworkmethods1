name = input("Введіть своє ім'я:")

if name.isspace() or name == "":
    print("Введено пробіли або порожньо.")
else:
    print(f"Привіт, {name}!")