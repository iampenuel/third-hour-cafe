## PROJECT 1 - VibeBot 1.0

# define function vibe_bot
def vibe_bot():   
    # print welcome message
    print("Welcome to The Third Hour: VibeCheckBot 1.0™")
    
    # using while loop
    while True:
        # ask user how they feel
        response = input("How are you feeling today (tired, overwhelmed, in love, or 'exit' to leave)?: ").strip().lower()
        
        # if tired
        if response == "tired":
            # print vibe diagnosis
            print("Vibe Diagnosis: You need lavender, jazz, and a Psalm. Go read Psalm 23 and take a nap.")
            print("------")

        # elif overwhelmed
        elif response == "overwhelmed":
            # print vibe diagnosis
            print("Vibe Diagnosis: One word...REST! (remember to cast your cares on Him - God) Also maybe go outside :)")
            print("------")

        # elif "in love"
        elif response == "in love":
            # print vibe diagnosis
            print("Awww...Now go get accountability. And maybe an iced cortado to help you think straight.")
            print("------")

        # elif exit
        elif response == "exit":
            # print exit blessing
            print("Grace and peace be with you. Logging off...")
            break

        # else
        else:
            # print vibe diagnosis
            print("Default Vibe: God still loves you. Go talk to Him about it.")
            print("------")

# call the function
vibe_bot()