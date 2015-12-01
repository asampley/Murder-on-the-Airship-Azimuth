init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CABIN]
    
label i_cabin:
    scene bg cabinImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CABIN]
        
        # Opening description of the room
        Game.narrateADV("Each room is designed in the same manner as of that of the king's. The mattress as you can see is covered with luxurious silk sheets. . .")
        Game.narrateADV("The ceilings are carefully crafted with shining gold accents and thick plush carpets that caress your feet as you walk.")
        Game.jump(room.label + "_in")
        
label i_cabin_in:        
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
