import os
os.chdir(os.path.dirname(os.path.abspath("Python v2 Support Files\\Main\\Wowza.txt")))
rouge = 1
while rouge == 1:
    delopen = input("del or open: ")
    if delopen == "open":
        with open('Wowza.txt','w') as message:
            message.write('Testing file for player configuration :3\n')
            message.write('User:')

        message = open('Wowza.txt','a')
        message.write('1\n')
        message.close()

        message_test = open('Wowza.txt','r')
        content = message_test.read()
        print(content)
        message_test.close()

    elif delopen =="del":
        message_file = 'Wowza.txt'

        if os.path.exists(message_file):
            os.remove(message_file)
            print("Message file removed")
            
        else: 
            print("There was no message file to remove")
