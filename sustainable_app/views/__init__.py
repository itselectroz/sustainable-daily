# Add view exports to this file
# add all names to __all__ array

from .login import login
from .register import register, privacy_policy
from .logout import logout
from .password_reset import password_reset, forgot_password

from .home import home, complete_personal, update_water, update_daily_goal_status
from .leaderboard import leaderboard
from .profile import profile, equip, purchase

from .goals import quiz, survey, minigame_catching, minigame_sorting
from .location import qr_callback, view_location

from .game_keeper import game_keeper, game_keeper_locations, game_keeper_surveys, game_keeper_questions, remove_keeper, locations_remove, questions_remove, surveys_remove, open_file


__all__ = [
    'login', 'register', 'privacy_policy', 'logout', 'password_reset', 'forgot_password',
    'home', 'complete_personal', 'update_water', 'update_daily_goal_status',
    'leaderboard', 'profile', 'equip', 'purchase',
    'quiz', 'survey', 'qr_callback', 'view_location',
    'game_keeper', 'game_keeper_locations', 'game_keeper_surveys', 'game_keeper_questions',
    'remove_keeper', 'locations_remove', 'questions_remove', 'surveys_remove', 'open_file',
    'minigame_catching', 'minigame_sorting'
]
