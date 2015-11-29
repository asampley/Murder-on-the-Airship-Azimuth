label t_knight:
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_KNIGHT]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_knight_loop:
    python:
        # define line and give options
        # in this case, the line is whatever the character last said.
        line = Game.prevNarrate
        choices = ["Tell me about yourself.", "What is your connection to the victim?", "Describe what you saw this evening", "Ask about a discovery", "Ask about another suspect", "Leave"]
        
        # say line and give options
        #character.speakADV(line)
        character.inputADV(line, choices)
        Game.checkQuit()
        
        try:
            index = int(Game.input) - 1
            if index == 0:
                Game.jump(character.label + "_you")
            elif index == 1:
                Game.jump(character.label + "_vic")
            elif index == 2:
                Game.jump(character.label + "_saw")
            elif index == 3:
                Game.jump(character.label + "_found")
            elif index == 4:
                Game.jump(character.label + "_other")
            elif index == 5:
                Game.jump("start")
            else:
                raise ValueError("wrong choice")

        except ValueError:
            character.speakADV("I don't know what you mean")
        
        Game.jump(character.label + "_loop")
        
label t_knight_you:
    python:
        character.speakADV("Sergeant-Major Angus P. Ritter, Her Infallible Majesty's Ninth Overland Rifle Brigade, retired. ")
        Game.jump(character.label + "_loop")
label t_knight_vic:
    python:
        
        Game.jump(character.label + "_loop")
        
label t_knight_saw:
    python:
        character.speakADV("I left the dining table at eight o'clock precisely. I recovered a book from my luggage in the hold, then returned to my cabin, where I remained until 9:30.")
        character.speakADV("At that time, I visited the observation deck near the cockpit, where I encountered Lady Royaume. We observed the night sky in silence until Airman Newport discovered the body.")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(Game.preNarrate,choices)
        index = int(Game.input)-1
        if index == 0:
            Game.YOU.narrateADV("That was very succinct, thank you.")
            character.speakADV("{i}Ritter nods sharply{\i}")
        elif index == 1:
            pass
        
        Game.jump(character.label + "_loop")

label t_knight_found:
    python:
        Game.jump(character.label + "_loop")
label t_knight_other:
    python:
        Game.jump(character.label + "_loop")
label t_knight_bishop:
    python:
        Game.jump(character.label + "_loop")
label t_knight_knight:
    python:
        Game.jump(character.label + "_loop")
label t_knight_pawn:
    python:
        Game.jump(character.label + "_loop")
label t_knight_queen:
    python:
        Game.jump(character.label + "_loop")
