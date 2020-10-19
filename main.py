def reb():
    print("reb")
def rec():
    print("rec")

commands = ["reb","rec"]

cli = input('func name:')
for i in range(0, len(commands)):
    if commands[i] == str(cli):
        globals()[str(cli)]()