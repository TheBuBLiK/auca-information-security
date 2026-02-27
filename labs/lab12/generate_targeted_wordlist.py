name = 'amantai'
surname = 'Bublik'
year = '2005'
words = {
    name.lower(),
    name.capitalize(),
    surname.lower(),
    f"{name}{year}",
    f"{name}{year}!",
    f"{name.capitalize()}{year}",
    f"{name.capitalize()}{year}!",
    f"{surname}{year}",
    f"{name.lower()}{year}",
    f"{name[0].lower()}{surname.lower()}{year}",
    f"{name}{year}!",
}
with open('targeted_passwords.txt', 'w', encoding='utf-8') as f:
    for w in sorted(words):
        f.write(w + '\n')
