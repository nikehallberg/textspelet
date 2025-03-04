import sys
import random
from optionrndm import all_activities

class Game:
    def __init__(self, player, events):
        self.player = player
        self.day = 1
        self.time = GameTime()
        self.feeling = random.choice(['invigorated', 'refreshed', 'rejuvenated', 'energized', 'restored', 'renewed'])
        self.weather = random.choice(['raining', 'sunny', 'snowing', 'windy', 'cloudy', 'hailing'])
        self.events = events
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def start(self):
        while True:
            answer = input("Are you ready? (Yes or No): ").strip().lower()
            if answer == 'yes':
                print('Let us start your adventure!\n')
                self.run_game()
                break
            elif answer == 'no':
                sys.exit('Come back when you are ready.')
            else:
                print('Invalid answer, please input Yes or No.')

    def ask_question(self, description, options):
        print(description)
        for i, option in enumerate(options, 1):
            time_required = option.get('time', {"hours": 1, "minutes": 0})
            hours = time_required.get('hours', 0)
            minutes = time_required.get('minutes', 0)
            print(f"{i}. {list(option.values())[0]} (Time: {hours} hours, {minutes} minutes)")
        while True:
            choice = input("Choose an option: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                selected_option = options[int(choice) - 1]
                time_spent = selected_option.get('time', {"hours": 1, "minutes": 0})
                self.time.update_time(hours=time_spent.get('hours', 0), minutes=time_spent.get('minutes', 0))

                if selected_option.get("end_day", False):
                    print(f"Option chosen ends the day: {list(option.values())[0]}")
                    self.end_day()
                    return None

                return selected_option["next"]

            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")

    def run_game(self):
        while True:
            self.run_day()

            continue_game = input("Do you want to continue to the next day? (Yes or No): ").strip().lower()
            if continue_game == 'yes':
                self.start_new_day()
            else:
                print("Thanks for playing!")
                break

    def run_day(self):
        day_of_week = self.days[(self.day - 1) % 7]

        print(
            f"Day {self.day}, {day_of_week}, {self.time.get_time()}\n"
            f"You feel {self.feeling} and the weather is {self.weather}.\n"
        )
        print("⋆｡°• 🌧 ⛆༄. ݁₊ ⊹⋆.🌧 ⛆༄ . ݁˖ . ݁⛆༄⋆｡°• ⋆｡°• 🌧 ⛆༄. ݁₊ ⊹⋆.🌧 ⛆༄ . ݁˖ . ݁⛆༄⋆｡°• ")

        if self.day == 1:
            current_event_id = 1

            while current_event_id:
                event = next(e for e in self.events if e["id"] == current_event_id)
                description = event["description"]
                options = event["option"]
                current_event_id = self.ask_question(description, options)

                if current_event_id is None:
                    return

                print(f"Current time: {self.time.get_time()}")

                if self.time.hour >= 20:
                    print("\nThe day is winding down. It's time for bed.\n")
                    self.end_day()
                    return
        elif self.day == 2:
            current_event_id = 34
            while current_event_id:
                event = next(e for e in self.events if e["id"] == current_event_id)
                description = event["description"]
                options = event["option"]
                current_event_id = self.ask_question(description, options)

                if current_event_id is None:
                    return

                print(f"Current time: {self.time.get_time()}")

                if self.time.hour >= 20:
                    print("\nThe day is winding down. It's time for bed.\n")
                    self.end_day()
                    return

        else:
            for activity in all_activities:
                for subclass_name, subclass in activity.__dict__.items():
                    if isinstance(subclass, type) and hasattr(subclass, 'options'):
                        options = list(subclass.options)
                        random.shuffle(options)
                        print(f"{subclass.description}\n")

                        print(f"Current time: {self.time.get_time()}")

                        print("Choose an option:")
                        for i, option in enumerate(options, 1):
                            print(f"{i}. {option['name']} - {option['description']}")

                        while True:
                            try:
                                choice_index = int(input("Enter the number of your choice: ")) - 1
                                if 0 <= choice_index < len(options):
                                    chosen_option = options[choice_index]["name"]
                                    print(f"You chose: {chosen_option}\n")
                                    break
                                else:
                                    print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")

            self.end_day()

    def end_day(self):
        print("The day has ended. Time for bed...\n")
        print("˚　　　　✦　　　.　　. 　˚　.　　　　　 . ✦　　　 　˚　　　　 . ★⋆. . 　　˚　　 　　*　　 　　✦　　　.　　.　　　✦　˚ 　　　　˚　.˚　　　　　　.　　. 　˚　.　　　　 　　 　　　　 ✦")
        self.time.set_time(10)
        self.day += 1
        self.feeling = random.choice(['invigorated', 'refreshed', 'rejuvenated', 'energized', 'restored', 'renewed'])
        self.weather = random.choice(['raining', 'sunny', 'snowing', 'windy', 'cloudy', 'hailing'])

    def start_new_day(self):
        print(f"Starting a new day... Day {self.day}\n")
        self.run_day()


class GameTime:
    def __init__(self):
        self.hour = 10
        self.minute = 0

    def update_time(self, hours=0, minutes=0):
        self.minute += minutes
        self.hour += hours + self.minute // 60
        self.minute %= 60
        self.hour %= 24

    def get_time(self):
        period = "AM" if self.hour < 12 else "PM"
        hour_display = self.hour if self.hour <= 12 else self.hour - 12
        hour_display = hour_display if hour_display != 0 else 12
        return f"{hour_display}:{self.minute:02d} {period}"

    def set_time(self, hour, minute=0):
        self.hour = hour % 24
        self.minute = minute % 60
