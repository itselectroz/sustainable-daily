# Add view exports to this file
# add all names to __all__ array

from .index import index
from .home import home, complete_personal, update_daily_goal_status
from .login import login
from .logout import logout
from .profile import profile, equip
from .register import register, privacy_policy
from .leaderboard import leaderboard
from .sorting import sorting
from .minigame_catching import minigame_catching
from .password_reset import password_reset, forgot_password
from .game_keeper import game_keeper, game_keeper_locations, game_keeper_surveys, game_keeper_events, remove_keeper, locations_add, locations_remove, qr_callback, open_file
from .quiz import quiz
from .minigame_survey import minigame_survey
from .view_location import view_location


__all__ = ['index', 'login', 'logout', 'profile', 'register', 'leaderboard', 'home',
           'minigame_catching', 'sorting', 'equip', 'game_keeper',
           'game_keeper_locations', 'game_keeper_surveys', 'game_keeper_events', 'remove_keeper',
           'locations_add', 'locations_remove', 'qr_callback', 'password_reset', 'forgot_password',
           'open_file', 'complete_personal', 'quiz', 'minigame_survey', 'privacy_policy', 
           'update_daily_goal_status', 'view_location']
