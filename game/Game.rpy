init -999 python: # Game class must be given first priority to load
    # Game is a purely static class, and does not need to be instantiated
    class Game:
        input = "" # Static(ish) variable player text input is put into
        __moves = 0 # Numbers of moves player has made
        notes = [] # List of states player has reached, for determining game progress and notebook entries
        
        # Array of npcs
        NPC_NUM = 6
        npcs = [None] * NPC_NUM
        NPC_KING = 0
        NPC_QUEEN = 1
        NPC_BISHOP = 2
        NPC_KNIGHT = 3
        NPC_ROOK = 4
        NPC_PAWN = 5
        
        # Array of rooms
        # Static(ish) array of Rooms
        ROOM_NUM = 9
        rooms = [None] * ROOM_NUM
        ROOM_CABIN = 0
        ROOM_DINING = 1
        ROOM_GALLEY = 2
        ROOM_BATHS = 3
        ROOM_LOUNGE = 4
        ROOM_BAR = 5
        ROOM_CARGO = 6
        ROOM_COCKPIT = 7
        ROOM_ENGINE = 8
        
        # Narrator for narrating
        __Narrator = Character(None, kind=adv)
        
        # Set the initial state of the game
        @staticmethod
        def initialize():
            # NPC defined in NPC.rpy
            Game.npcs[Game.NPC_KING] = NPC("King", None, "#ffffff", []) # White
            Game.npcs[Game.NPC_QUEEN] = NPC("Queen", "t_queen", "#ff0000", []) # Red
            Game.npcs[Game.NPC_BISHOP] = NPC("Bishop", "t_bishop", "#00ff00", []) # Green
            Game.npcs[Game.NPC_KNIGHT] = NPC("Knight", "t_knight", "#0000ff", []) # Blue
            Game.npcs[Game.NPC_ROOK] = NPC("Rook", "t_rook", "#ffff00", []) # Yellow
            Game.npcs[Game.NPC_PAWN] = NPC("Pawn", "t_pawn", "#00ffff", []) # Cyan
            
              
            # Room defined in Room.rpy
            Game.rooms[Game.ROOM_CABIN] = Room("Passenger Cabins", "i_cabin", 0, 0, [])
            Game.rooms[Game.ROOM_DINING] = Room("Dining Room", "i_dining", 1, 0, [])
            Game.rooms[Game.ROOM_GALLEY] = Room("Galley", "i_galley", 2, 0, [])
            Game.rooms[Game.ROOM_BATHS] = Room("Baths", "i_baths", 0, 1, [])
            Game.rooms[Game.ROOM_LOUNGE] = Room("Passenger Lounge", "i_lounge", 1, 1, [])
            Game.rooms[Game.ROOM_BAR] = Room("Bar", "i_bar", 2, 1, [])
            Game.rooms[Game.ROOM_CARGO] = Room("Cargo Hold", "i_cargo", 0, 2, [])
            Game.rooms[Game.ROOM_COCKPIT] = Room("Cockpit", "i_cockpit", 1, 2, [])
            Game.rooms[Game.ROOM_ENGINE] = Room("Engine Room", "i_engine", 2, 2, [])
        
        # Get player input in ADV mode
        @staticmethod
        def inputADV(prompt):
            Game.input = renpy.input(prompt)
        
        # Get player input in NVL mode
        @staticmethod
        def inputNVL(prompt):
            Game.input = renpy.call_screen("nvl_input", prompt)
        
        # Facade method for jumping to labels in Ren'Py, if anything needs to be done every jump it can be done here
        @staticmethod
        def jump(label):
            renpy.jump(label)
        
        # Automatically check last player input against predetermined quit commands, and jump to label if one matches
        # Default label is the start menu of the game
        @staticmethod
        def checkQuit(label="start"):
            target = Game.input.lower()
            if target == "q": Game.jump(label)
            if target == "quit": Game.jump(label)
            if target == "e": Game.jump(label)
            if target == "exit": Game.jump(label)
            
        # Increment the number of moves, and check if anything needs to happen
        @staticmethod
        def incrementMoves():
            Game.__moves += 1
            # checks would be done here
            
        @staticmethod
        def getMoves():
            return Game.__moves
            
        @staticmethod
        def narrate(line):
            renpy.say(Game.__Narrator, line)