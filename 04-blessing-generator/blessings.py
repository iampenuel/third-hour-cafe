## PROJECT 4 - Blessing Generator
# import random
import random

# define function get_blessed
def get_blessed():
    # print welcome message
    print("Welcome to The Third Hour: Blessing Generator™")
    # create dictionary
    blessings = {
        "tired": [
            "May God give rest to your soul and renewal to your body.",
            "Even youths grow weary, but your strength is being restored. (Isaiah 40:30-31)"
        ],
        "anxious": [
            "His peace surpasses understanding. Let it guard your heart. (Phil 4:6-7)",
            "You are held—even when your mind runs wild."
        ],
        "lost": [
            "The Shepherd leaves the ninety-nine for you. He knows where you are.",
            "You’re not forgotten. Heaven hasn’t misplaced you."
        ],
        "happy": [
            "The joy of the Lord is your strength!!! Yes!!(Nehemiah 8:10)"
        ],
        "sad": [
            """The Lord is close to the brokenhearted and saves those who are crushed in spirit.""",
            """look up (Psalm 34:18) on Google...I bet you'll find comfort in this. 
            Sendind digital hugs you beautiful human!"""
        ],
        "angry": [
            """Be quick to listen, slow to speak, and slower to anger—because 
            anger rarely leads to what's right. see (James 1:19-20)""",
            """Don’t let anger control you or linger too long—it gives the enemy 
            a foothold. see Ephesians 4:26-27"""
        ]
    }

    # beginner-friendly helpers (aliases + answer sets)
    alias = {
        "sleepy": "tired", "exhausted": "tired", "weary": "tired",
        "worried": "anxious", "nervous": "anxious", "stressed": "anxious",
        "confused": "lost", "stuck": "lost", "adrift": "lost",
        "joy": "happy", "joyful": "happy", "glad": "happy",
        "down": "sad", "blue": "sad", "heartbroken": "sad",
        "mad": "angry", "frustrated": "angry", "irritated": "angry"
    }
    yes_set = {"yes", "y", "yeah", "yep", "sure"}
    no_set = {"no", "n", "nope"}
    exit_set = {"exit", "quit", "q", "done"}
    list_set = {"list", "options", "help"}

    # use while loop
    while True:
        # ask user how they are feeling (use as key)
        feeling = input(
            "\nHow are you feeling today? (type 'list' for options or 'exit' to finish): "
        ).strip().lower()

        # allow quick exit
        if feeling in exit_set:
            break

        # show options for discoverability
        if feeling in list_set:
            print("Try one of:", ", ".join(sorted(blessings.keys())))
            continue

        # normalize via alias map
        base = alias.get(feeling, feeling)

        # call blessing from dictionary using the key
        if base in blessings:
            blessing = random.choice(blessings[base])
            print(f"🕊️ Blessing: {blessing}")
        else:
            print("""God sees you and is with you in this...yes, even in this.
Talk to Him about how you feel. He wants to hear from you!""")

        # ask if they would like another
        more_blessings = input("\nWould you like another? (yes/no): ").strip().lower()
        print("-----")

        # if not yes
        # (reprompt gently on unclear answers; respect 'exit' anywhere)
        while (
            more_blessings not in yes_set
            and more_blessings not in no_set
            and more_blessings not in exit_set
        ):
            more_blessings = input(
                "Please answer 'yes' or 'no' (or 'exit' to finish): "
            ).strip().lower()

        if more_blessings in no_set or more_blessings in exit_set:
            # break
            break

    # print closing message
    print("\nYou’re loved. You’re seen. The café is always open.")

# call the funtion
get_blessed()
