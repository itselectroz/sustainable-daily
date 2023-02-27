# Add view exports to this file
# add all names to __all__ array

from .index import index
from .home import home
from .login import login
from .logout import logout
from .profile import profile, equip
from .register import register
from .leaderboard import leaderboard
from .sorting import sorting
from .minigame_catching import minigame_catching


__all__ = ['index', 'login', 'logout', 'profile', 'register', 'leaderboard', 'home', 'minigame_catching', 'sorting', 'equip']
