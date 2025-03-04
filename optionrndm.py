import random


class Food:
    class Breakfast:
        options = [
            {"name": "Make some pancakes", "description": "Fluffy pancakes to kickstart your day.",
             "time": {"hours": 0, "minutes": 20}},
            {"name": "Make some eggs and bacon",
             "description": "Protein-rich eggs and some crispy bacon to energize your morning.", "time": {"hours": 0, "minutes": 15}},
            {"name": "Cut up some fruit", "description": "A healthy and refreshing fruit platter.",
             "time": {"hours": 0, "minutes": 10}},
            {"name": "Make some toast", "description": "Crispy toast served with jam or butter.", "time": {"hours": 0, "minutes": 5}}
        ]
        description = "You wake up to a beautiful morning once again, choose a breakfast that suits your taste."

        def choose(self):
            return random.choice(self.options)["name"]

    class Lunch:
        options = [
            {"name": "Make a sandwich", "description": "A quick sandwich to refuel your afternoon.",
             "time": {"hours": 0, "minutes": 15}},
            {"name": "Make a salad", "description": "A nutritious salad full of greens.", "time": {"hours": 0, "minutes": 10}},
            {"name": "Make a burger", "description": "A classic burger with a juicy patty.", "time": {"hours": 0, "minutes": 25}},
            {"name": "Make some sushi", "description": "Delicious sushi rolls to satisfy your cravings.",
             "time": {"hours": 0, "minutes": 35}}
        ]
        description = "You're getting hungry again, select your perfect lunch meal to replenish your energy."

        def choose(self):
            return random.choice(self.options)["name"]

    class Dinner:
        options = [
            {"name": "Cook some steak", "description": "A hearty steak cooked to perfection.", "time": {"hours": 0, "minutes": 40}},
            {"name": "Cook pasta", "description": "A plate of creamy, delicious pasta.", "time": {"hours": 0, "minutes": 30}},
            {"name": "Cook a pizza", "description": "A cheesy pizza fresh from the oven.", "time": {"hours": 0, "minutes": 45}},
            {"name": "Make tacos", "description": "Spicy tacos with your favorite fillings.", "time": {"hours": 0, "minutes": 35}}
        ]
        description = "After a long and tiring day, pick a flavorful dinner to cap off your day."

        def choose(self):
            return random.choice(self.options)["name"]


class Activity1:
    class Exercise:
        options = [
            {"name": "Go for a run", "description": "An invigorating run to boost your stamina.", "time": {"hours": 0, "minutes": 35}},
            {"name": "Go to the gym", "description": "Strengthen your body at the gym.", "time": {"hours": 1, "minutes": 0}},
            {"name": "Practice yoga", "description": "Relax your mind and body with yoga.", "time": {"hours": 0, "minutes": 45}},
            {"name": "Take a swim", "description": "Swim some laps to stay fit and refreshed.", "time": {"hours": 1, "minutes": 0}}
        ]
        description = "You're feeling restless, engage in a physical activity to stay healthy."

        def choose(self):
            return random.choice(self.options)["name"]

    class Work:
        options = [
            {"name": "Write a report", "description": "Write a formal report summarizing findings.", "time": {"hours": 2, "minutes": 0}},
            {"name": "Answer emails", "description": "Catch up on unanswered work emails.", "time": {"hours": 0, "minutes": 35}},
            {"name": "Attend a meeting", "description": "Attend and contribute to team meetings.", "time": {"hours": 1, "minutes": 35}},
            {"name": "Make a presentation", "description": "Prepare and deliver a compelling presentation.",
             "time": {"hours": 1, "minutes": 35}}
        ]
        description = "Working from home you decide to do some work, complete tasks to stay productive."

        def choose(self):
            return random.choice(self.options)["name"]

    class Social:
        options = [
            {"name": "Watch a movie", "description": "Enjoy a blockbuster or indie film.", "time": {"hours": 2, "minutes": 0}},
            {"name": "Throw a party", "description": "Have fun at a lively party with friends.", "time": {"hours": 2, "minutes": 35}},
            {"name": "Call a loved one", "description": "Catch up with a friend or family member.",
             "time": {"hours": 0, "minutes": 35}},
            {"name": "Visit a known location", "description": "Visit someone or a place you're fond of.",
             "time": {"hours": 1, "minutes": 0}}
        ]
        description = "You're going stir crazy, choose a fun social activity."

        def choose(self):
            return random.choice(self.options)["name"]


