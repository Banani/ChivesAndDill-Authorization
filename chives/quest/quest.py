class Goal:
    pass


class Quest:
    def __init__(self, description: str, goal: Goal):
        self.description = description
        self.goal = goal


class Murder:
    def __init__(self, _type: type):
        self.type = _type


class KillingSpree(Goal):
    def __init__(self, _type: type, amount: int):
        self.type = _type
        self.amount = amount


class CompositeGoal(Goal):
    def __init__(self, goals: list[Goal]):
        self.goals = goals


class PigSlut:
    pass


class PigFucker:
    pass


class Dragon:
    pass


class Visit(Goal):
    def __init__(this, x: int, y: int):
        this.x = x
        this.y = y


quests = [
    Quest('Rush to kill the pig fuckers', KillingSpree(PigFucker, 12)),

    Quest('Find pig slut', CompositeGoal([
        Visit(200, 200),
        Visit(100, 80),
        Murder(PigSlut),
    ])),
    
]

rapunzel_quest = {
    "Find Rapunzel's cat": {
        'accomplish': {
            'goal': 'location',
            'region': 'root',
            'x': 560,
            'y': 481,
            'tolerance': 50,
        }
    },
    "Inform Rapunzel where the cat is": {
        'accomplish': {
            'goal': 'talk',
            'actor': 'actor.rapunzel'
        }
    },
    "Find the cock sucker cat and rip some of the hair": {
        'accomplish': {
            'goal': 'talk',
            'actor': "actor.rapunzel.cat"
        }
    },
    "Show Rapunzel scratches on your hand": {
        'accomplish': {
            'goal': 'talk',
            'actor': "rapunzel"
        },
        'reward': {
            'exp': 12,
            'items': ['item.apple']
        }
    },
}

dragon_quest = {
    "Find out where the dragon is": {
        'accomplish': {
            'goal': 'talk',
            'actor': 'actor.dragonHunter'
        }
    },
    "Find out where the dragon is, from his father": {
        'accomplish': {
            'goal': 'talk',
            'actor': 'actor.dragonHuntersFather'
        }
    },
    "Go kill dragon": {
        'accomplish': {
            'goal': 'talk',
            'actor': 'actor.dragon'
        }
    },
    "Go talk to dragon hunter": {
        'accomplish': {
            'goal': 'talk',
            'actor': 'actor.dragonHunter'
        }
    },
}
