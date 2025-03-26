import zombiedice, random

class MyZombie():

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun == 2:
                break
            else:
                diceRollResults = zombiedice.roll()
                
class RandomBot():
    def __init__(self, name):
        self.name = name
        
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        
        while diceRollResults is not None:
            decide = random.randint(0,1)
            if decide == 1:
                diceRollResults = zombiedice.roll()
            else:
                break
    

class StopTwoB():

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brain = 0

        while diceRollResults is not None:
            brain += diceRollResults['brains']

            if brain < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class StopTwoSG():

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotgun = 0

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class SGMorethanBrain():
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brain = 0
        shotgun = 0

        while diceRollResults is not None:
            brain += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if brain < shotgun:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    RandomBot(name="My Random Zombie"),
    StopTwoB(name="Stop at 2 brain"),
    StopTwoSG(name="Stop at 2 SG"),
    SGMorethanBrain(name="More than brain")
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)