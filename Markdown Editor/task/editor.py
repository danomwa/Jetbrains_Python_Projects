while True:
    x = input("Choose a formatter: ")
    if x == '!help':
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
              "Special commands: !help !done")
    elif x == "!done":
        break
    elif x in ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list',
               'ordered-list', 'new-line']:
        continue
    else:
        print("Unknown formatting type or command")
