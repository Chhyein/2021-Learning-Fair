import random

print('Round 1. 음식 맞추기 게임!')
print()
print('제가 생각하는 음식을 맞춰보세요.')
print()
print('맞출 수 있는 기회는 1번입니다.')

food = ['라면', '치킨', '삼겹살']
food1 = random.choice(food)
print('[라면🍜, 치킨🍗, 삼겹살🥓, 피자🍕, 햄버거🍔, 도시락🍱]')
print()
if food1 == food[0]:
    print('1. 분식류 입니다.')
    print('2. 뜨겁게도 차갑게도 먹는 음식입니다.')
    print('3. 김치와 잘 어울립니다.')
    print('4. 간단하게 해먹을 수 있는 음식입니다.')
    print('5. 비교적 저렴한 가격입니다.')
    print()
    guess = str(input('제가 생각하는 음식은 무엇일까요? '))
    if guess == food[0]:
        print('정답입니다.🤗 제가 생각하는 음식은 <%s>입니다.' % (food[0]))
        print()
        import random
        print('Round 2. 가위바위보 게임!')
        print()
        print('기회는 무제한입니다. 컴퓨터를 이겨보세요.')
        print()
        print('✌는 숫자 0, ✊는 숫자 1, 🖐는 숫자 2 입니다.')
        print()
        
        computer = random.randint(0, 2)
        
        while True:
            user = int(input( '0(✌), 1(✊), 2(🖐) 중에 하나를 선택하세요. ' ))
            if user in [0,1,2]:
                if \
                   (computer == user + 1) or \
                   (computer == 0 and user == 2):
                   print('컴퓨터:', computer)
                   print('내가 졌다!')
                   play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                   if play_again.lower().startswith('네'):
                       continue
                   else:
                       print('게임종료')
                       break
                elif \
                     (computer == user):
                     print('컴퓨터:', computer)
                     print('비겼다!')
                     play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                     if play_again.lower().startswith('네'):
                         continue
                     else:
                         print('게임종료')
                         break
                     
                else:
                    print('컴퓨터:', computer)
                    print('내가 이겼다!🤗')
                    print()

                    import random
                    print('Round 3. 🍦배스킨라빈스 31 게임!')
                    print()
                    print('31을 먼저 말하는 사람이 지는 게임입니다.')
                    while True:
                        turn = int(input('시작할 순서를 정하세요. (선공 1, 후공 0 입력): '))
                        if turn in [0, 1]:
                            break
                        else:
                            print("잘못된 입력입니다. 다시 입력해주세요.")
                    
                    first = 0
                    later = 1

                    while first < 31:
                        if later % 2 == turn:
                            print()
                            print('참가자의 순서')
                            while True:
                                num = int(input('1~3 중 말할 숫자의 개수를 입력하세요: '))
                                if num in [1, 2, 3]:
                                    break
                                else:
                                    print("잘못된 입력입니다. 다시 입력해주세요.")
                           
                            for i in range(num):
                                first  += 1
                                print("참가자: '{0}'!!!".format(first))
                        else:
                            print('컴퓨터의 순서')
                            num = random.randint(1, 3)
                            for i in range(num):
                                first  += 1
                                print("컴퓨터: '{0}'!!!".format(first))
                        later += 1
                    if later % 2 == turn:
                        print('🎉축하합니다!😊 3개의 Round 모두 승리했습니다!!🎉')
                        break
                    else:
                        print('아쉽네요! Round 3에서 패배했습니다!!😢')
                        break
            
    else:
        print('틀렸습니다. Round 1에서 패배했습니다!!😢')
            

