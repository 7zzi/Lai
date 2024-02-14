x = open(f"misc/logging.isEnabled/1204867121364996127.txt", 'r+')
print(x.readline())
if (str(x.readline())) == "false":
    print(x.readline())
    x.truncate(0)
    x.seek(0)

    x.write('1')

    print('logging enabled. #logs')

if (x.readline()) == 'true':
    print('logging is already enabled! #logs')