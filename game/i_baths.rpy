init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BATHS]
    Game.cluesFound[Game.BATHS_WOUND] = False
    Game.cluesFound[Game.BATHS_TIME_OF_DEATH] = False
    Game.state["baths_body_turned"] = False
    
    def look():
        Game.narrateADV( "The {b}body{/b} of Henry Augustus Algernon Royaume is in a pool of blood from the {b}wound{/b} on his head." )
        if Game.state["baths_body_turned"]:
            Game.narrateADV("He is still in his evening wear, now flipped onto his back, his dead eyes staring eerily")
        else:
            Game.narrateADV("He is still in his evening wear, lying face down.")
    def turn():
        Game.state["baths_body_turned"] = True
        Game.narrateADV( "You flip over the {b}body{/b}. It looks like there is something in his {b}pocket{/b}." )
    body = Clue( "body", [ "look", "turn" ], [ look, turn ] )
    
    def look():
        Game.cluesFound[Game.BATHS_WOUND] = True
        Game.narrateADV( "The {b}wound{/b} appears to be caused by a heavy metal object." )
    wound = Clue( "wound" , [ "look" ], [ look ])
    
    def look():
        if Game.state["baths_body_turned"]:
            Game.narrateADV( "There is something small and round in his {b}pocket{/b}, and possibly some glass shards" )
    def open():
        if Game.state["baths_body_turned"]:
            Game.cluesFound[Game.BATHS_TIME_OF_DEATH] = True
            Game.narrateADV( "Inside his pocket is a silver pocket watch. It must have broken when he fell. The face reads 8:42" )
    pocket = Clue( "pocket", [ "look", "open" ], [ look, open ] )
    
    room.addClue(body)
    room.addClue(wound)
    room.addClue(pocket)
    
    def look():
        Game.narrateADV( "The {b}body{/b} of Henry Augustus Algernon Royaume is in a pool of blood from the {b}wound{/b} on his head." )
        if Game.state["baths_body_turned"]:
            Game.narrateADV("He is still in his evening wear, now flipped onto his back, his dead eyes staring eerily")
        else:
            Game.narrateADV("He is still in his evening wear, lying face down.")
    room.addCommand( "look", look )
    
    # clean namespace
    del look
    del body

label i_baths:
    scene bg bathImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_BATHS]
        
        # Opening description of the room
        Game.narrateADV("One of the most expensive places on the [Game.zeppelinName] is this big bath. This was created especially on queen's demand. . . ")
        Game.narrateADV("The ceilings are brilliantly modelled with light bulbs and design patterns with four pillars giving a very royal look to the pool while providing support to the ceiling. . .")
        Game.narrateADV("It is contained with a lot good smelling candle lights, towels and and multiple doors on the sides to give a palace look.")
        Game.jump(room.label + "_in")
        
label i_baths_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