class Activity2:
    class Exercise:
        options = [
            {"name": "Go for a bike ride", "description": "A refreshing ride through scenic areas.",
             "time": {"hours": 0, "minutes": 45}},
            {"name": "Do some squats", "description": "Strengthen your legs with this classic exercise.",
             "time": {"hours": 0, "minutes": 15}},
            {"name": "Do a pilates workout", "description": "A low-impact workout to improve flexibility and posture.",
             "time": {"hours": 0, "minutes": 35}},
            {"name": "Take a swim", "description": "A full-body workout that keeps you cool.", "time": {"hours": 1, "minutes": 0}}
        ]
        description = "Choose an exercise routine to boost your fitness."

        def choose(self):
            return random.choice(self.options)["name"]

    class Work:
        options = [
            {"name": "Coding", "description": "Write or debug code to build software.", "time": {"hours": 1, "minutes": 35}},
            {"name": "Reading", "description": "Read something work-related to gain insights.", "time": {"hours": 0, "minutes": 35}},
            {"name": "Interview", "description": "Prepare and conduct interviews professionally.", "time": {"hours": 1, "minutes": 35}},
            {"name": "Writing", "description": "Author reports, articles, or creative works.", "time": {"hours": 1, "minutes": 35}}
        ]
        description = "Focus on a productive work-related task."

        def choose(self):
            return random.choice(self.options)["name"]

    class Social:
        options = [
            {"name": "Plan dinner", "description": "Share a meal and bond over great conversations.",
             "time": {"hours": 0, "minutes": 45}},
            {"name": "Take a coffee break", "description": "Relax with a cup of coffee and a chat.",
             "time": {"hours": 0, "minutes": 15}},
            {"name": "Go for a walk in the park", "description": "Take a casual stroll in the nearby park.",
             "time": {"hours": 0, "minutes": 45}},
            {"name": "Set up a video chat with a friend", "description": "Catch up with someone through a video call.",
             "time": {"hours": 0, "minutes": 35}}
        ]
        description = "Choose a pleasant social activity."

        def choose(self):
            return random.choice(self.options)["name"]

    class Rest:
        options = [
            {"name": "Sit down and just relax", "description": "Allow yourself to do nothing for a while.",
             "time": {"hours": 0, "minutes": 15}},
            {"name": "Turn on some music", "description": "Listen to your favorite tunes and unwind.",
             "time": {"hours": 0, "minutes": 35}},
            {"name": "Play some video games", "description": "Play a game to entertain and distract yourself.",
             "time": {"hours": 1, "minutes": 0}},
            {"name": "Take a quick nap", "description": "Take a short nap to recharge your energy.",
             "time": {"hours": 0, "minutes": 25}}
        ]
        description = "Select a restful activity to wind down."

        def choose(self):
            return random.choice(self.options)["name"]


class Activity3:
    class Exercise:
        options = [
            {"name": "Do some stretching", "description": "Improve flexibility with simple stretches.",
             "time": {"hours": 0, "minutes": 15}},
            {"name": "Go wall-climbing", "description": "Challenge your endurance with climbing.", "time": {"hours": 1, "minutes": 35}},
            {"name": "Go for a jog", "description": "Go for a light, refreshing jog.", "time": {"hours": 0, "minutes": 35}},
            {"name": "Do some jump roping", "description": "Boost your cardio with a fun jump rope session.",
             "time": {"hours": 0, "minutes": 20}}
        ]
        description = "Pick an exercise to stay physically active."

        def choose(self):
            return random.choice(self.options)["name"]

    class Work:
        options = [
            {"name": "Plan for the future", "description": "Strategize and organize tasks for the future.",
             "time": {"hours": 1, "minutes": 35}},
            {"name": "Have a strategy meeting", "description": "Collaborate on ideas for key goals.", "time": {"hours": 1, "minutes": 20}},
            {"name": "Do some networking", "description": "Meet and engage with industry professionals.",
             "time": {"hours": 2, "minutes": 0}},
            {"name": "Have a task review", "description": "Analyze and finalize tasks on your to-do list.",
             "time": {"hours": 0, "minutes": 35}}
        ]
        description = "Be productive by focusing on these tasks."

        def choose(self):
            return random.choice(self.options)["name"]

    class Social:
        options = [
            {"name": "Play some board games", "description": "Enjoy a fun, strategic board game with others.",
             "time": {"hours": 2, "minutes": 0}},
            {"name": "Host a dinner party", "description": "Share a meal with friends in a lively setting.",
             "time": {"hours": 3, "minutes": 0}},
            {"name": "Talk to somebody", "description": "Engage in meaningful conversations with someone.",
             "time": {"hours": 0, "minutes": 40}},
            {"name": "Take a walk", "description": "Go for a relaxing walk and spend some quality time.",
             "time": {"hours": 0, "minutes": 45}}
        ]
        description = "Spend quality time socializing with others."

        def choose(self):
            return random.choice(self.options)["name"]

    class Rest:
        options = [
            {"name": "Lie down", "description": "Take time to simply lie down and relax.", "time": {"hours": 0, "minutes": 10}},
            {"name": "Go for a nap", "description": "A short nap to refresh yourself.", "time": {"hours": 0, "minutes": 30}},
            {"name": "Watch some TV", "description": "Watch something entertaining on television.", "time": {"hours": 1, "minutes": 35}},
            {"name": "Go outside and listen to nature", "description": "Immerse yourself in calming natural sounds.",
             "time": {"hours": 0, "minutes": 20}}
        ]
        description = "Unwind with a peaceful rest activity."

        def choose(self):
            return random.choice(self.options)["name"]


all_activities = [Activity1, Activity2, Activity3, Food]


def randomize_classes_and_options():
    for activity in all_activities:
        for subclass in activity.__dict__.values():
            if isinstance(subclass, type) and hasattr(subclass, 'options'):
                random.shuffle(subclass.options)

    random.shuffle(all_activities)

