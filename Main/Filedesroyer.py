import os
import random
os.chdir(os.path.dirname(os.path.abspath("Python v2 Support Files\\Filefuller\\Ah")))
number_file = 0
filelooper = 1
print("Your current directory is:", os.getcwd())
while filelooper == 1:
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')
    with open('Wildtest.txt','w') as message:
        message.write('Testing file for player score storage :3\n')
        message.write(f'User latest saved score:\n')
        message.write(f'User latest saved round:')
    os.rename('Wildtest.txt', f'{random.randint(1000, 50000)}.txt')

for text_file in os.listdir():
    if text_file.endswith('.txt'):
        print(text_file)