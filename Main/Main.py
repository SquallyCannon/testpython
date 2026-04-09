import random
import math
import Testmain
import os
os.chdir(os.path.dirname(os.path.abspath("Python v2 Support Files\\Main\\Wowza.txt")))
message_file2 = 'Wowza.txt'
if os.path.exists(message_file2):
    with open('Wowza.txt','r') as message2:
        linesm2 = [line.strip() for line in message2]
        glb_highest_score = int(linesm2[1].split(':')[1].strip())
        glb_highest_round = int(linesm2[2].split(':')[1].strip())
else:
    glb_highest_score = 0
    glb_highest_round = 0

runrandom = "n" #input("Random? y/n: ")
rank = 30
score = 50000
ranvalue = 100
sscore = score

game_state = True
base_game_lives = 3 #int(input('Number of lives: '))
game_end = 1000 #int(input('Number of rounds: '))
rankmax = 30
high_round = 0
high_score = 0
highest_round = 0
highest_score = 0
print("")
while game_state == True:
    game_lives = base_game_lives

    game_round = 0
    Lose_streak = 0
    Elife_streak = 0
    Loss_count = 0
    high_round = 0
    high_score = 0
    if runrandom == "y":
        score = 0
    else:
        score = sscore

    if runrandom == "y":
        rank = random.randint(1, rankmax)



    while game_lives > 0:
        if game_round >= 10 and not runrandom == "y":
            addlife = ((9)*20000)+((game_round-9)*40000)
            beatlv = ((9)*10000)+((game_round-9)*20000)
        elif game_round >= 100 and not runrandom == "y":
            addlife = ((9)*20000)+((90)*40000)+((game_round-99)*80000)
            beatlv = ((9)*10000)+((90)*20000)+((game_round-99)*40000)
        elif game_round >= 1000 and not runrandom == "y":
            addlife = ((9)*20000)+((90)*40000)+((900)*80000)+((game_round-999)*160000)
            beatlv = ((9)*10000)+((90)*20000)+((900)*40000)+((game_round-999)*80000)
        else:
            addlife = ((game_round+1)*20000)
            beatlv = ((game_round+1)*10000)

        if runrandom == "y":
            score += random.randint(1000, 50000)
        else:
            score = sscore
        if runrandom == "y":
            ranvalue = random.randint(0, 100)

        print(f"Base Score:{score} Rank:{rank} ")
        
        bonus = (score/rankmax)*rank
        if bonus > score:
            bonus = score
        
        ranm = ranvalue/25+1
        Lossm = Loss_count/1000+1
        scoreb = score + bonus
        rankm = math.sqrt(rank+1)
        scorem = 1

        if 10000 > score >= 5000:
            scorem = score/5000
        elif 20000 > score >= 10000:
            scorem = (score/10000)+1
        elif 50000 > score >= 20000:
            scorem = (score/20000)+2
        elif score >= 50000:
            scorem = (score/50000)+3.5

        print(f'score self mult:{scorem}')

        total_score = math.ceil(scoreb*rankm*ranm*Lossm*scorem)
        score -= beatlv
        if score < 1:
            score = 0
        print(f"Bonus:{int(bonus)}")
        print(f"Final Score:{total_score}",)
        print(f"rank multipler:{rankm}")
        print(f"random value:{ranvalue}")

        if total_score >= addlife:
            game_round += 1
            Elife_streak += 1
            game_lives += Elife_streak
            Lose_streak = 0
            print(f"Lives +{Elife_streak}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"Lives remaining:{int(game_lives)}")
            print(f"Round:{game_round}")

        elif total_score < beatlv:
            game_round += 1
            Lose_streak += 1
            Elife_streak = 0
            Loss_count += 1
            game_lives -= Lose_streak
            print(f"you were {beatlv-total_score} points off of victory")
            print(f"Lives -{Lose_streak}-------------------------------------------------------------")
            if game_lives < 1:
                game_lives = 0
            print(f"Lives remaining:{int(game_lives)}")
            print(f"Round:{game_round}")

        else:
            game_round += 1
            Lose_streak = 0
            Elife_streak = 0
            print(f"you were {addlife-total_score} points off from an life bonus")
            print("Restart #####################################")
            print(f"Lives remaining:{int(game_lives)}")
            print(f"Round:{game_round}")


        print(f"bonus req:{addlife} beat req:{beatlv}")
        print(f"Lose streak:{Lose_streak}")
        print(f"Extra Life streak:{Elife_streak}")
        print("")

        if total_score > high_score:
            high_score = total_score
        if game_round > high_round:
            high_round = game_round

        if game_round <= game_end and game_lives < 1:
            print("Game over")
            print(f"loss count:{Loss_count}")
            print("")
            break
        elif game_round >= game_end:
            print("Congrats, you have won.")
            print(f"loss count:{Loss_count}")
            print("")
            break
    


    if high_round > highest_round:
        highest_round = high_round
    if high_score > highest_score:
            highest_score = high_score

    print("Thank you for playing.")
    print(f"Your highest score was: {high_score}")
    print(f"Your highest round was: {high_round}")
    print(f"Your highest score this session was: {highest_score}")
    print(f"Your highest round this session was: {highest_round}")

    restarter = input("restart? y/n: ")
    if restarter == "y":
        game_lives = base_game_lives

    elif highest_score >= glb_highest_round and highest_round > glb_highest_round:

        delopen = input("Save score(s), Delete data(del), Nothing(n), Restart(r): ")
        
        if delopen == "s" or delopen == "save":
            with open('Wowza.txt','w') as message:
                message.write('Testing file for player score storage :3\n')
                message.write(f'User latest saved score: {highest_score}\n')
                message.write(f'User latest saved round: {highest_round}')
            
            break

        elif delopen == "del":
            message_file = 'Wowza.txt'

            if os.path.exists(message_file):
                os.remove(message_file)
                print("Message file removed")
                        
            else: 
                print("There was no message file to remove")
            
            break

        elif delopen == "r":
            game_lives = base_game_lives
        
        else:
            break
    
    else:
        delopen = input("Delete data(del), Nothing(n), Restart(r): ")

        if delopen =="del":
            message_file = 'Wowza.txt'

            if os.path.exists(message_file):
                os.remove(message_file)
                print("Message file removed")
                        
            else: 
                print("There was no message file to remove")
            
            break

        elif delopen == "r":
            game_lives = base_game_lives
        
        else:
            break
