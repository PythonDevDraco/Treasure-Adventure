print('''
*********************************************************************************

                               _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   )
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~  
              ~        ~~       ~~~       ~

*********************************************************************************
''')

print("Welcome to Treasure Adventure !")
print("There is a treasure somewhere on this island and you have to find it !")

choice1 = input('''But you come across a bunch of monsters. What will you do ? 
A) Fight them 
B) Sneak past them
Type A to choose option A or type B to choose option B.

''').lower()

if choice1 == "a":
    print("The monsters were more powerful than you. You Died, Game Over.")

elif choice1 == "b":

    choice2 = input('''You sneaked pass the monsters successfully ! Now you have to cross a river 
A) Ignore the river and find a dfferent path
B) Swim across
Type A to choose option A or type B to choose option B.

''').lower()

    if choice2 == "a":

        choice3 = input('''You found a road which lead to a cave. You entered the cave and you found three boxes. Which one will you open ?
A) The white box
B) The box with mythological creatures made on it
C) The box made out of gold
Type A to choose option A or type B to choose option B or type C to choose option C.

''').lower()

        if choice3 == "a":

            print(R'''You found the treasure ! You Won, Game Over.
                    _.--.
                _.-'_:-'||
            _.-'_.-::::'||
       _.-:'_.-::::::'  ||
     .'`-.-:::::::'     ||
    /.'`;|:::::::'      ||_
   ||   ||::::::'     _.;._'-._
   ||   ||:::::'  _.-!oo @.!-._'-.
   |'.  ||:::::.-!()oo @!()@.-'_.|
    '.'-;|:.-'.&$@.& ()$%-'o.'\U||
      `>'-.!@%()@'@_%-'_.-o _.|'||
       ||-._'-.@.-'_.-' _.-o  |'||
       ||=[ '-._.-\U/.-'    o |'||
       || '-.]=|| |'|      o  |'||
       ||      || |'|        _| ';
       ||      || |'|    _.-'_.-'
       |'-._   || |'|_.-'_.-'
        '-._'-.|| |' `_.-'
            '-.||_/.-'
        ''')

        elif choice3 == "b":
            print("It was a trap ! The box had venomous creatures inside it. You Died, Game Over.")
        elif choice3 == "c":
            print("It was a trap ! The box had poison inside it which killed you. You Died, Game Over.")
            
    elif choice2 == "b":
        print("The river was poisonous. You Died, Game Over.")