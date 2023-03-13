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
from .quiz import quiz
from .password_reset import password_reset,forgot_password
from .game_keeper import game_keeper, game_keeper_locations, game_keeper_surveys, game_keeper_events, remove_keeper, locations_add, locations_remove, qr_callback, open_file


__all__ = ['index', 'login', 'logout', 'profile', 'register', 'leaderboard', 'home', 
           'minigame_catching', 'sorting', 'equip', 'game_keeper', 'quiz',
           'game_keeper_locations', 'game_keeper_surveys', 'game_keeper_events', 'remove_keeper'
           'locations_add', 'locations_remove', 'qr_callback', 'password_reset', 'forgot_password', 'open_file']
