class Options:
    def __init__(self):
        self.answer = [
            {
                "id": 1,
                "description": "You wake up in your house just outside of town. It's a beautiful morning. Do you:",
                "option": [
                    {"option1": "Get up", "next": 2, "time": {"hours": 0, "minutes": 2}},
                    {"option2": "Go back to sleep", "next": 3, "time": {"hours": 2, "minutes": 0}}
                ]
            },
            {
                "id": 2,
                "description": "What do you do first?",
                "option": [
                    {"option1": "Eat breakfast", "next": 4, "time": {"hours": 0, "minutes": 30}},
                    {"option2": "Go outside", "next": 5, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Turn on the TV", "next": 13, "time": {"hours": 1, "minutes": 0}}
                ]
            },
            {
                "id": 3,
                "description": "You decide to sleep a bit longer. You wake up feeling even better!",
                "option": [
                    {"option1": "Start your day", "next": 2, "time": {"hours": 0, "minutes": 2}}
                ]
            },
            {
                "id": 4,
                "description": "You make a delicious breakfast. The day is off to a great start!",
                "option": [
                    {"option1": "Go outside", "next": 5, "time": {"hours": 0, "minutes": 2}},
                    {"option2": "Turn on the TV", "next": 13, "time": {"hours": 1, "minutes": 0}}
                ]
            },
            {
                "id": 5,
                "description": "You step outside and feel the fresh air. It's a beautiful day!",
                "option": [
                    {"option1": "Go for a walk", "next": 6, "available_on": ["Monday"], "time": {"hours": 1, "minutes": 0}},
                ]
            },
            {
                "id": 6,
                "description": "You go for a walk to the woods west of your home, strangely enough you have a feeling you are being watched. \nWhen you arrive back home from your walk you notice an envelope hanging out of your mailbox.",
                "option": [
                    {"option1": "Open the envelope", "next": 7, "time": {"hours": 0, "minutes": 1}},
                    {"option2": "Inspect the envelope", "next": 8, "time": {"hours": 0, "minutes": 2}},
                    {"option3": "Throw it in the trash", "next": 9, "time": {"hours": 0, "minutes": 1}}
                ]
            },
            {
                "id": 7,
                "description": "Inside the envelope, you find a strange letter written in a language you don't understand. It gives you an uneasy feeling",
                "option": [
                    {"option1": "Keep the letter", "next": 12, "time": {"hours": 0, "minutes": 1}},
                    {"option2": "Burn the letter", "next": 10, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Throw it in the trash", "next": 9, "time": {"hours": 0, "minutes": 2}}
                ]
            },
            {
                "id": 8,
                "description": "You inspect the envelope carefully. It has no return address, but the paper feels oddly cold to the touch.",
                "option": [
                    {"option1": "Open the envelope", "next": 7, "time": {"hours": 0, "minutes": 2}},
                    {"option2": "Throw it in the trash", "next": 9, "time": {"hours": 0, "minutes": 1}},
                ]
            },
            {
                "id": 9,
                "description": "You throw the unknown envelope in your trashcan.",
                "option": [
                    {"option1": "Go inside", "next": 13, "time": {"hours": 0, "minutes": 1}},
                    {"option2": "Walk to town", "next": 11, "time": {"hours": 0, "minutes": 30}},
                ]
            },
            {
                "id":10 ,
                "description": "You burn the letter. The flames burn green for a moment before turning to ash. A chill runs down your spine.",
                "option": [
                    {"option1": "Watch TV and relax at home", "next": 13, "time": {"hours": 7, "minutes": 0}},
                    {"option2": "Walk into town", "next": 11, "time": {"hours": 0, "minutes": 35}}
                ]
            },
            {
                "id": 11,
                "description": "You walk down the gravel road east of your house that leads to the town. \nOnce you arrive at the town square you notice someone suspicious wearing a mask leaving hastily. \nYou see the door to the police station open and a large mass gathered in the middle of the square. ",
                "option": [
                    {"option1": "Follow the masked person", "next": 14, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Walk up to see what the people are gathered around", "next": 16, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Go into the police station", "next": 17, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 12,
                "description": "You decide to keep the letter and put it in your pocket, you feel a strange energy coming from it. When you reach for it again there's nothing but dust",
                "option": [
                    {"option1": "Walk into town", "next": 11, "time": {"hours": 0, "minutes": 35}},
                ]
            },
            {
                "id": 13,
                "description": "You sit down and look through all of the channels",
                "option": [
                    {"option1": "Go outside", "next": 5, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 14,
                "description": "You follow the masked person away from the crowded time square,\nleading you to the outskirts of town and the old cave.",
                "option": [
                    {"option1": "Go into the mine", "next": 18, "time": {"hours": 0, "minutes": 12}},
                    {"option2": "Go back to town square", "next": 15, "time": {"hours": 0, "minutes": 15}}
                ]
            },
            {
                "id": 15,
                "description": "You go back to the town square.",
                "option": [
                    {"option1": "Walk up to see what the people are gathered around", "next": 16, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go into the police station", "next": 17, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 16,
                "description": "You walk up to the crowd of people, slowly moving towards the center and see a body laying lifeless on the ground, the people are frantic.",
                "option": [
                    {"option1": "Go into the police station", "next": 17, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 17,
                "description": "You walk into the police station, It's completely empty, there are phones ringing.",
                "option": [
                    {"option1": "Pick up a phone", "next": 19, "time": {"hours": 0, "minutes": 1}},
                    {"option2": "Check a computer", "next": 21, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 18,
                "description": "You walk into the mine, the ground is slippery and there are torches lit on the walls of the cave.",
                "option": [
                    {"option1": "Go further in", "next": 23, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go back to the town square", "next": 15, "time": {"hours": 0, "minutes": 18}}
                ]
            },
            {
                "id": 19,
                "description": "The phone right next to you is ringing, you pick it up hesitantly and say 'Hello', you hear multiple muffled voices and then the caller hangs up. ",
                "option": [
                    {"option1": "Check a computer", "next": 21 , "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Try to call back", "next": 22 , "time": {"hours": 0, "minutes": 2}}
                ]
            },
            {
                "id": 20,
                "description": "Are you ready to begin the next day?",
                "option": [
                    {"option1": "Yes", "next": 30 , "time": {"hours": 0, "minutes": 0}},
                ]
            },
            {
                "id":21,
                "description": "You go to the nearest computer and turn it on hoping to find some answers,\nbut it's password protected.",
                "option": [
                    {"option1": "Look around for clues about the password", "next":24, "time": {"hours": 0, "minutes": 15}},
                    {"option2": "Try to brute force it", "next":26, "time": {"hours": 0, "minutes": 45}},
                    {"option3": "Leave it", "next":25, "time": {"hours": 0, "minutes": 0}}
        ]
        },
            {
                "id": 22,
                "description": "You try to call back the number that just called in, it rings twice before the line gets completely quiet,\n someone has cut the phone line.",
                "option": [
                    {"option1": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}},
                    {"option2": "Check the phone line", "next": 29, "time": {"hours": 0, "minutes": 10}},
                ]
            },
            {
                "id": 23,
                "description": "You go further into the mine until you get to the end, where you find a notebook and some drawings on the wall. ",
                "option": [
                    {"option1": "Read through the notebook", "next": 27, "time": {"hours": 0, "minutes": 7}},
                    {"option2": "Look at the drawings on the walls", "next": 28, "time": {"hours": 0, "minutes": 4}},
                    {"option3": "Go back to town square", "next": 15, "time": {"hours": 0, "minutes": 25}}
                ]
            },
            {
                "id": 24,
                "description": "You look around the room for clues on what the password is, you see a note on the postboard. \nYou pick it up and get into the computer.",
                "option": [
                    {"option1": "Check through search history", "next": 31, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Look through files", "next": 32, "time": {"hours": 0, "minutes": 15}},
                ]
            },
            {
                "id": 25,
                "description": "You decide to leave it alone and spend the rest of your day back home.",
                "option": [
                    {"option1": "Go home", "next": 30, "end_day": True}
                ]
            },
            {
                "id": 26,
                "description": "You sit at the desk trying different random password combinations, it doesn't work.",
                "option": [
                    {"option1": "Look around for clues for the password", "next": 24, "time": {"hours": 0, "minutes": 15}},
                    {"option2": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}},
                ]
            },
            {
                "id": 27,
                "description": "You pick the notebook up and start reading through it, it's filled with nonsensical religious ramblings.",
                "option": [
                    {"option1": "You look at the drawings on the wall", "next":28 , "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go back to town square", "next": 15, "time": {"hours": 0, "minutes": 20}}
                ]
            },
            {
                "id": 28,
                "description": "You take a look at the drawings on the wall, \nthere are religious symbols and the word 'FYRE' written over and over again.",
                "option": [
                    {"option1": "Go back to town square", "next": 15, "time": {"hours": 0, "minutes": 20}},
                ]
            },
            {
                "id": 29,
                "description": "You go around the back to check the phone line, you find a box cutter near the line and a singular footprint",
                "option": [
                    {"option1": "Check the computer", "next": 21, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}},
                ]
            },
            {
                "id": 30,
                "description": "",
                "option": [
                    {"option1": "", "next": 34, "time": {"hours": 0, "minutes": 0}},
                    {"option2": "", "next": 35, "time": {"hours": 0, "minutes": 0}},
                    {"option3": "", "next": 36, "time": {"hours": 0, "minutes": 0}}
                ]
            },
            {
                "id": 31,
                "description": "You open up the browser and start looking through the browser history, it has recently been cleared",
                "option": [
                    {"option1": "Look through the files", "next": 32, "time": {"hours": 0, "minutes": 15}},
                    {"option2": "Look through the emails", "next": 33, "time": {"hours": 0, "minutes": 20}},
                    {"option3": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}}
                ]
            },
            {
                "id": 32,
                "description": "You look through the files on the computer, you find a suspicious program that was downloaded yesterday",
                "option": [
                    {"option1": "Look through the browser history", "next": 31, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Look through the emails", "next": 33, "time": {"hours": 0, "minutes": 20}},
                    {"option3": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}}
                ]
            },
            {
                "id": 33,
                "description": "You decide to look through the emails, the inbox is full of mundane work stuff.\n When you check the trashcan you find emails talking about a mysterious sighting in the cave.",
                "option": [
                    {"option1": "Look through the files", "next": 32, "time": {"hours": 0, "minutes": 15}},
                    {"option2": "Look through the browser history", "next": 31, "time": {"hours": 0, "minutes": 10}},
                    {"option3": "Leave it", "next": 25, "time": {"hours": 0, "minutes": 0}}
                ]
            },

            #day2 events
            {
                "id": 34,
                "description": "You wake up in your house just outside of town. It's a beautiful morning. Do you:",
                "option": [
                    {"option1": "Get up", "next": 35, "time": {"hours": 0, "minutes": 2}},
                    {"option2": "Go back to sleep", "next": 36, "time": {"hours": 2, "minutes": 0}}
                ]
            },
            {
                "id": 35,
                "description": "What do you do first?",
                "option": [
                    {"option1": "Eat breakfast", "next": 37, "time": {"hours": 0, "minutes": 30}},
                    {"option2": "Go outside", "next": 38, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Turn on the TV", "next": 39, "time": {"hours": 1, "minutes": 0}}
                ]
            },
            {
                "id": 36,
                "description": "You decide to sleep a bit longer. You wake up feeling even better!",
                "option": [
                    {"option1": "Start your day", "next": 35, "time": {"hours": 0, "minutes": 2}}
                ]
            },
            {
                "id": 37,
                "description": "You make a delicious breakfast. The day is off to a great start!",
                "option": [
                    {"option1": "Go outside", "next": 38, "time": {"hours": 0, "minutes": 2}},
                    {"option2": "Turn on the TV", "next": 13, "time": {"hours": 1, "minutes": 0}}
                ]
            },
            {
                "id": 38,
                "description": "You step outside and feel the fresh air, you get an uneasy feeling but theres no letter in your mailbox.",
                "option": [
                    {"option1": "Walk to town", "next": 40, "time": {"hours": 0, "minutes": 30}},
                    {"option2": "Go for a walk", "next": 41, "time": {"hours": 1, "minutes": 0}},
                ]
            },
            {
                "id": 39,
                "description": "You sit down and look through all of the channels",
                "option": [
                    {"option1": "Go outside", "next": 38, "time": {"hours": 1, "minutes": 0}}
                ]
            },
            {
                "id": 40,
                "description": "You walk down the gravel road east of your house that leads to the town. \nThe town square is empty and the police station is closed.",
                "option": [
                    {"option1": "Go check where the body was yesterday", "next": 42, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go into the police station", "next": 43, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Walk to the mines", "next": 44, "time": {"hours": 0, "minutes": 10}}
                ]
            },
            {
                "id": 41,
                "description": "You once again go for a walk to the woods west of your home,",
                "option": [
                    {"option1": "Keep going deeper into the forest", "next": 56, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Walk to town", "next": 40, "time": {"hours": 0, "minutes": 45}}
                ]
            },
            {
                "id": 42,
                "description": "The body is gone, all that's left is a dark spot and an enamel pin.\nYou pick up the enamel pin and put it in your pocket, it had the letters B.H on it.",
                "option": [
                    {"option1": "Go into the police station", "next": 43, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Walk to the mines", "next": 44, "time": {"hours": 0, "minutes": 10}}
                ]
            },
            {
                "id": 43,
                "description": "You try walking into the police station, but the door is locked.",
                "option": [
                    {"option1": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Walk to the mines", "next": 44, "time": {"hours": 0, "minutes": 10}},
                    {"option3": "Try to break into the police station", "next": 45, "time": {"hours": 0, "minutes": 10}},
                    {"option4": "Try to find another way into the police station", "next": 47, "time": {"hours": 0, "minutes": 30}}
                ]
            },
            {
                "id": 44,
                "description": "You walk to the mines, it's eerily quiet and pitch black inside, you need something to light up your way.",
                "option": [
                    {"option1": "Go back to town", "next": 40, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 20}},
                    {"option3": "Find a light source", "next": 46, "time": {"hours": 0, "minutes": 35}}
                ]
            },
            {
                "id": 45,
                "description": "You try to break into the police station, but the door is too strong.",
                "option": [
                    {"option1": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Walk to the mines", "next": 44, "time": {"hours": 0, "minutes": 10}},
                    {"option3": "Try to find another way into the police station", "next": 47, "time": {"hours": 0, "minutes": 30}}
                ]
            },
            {
                "id": 46,
                "description": "You find a flashlight in your house and head back to the mines, you can now see the walls are covered in the same symbols you saw yesterday, there's some fresh marks on the walls.",
                "option": [
                    {"option1": "Go further into the mine", "next": 48, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go back to town", "next": 40, "time": {"hours": 0, "minutes": 10}}
                ]
            },
            {
                "id": 47,
                "description": "You find a backdoor to the police station, it's locked but you can see through the window in the door that the lights are on inside.",
                "option": [
                    {"option1": "Find a good rock to try and break the window", "next": 49, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}},
                    {"option3": "Walk to the mines", "next": 44, "time": {"hours": 0, "minutes": 10}}
                ]
            },
            {
                "id": 48,
                "description": "You go further into the mine until you get to the end, the walls are completely empty and there's nothing there.",
                "option": [
                    {"option1": "Go back to town", "next": 40, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 20}}
                ]
            },
            {
                "id": 49,
                "description": "You find a rock and throw it at the window, it shatters and you can now climb in.",
                "option": [
                    {"option1": "Go inside", "next": 50, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 50,
                "description": "You climb through the window and find yourself in the police station, it's completely empty and the lights are flickering.",
                "option": [
                    {"option1": "Check the computers", "next": 51, "time": {"hours": 0, "minutes": 10}},
                    {"option2": "Check the evidence room", "next": 52, "time": {"hours": 0, "minutes": 15}},
                    {"option3": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 51,
                "description": "You go to the nearest computer and try to turn it on, but the screen has an error message on it",
                "option": [
                    {"option1": "Go to the evidence room", "next": 52, "time": {"hours": 0, "minutes": 15}},
                    {"option2": "Leave it", "next": 54, "time": {"hours": 0, "minutes": 0}}
                ]
            },
            {
                "id": 52,
                "description": "You go to the evidence room and find a case file on the body that was found yesterday, it's filled with pictures and notes.",
                "option": [
                    {"option1": "Read through the case file", "next": 53, "time": {"hours": 0, "minutes": 7}},
                    {"option2": "Look at the pictures", "next": 58, "time": {"hours": 0, "minutes": 4}},
                    {"option3": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 53,
                "description": "You skim through the case file, there is mention of a mysterious symbol found in the file",
                "option": [
                    {"option1": "Look at the pictures", "next": 58, "time": {"hours": 0, "minutes": 0}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}}
                ]
            },
            {
                "id": 54,
                "description": "You decide to leave it alone and spend the rest of your day back home.",
                "option": [
                    {"option1": "Go home", "next": 55, "end_day": True}
                ]
            },
            {
                "id": 55,
                "description": "",
                "option": [
                    {"option1": "", "next": 00, "time": {"hours": 0, "minutes": 0}},
                    {"option2": "", "next": 00, "time": {"hours": 0, "minutes": 0}},
                    {"option3": "", "next": 00, "time": {"hours": 0, "minutes": 0}}
                ]
            },
            {
                "id": 56,
                "description": "You keep going deeper into the forest, you find a clearing with a small shrine in the middle.",
                "option": [
                    {"option1": "Inspect the shrine", "next": 58, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 20}}
                ]
            },
            {
                "id": 57,
                "description": "The shrine has a fox on it, there's mysterious text written underneath the fox. You don't understand the language.",
                "option": [
                    {"option1": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 5}},
                    {"option2": "Walk into town", "next": 40, "time": {"hours": 0, "minutes": 35}}
                ]
            },
            {
                "id": 58,
                "description": "You look at the pictures and see the same symbol that was on the envelope you found yesterday.",
                "option": [
                    {"option1": "Go back home", "next": 54, "time": {"hours": 0, "minutes": 40}},
                ]
            }
        ]