if food1 == food[1]:
    print('1. 야식하면 떠오르는 음식입니다.')
    print('2. 튀김류의 음식입니다.')
    print('3. 맥주랑 잘 어울립니다.')
    print('4. 다양한 맛을 즐길 수 있습니다.')
    print('5. 다양한 프랜차이즈 음식점이 있습니다.')
    print()
    guess = str(input('제가 생각하는 음식은 무엇일까요? '))
    if guess == food[1]:
        print('정답입니다.🤗 제가 생각하는 음식은 <%s>입니다.' % (food[1]))
        print()
        import random
        print('round2. 가위바위보 게임!')
        print()
        print('기회는 무제한입니다. 컴퓨터를 이겨보세요.')
        print()
        print('✌는 숫자 0, ✊는 숫자 1, 🖐는 숫자 2 입니다.')
        print()

        computer = random.randint(0, 2)
        
        while True:
            user = int(input( '0(✌), 1(✊), 2(🖐) 중에 하나를 선택하세요. ' ))
            if user in [0,1,2]:
                if \
                   (computer == user + 1) or \
                   (computer == 0 and user == 2):
                   print('컴퓨터:', computer)
                   print('내가 졌다!')
                   play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                   if play_again.lower().startswith('네'):
                       continue
                   else:
                       print('게임종료')
                       break
                elif \
                     (computer == user):
                     print('컴퓨터:', computer)
                     print('비겼다!')
                     play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                     if play_again.lower().startswith('네'):
                         continue
                     else:
                         print('게임종료')
                         break
                     
                else:
                    print('컴퓨터:', computer)
                    print('내가 이겼다!🤗')
                    print()
                    
                    
                    print('Round 3. 🍦배스킨라빈스 31 게임!')
                    print()
                    print('31을 먼저 말하는 사람이 지는 게임입니다.')
                    while True:
                        turn = int(input('시작할 순서를 정하세요. (선공 1, 후공 0 입력): '))
                        if turn in [0, 1]:
                            break
                        else:
                            print("잘못된 입력입니다. 다시 입력해주세요.")
                    
                    first = 0
                    later = 1

                    while first < 31:
                        if later % 2 == turn:
                            print()
                            print('참가자의 순서')
                            while True:
                                num = int(input('1~3 중 말할 숫자의 개수를 입력하세요: '))
                                if num in [1, 2, 3]:
                                    break
                                else:
                                    print("잘못된 입력입니다. 다시 입력해주세요.")
                           
                            for i in range(num):
                                first  += 1
                                print("참가자: '{0}'!!!".format(first))
                        else:
                            print('컴퓨터의 순서')
                            num = random.randint(1, 3)
                            for i in range(num):
                                first  += 1
                                print("컴퓨터: '{0}'!!!".format(first))
                        
                    if later % 2 == turn:
                        print('🎉축하합니다!😊 3개의 Round 모두 승리했습니다!!🎉')
                        break
                    else:
                        print('아쉽네요! Round 3에서 패배했습니다!!😢')
                        break
            
    else:
        print('틀렸습니다. Round 1에서 패배했습니다!!😢')
            

if food1 == food[2]:
    print('1. 이 음식을 파는 가게가 많이 있습니다.')
    print('2. 기름이 많은 음식입니다.')
    print('3. 배달도 가능합니다.')
    print('4. 폭 넓은 요리에 쓰입니다.')
    print('5. 채소와 조합이 좋습니다.')
    print()
    guess = str(input('제가 생각하는 음식은 무엇일까요? '))
    if guess == food[2]:
        print('정답입니다.🤗 제가 생각하는 음식은 <%s>입니다.' % (food[2]))
        print()
        import random
        print('Round 2. 가위바위보 게임!')
        print()
        print('기회는 무제한입니다. 컴퓨터를 이겨보세요.')
        print('✌는 숫자 0, ✊는 숫자 1, 🖐는 숫자 2 입니다.')
        print()
        
        computer = random.randint(0, 2)
        
        while True:
            user = int(input( '0(✌), 1(✊), 2(🖐) 중에 하나를 선택하세요. ' ))
            if user in [0,1,2]:
                if \
                   (computer == user + 1) or \
                   (computer == 0 and user == 2):
                   print('컴퓨터:', computer)
                   print('내가 졌다!')
                   play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                   if play_again.lower().startswith('네'):
                       continue
                   else:
                       print('게임종료')
                       break
                elif \
                     (computer == user):
                     print('컴퓨터:', computer)
                     print('비겼다!')
                     play_again = input('게임을 다시 진행하겠습니까?(네/아니오) ')
                     if play_again.lower().startswith('네'):
                         continue
                     else:
                         print('게임종료')
                         break
                     
                else:
                    print('컴퓨터:', computer)
                    print('내가 이겼다!🤗')
                    print()

                    import random
                    print('Round 3. 🍦배스킨라빈스 31 게임!')
                    print()
                    print('31을 먼저 말하는 사람이 지는 게임입니다.')
                    while True:
                        turn = int(input('시작할 순서를 정하세요. (선공 1, 후공 0 입력): '))
                        if turn in [0, 1]:
                            break
                        else:
                            print("잘못된 입력입니다. 다시 입력해주세요.")
                    
                    first = 0
                    later = 1

                    while first < 31:
                        if later % 2 == turn:
                            print()
                            print('참가자의 순서')
                            while True:
                                num = int(input('1~3 중 말할 숫자의 개수를 입력하세요: '))
                                if num in [1, 2, 3]:
                                    break
                                else:
                                    print("잘못된 입력입니다. 다시 입력해주세요.")
                           
                            for i in range(num):
                                first  += 1
                                print("참가자: '{0}'!!!".format(first))
                        else:
                            print('컴퓨터의 순서')
                            num = random.randint(1, 3)
                            for i in range(num):
                                first  += 1
                                print("컴퓨터: '{0}'!!!".format(first))
                   
                    if later % 2 == turn:
                        print('🎉축하합니다!😊 3개의 Round 모두 승리했습니다!!🎉')
                        break
                    else:
                        print('아쉽네요! Round 3에서 패배했습니다!!😢')
                        break
            
    else:
        print('틀렸습니다. Round 1에서 패배했습니다!!😢')
            

                    
