
print(r'''       
            ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
    ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You enter a pristine jungle where two paths appear, a deserted trail on the left and a wide road with \nmultiple footsteps on the right.")
choice1=input("Do you choose to go ‘left’ or ‘right’?")

if choice1=="left" or choice1=="Left":
    print("The narrow path twisted and turned seven times and finally led to a golden lake.")
    choice2=input("The golden shimmering lake draws you forward,\n do you choose to ‘swim’ or ‘wait’ for the boat to arrive?")

    if choice2=="wait" or choice2=="Wait":
        print("You waited from dawn until dark, and when you were about to give up, \nthe lights of a fishing boat broke through the darkness, \nand you took a ride in a battered fishing boat.")
        print("The boat sways in the wind, and after a night to reach your destination, \nyou step off the boat in the early morning fog and step onto another unknown land.")
        choice3=input("You come to an old castle building, and as you walk inside, you see three rooms.\n The treasure is close at hand, which door do you choose to enter? \nIs it ‘red’? ‘yellow’? Or ‘blue’?")

        if choice3=="yellow" or choice3=="Yellow":
            print("You push open the yellow door to a room that shines with golden light, \nthis room has no lights, \nbut the walls made of gold bricks and all kinds of gold and silver jewelry blind you.")
            print("Congratulations! \nYou've made it all the way to the real golden house, enjoy your loot!")
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
        elif choice3 == "red" or choice3 == "Red":
                print(
                    "You push open the red door to your room and the moment you walk in, \nthe room automatically locks and the fire that comes crashing down engulfs you...Game over!")
                print(r'''

                      (  .      )
                  )           (              )
                        .  '   .   '  .  '  .
               (    , )       (.   )  (   ',    )
                .' ) ( . )    ,  ( ,     )   ( .
             ). , ( .   (  ) ( , ')  .' (  ,    )
            (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

                   ''')
        elif choice3 == "blue" or choice3 == "Blue":
                print(
                    "You push open the blue door to your room, and the moment you enter\n you feel like you're not entering a room, but a freezer.\n Shortly after that you are frozen into a human popsicle.Game over!")
        else:
            print("Typo, put you in the dark room!")
    elif choice2=="swim" or choice2=="Swim":
        print("You've been attacked by a crocodile that's been lurking in the water for a long time, \nand all that's left is a skeleton... Game over!")
        print(r'''
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'

        ''')
    else:
        print("Typo, put you in the dark room!")
elif choice1=="right" or choice1=="Right":
    print("The open road hides traps and you fall into big holes. Leading ahead is the Fire Dragon's treasure trove,\n where the bones and ashes of countless predecessors feed the lush jungle. \nAwaiting the arrival of the next... Game over!")
    print(r'''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
                          )        \_____________  `              \  /
(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \
''')
else:
    print("Typo, put you in the dark room!")