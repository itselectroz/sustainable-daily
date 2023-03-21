from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.files import File
from ...models import User, Item, Goal, Location, Survey, SurveyQuestion, SurveyChoice, QuizQuestion, Statistics
from django.shortcuts import reverse
import qrcode
import shutil
import datetime
import os
from io import BytesIO

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **options):
        try:
            self.stdout.write("Rolling back all migrations...")
            call_command('migrate', 'sustainable_app', 'zero')
            self.stdout.write(self.style.SUCCESS('Successfully rolled back migrations.'))
            
            self.stdout.write("Remigrating...")
            call_command('migrate', 'sustainable_app')
            self.stdout.write(self.style.SUCCESS('Successfully re-migrated database.'))
            
            self.stdout.write("Deleting existing images...")
            self.delete_images()
            self.stdout.write(self.style.SUCCESS('Successfully deleted existing images.'))
            
            self.stdout.write("Creating dummy users...")
            self.create_users()
            self.stdout.write(self.style.SUCCESS('Successfully created dummy users.'))
            
            self.stdout.write("Creating dummy locations...")
            self.create_locations()
            self.stdout.write(self.style.SUCCESS('Successfully created dummy locations.'))
            
            self.stdout.write("Creating dummy surveys...")
            self.create_surveys()
            self.stdout.write(self.style.SUCCESS('Successfully created dummy surveys.'))
            
            self.stdout.write("Creating dummy quiz questions...")
            self.create_questions()
            self.stdout.write(self.style.SUCCESS('Successfully created dummy quiz questions.'))
            
            self.stdout.write("Setting dummy Statistics...")
            self.set_stats()
            self.stdout.write(self.style.SUCCESS('Successfully set dummy statistics.'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR('Something went wrong:'))
            self.stderr.write(str(e))
        
    def create_users(self):
        """
        creates multiple users with dummy xp, points and items (for demonstration purposes)
        """
        # create user1
        user1 = User.objects.create_user("JohnS2", "john@example.com", "john")
        user1.xp=(user1.xp_for_level(3) + 100)
        user1.points=600
        user1.streak_length=2
        user1.first_name="John"
        user1.last_name="Smith"
        
        # bought items
        user1.owned_items.add(Item.objects.get(name="frog").id)
        user1.owned_items.add(Item.objects.get(name="viking").id)
        user1.owned_items.add(Item.objects.get(name="u_orange").id)
        user1.owned_items.add(Item.objects.get(name="b_grey").id)
        # default items for all users
        user1.owned_items.add(Item.objects.get(name="badger").id)
        user1.owned_items.add(Item.objects.get(name="none").id)
        user1.owned_items.add(Item.objects.get(name="u_black").id)
        user1.owned_items.add(Item.objects.get(name="b_white").id)
        # equipped items
        user1.equipped_items.add(Item.objects.get(name="frog").id)
        user1.equipped_items.add(Item.objects.get(name="viking").id)
        user1.equipped_items.add(Item.objects.get(name="u_orange").id)
        user1.equipped_items.add(Item.objects.get(name="b_grey").id)
        user1.save()
        
        # create user2
        user2 = User.objects.create_user("MattC", "matt@example.com", "matt")
        user2.xp=(user1.xp_for_level(9) + 100)
        user2.points=800
        user2.streak_length=4
        user2.first_name="Matt"
        user2.last_name="Collinson"
        
        # bought items
        user2.owned_items.add(Item.objects.get(name="bird").id)
        user2.owned_items.add(Item.objects.get(name="party").id)
        user2.owned_items.add(Item.objects.get(name="u_purple").id)
        # default items for all users
        user2.owned_items.add(Item.objects.get(name="badger").id)
        user2.owned_items.add(Item.objects.get(name="none").id)
        user2.owned_items.add(Item.objects.get(name="u_black").id)
        user2.owned_items.add(Item.objects.get(name="b_white").id)
        # equipped items
        user2.equipped_items.add(Item.objects.get(name="bird").id)
        user2.equipped_items.add(Item.objects.get(name="party").id)
        user2.equipped_items.add(Item.objects.get(name="u_purple").id)
        user2.equipped_items.add(Item.objects.get(name="b_white").id)
        user2.save()
        
        # create user3
        user3 = User.objects.create_user("LiamB", "liam@example.com", "matt")
        user3.xp=1000
        user3.points=400
        user3.streak_length=5
        user3.first_name="Liam"
        user3.last_name="Berrisford"
        
        # bought items
        user3.owned_items.add(Item.objects.get(name="crown").id)
        user3.owned_items.add(Item.objects.get(name="u_blue").id)
        user3.owned_items.add(Item.objects.get(name="b_pink").id)
        # default items for all users
        user3.owned_items.add(Item.objects.get(name="badger").id)
        user3.owned_items.add(Item.objects.get(name="none").id)
        user3.owned_items.add(Item.objects.get(name="u_black").id)
        user3.owned_items.add(Item.objects.get(name="b_white").id)
        # equipped items
        user3.equipped_items.add(Item.objects.get(name="badger").id)
        user3.equipped_items.add(Item.objects.get(name="crown").id)
        user3.equipped_items.add(Item.objects.get(name="u_blue").id)
        user3.equipped_items.add(Item.objects.get(name="b_pink").id)
        user3.save()
        
        # create user4
        user4 = User.objects.create_user("NickDRoss", "nick@example.com", "nick")
        user4.xp=(user1.xp_for_level(7) + 100)
        user4.points=700
        user4.streak_length=3
        user4.first_name="Nick"
        user4.last_name="Ross"
        
        # bought items
        user4.owned_items.add(Item.objects.get(name="fish").id)
        user4.owned_items.add(Item.objects.get(name="u_green").id)
        user4.owned_items.add(Item.objects.get(name="b_blue").id)
        # default items for all users
        user4.owned_items.add(Item.objects.get(name="badger").id)
        user4.owned_items.add(Item.objects.get(name="none").id)
        user4.owned_items.add(Item.objects.get(name="u_black").id)
        user4.owned_items.add(Item.objects.get(name="b_white").id)
        # equipped items
        user4.equipped_items.add(Item.objects.get(name="fish").id)
        user4.equipped_items.add(Item.objects.get(name="none").id)
        user4.equipped_items.add(Item.objects.get(name="u_green").id)
        user4.equipped_items.add(Item.objects.get(name="b_blue").id)
        user4.save()
        
        # create game_keeper
        game_keeper = User.objects.create_user("GameKeeper", "keeper@example.com", "admin")
        game_keeper.xp=200
        game_keeper.points=700
        game_keeper.first_name="Game"
        game_keeper.last_name="Keeper"
        game_keeper.game_keeper=True

        # default items for all users
        game_keeper.owned_items.add(Item.objects.get(name="badger").id)
        game_keeper.owned_items.add(Item.objects.get(name="none").id)
        game_keeper.owned_items.add(Item.objects.get(name="u_black").id)
        game_keeper.owned_items.add(Item.objects.get(name="b_white").id)
        # equipped items
        game_keeper.equipped_items.add(Item.objects.get(name="badger").id)
        game_keeper.equipped_items.add(Item.objects.get(name="none").id)
        game_keeper.equipped_items.add(Item.objects.get(name="u_black").id)
        game_keeper.equipped_items.add(Item.objects.get(name="b_white").id)
        game_keeper.save()


    def create_locations(self):
        """
        creates multiple dummy locations and goals (for demonstration purposes)
        """
        
        # create goal1
        goal1 = Goal.objects.create(
            name="Harrison",
            description="",
            image="sustainable_app/img/location_recycle.png",
            type=Goal.LOCATION,
            point_reward=100,
            xp_reward=100,
            active=True,
        )
        goal1.url = reverse('view_location', kwargs={'id': goal1.id})
        goal1.save()
        
        # create location1
        location1 = Location.objects.create(
            goal=goal1,
            name="Harrison",
            category=Location.RECYCLE,
            clue="Near a car park",
        )
        
        # generate qr code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(f"http://www.sustainable-daily.live/location_qr/{goal1.id}/")

        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format='PNG')

        # set attributes
        location1.image = "dummy_images/img_1.png"
        location1.qr.save(f"qr_{location1.id}.png", File(buffer))
        
        # create goal2
        goal2 = Goal.objects.create(
            name="Amory",
            description="",
            image="sustainable_app/img/location_water.png",
            type=Goal.LOCATION,
            point_reward=100,
            xp_reward=100,
            active=True,
        )
        goal2.url = reverse('view_location', kwargs={'id': goal2.id})
        goal2.save()
        
        # create location2
        location2 = Location.objects.create(
            goal=goal2,
            name="Amory",
            category=Location.WATER,
            clue="In a cafe",
        )
        
        # generate qr code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(f"http://www.sustainable-daily.live/location_qr/{goal2.id}/")

        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format='PNG')

        # set attributes
        location2.image = "dummy_images/img_2.png"
        location2.qr.save(f"qr_{location2.id}.png", File(buffer))
        
    def delete_images(self):
        """
        delete all existing qr codes and images
        """

        if not os.path.exists('media'):
            os.mkdir('media')

        if os.path.exists('media/location_qr'):
            shutil.rmtree('media/location_qr')
        if os.path.exists('media/location_images'):
            shutil.rmtree('media/location_images')
        
        os.mkdir('media/location_qr')
        os.mkdir('media/location_images')
        
    def create_surveys(self):
        """
        creates multiple dummy surveys and survey questions (for demonstration purposes)
        """
        
        # create goal1
        goal1 = Goal.objects.create(
            name="test survey1",
            description="",
            image="sustainable_app/img/survey_image.png",
            type=Goal.POLL,
            point_reward=100,
            xp_reward=100,
            active=True,
        )
        goal1.url = reverse('survey', kwargs={'id': goal1.id})
        goal1.save()
        
        # survey 1
        survey1 = Survey.objects.create(
            goal=goal1,
            survey_text="Travel"
        )
        
        # question 1
        surveyQ1 = SurveyQuestion.objects.create(
            survey=survey1,
            question_text="How do you get to campus?",
            pub_date=datetime.datetime.now()
        )
        
        # question 1 choices
        SurveyChoice.objects.create(
            question=surveyQ1,
            choice_text="Walk or Cycle",   
        )
        
        SurveyChoice.objects.create(
            question=surveyQ1,
            choice_text="Drive a car",
        )
        
        SurveyChoice.objects.create(
            question=surveyQ1,
            choice_text="Public transport",   
        )
        
        # question 2
        surveyQ2 = SurveyQuestion.objects.create(
            survey=survey1,
            question_text="What is your average step count per day?",
            pub_date=datetime.datetime.now()
        )
        
        # question 2 choices
        SurveyChoice.objects.create(
            question=surveyQ2,
            choice_text="Less than 10000",   
        )
        
        SurveyChoice.objects.create(
            question=surveyQ2,
            choice_text="More than 1000",
        )
        
    
    def create_questions(self):
        """
        creates multiple dummy quiz questions (for demonstration purposes)
        """
        
        # create question1
        question1 = QuizQuestion.objects.create(
            question="How many recycling bins are on campus?",
            a1="90",
            a2="150",
            a3="20",
            a4="380",
            correct_answer=2,
        )
        question1.save()
        
        # create question2
        question2 = QuizQuestion.objects.create(
            question="Who is the director of sustainability for UoE?",
            a1="Tanya Dale",
            a2="Marcos Oliveira",
            a3="David Wakeling",
            a4="Joanna Chamberlain",
            correct_answer=4,
        )
        
        question2.save()
        
        # create question3
        question3 = QuizQuestion.objects.create(
            question="On average what '%' of food waste in Universities is avoidable?",
            a1="75%",
            a2="20%",
            a3="40",
            a4="90",
            correct_answer=1,
        )
        question3.save()

    def set_stats(self):
        try:
            temp = Statistics.objects.get(name="water")
            temp.quantity = 237
            temp.save()
            temp = Statistics.objects.get(name="plastic")
            temp.quantity = 1054
            temp.save()
        except Statistics.DoesNotExist:
            self.stdout.write("ERROR: 'Statistics' NOT FOUND.")