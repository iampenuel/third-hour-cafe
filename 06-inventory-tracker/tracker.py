## PROJECT 6 - Spiritual Inventory Tracker™

# define the function spirit_tracker
def spirit_tracker():
    # print welcome message
    print("\nWelcome to The Third Hour: Emotional Inventory Tracker™")
    print("-----")
    # ask number of guests doing this tracker session
    while True:
        raw = input("\nHow many guests are submitting a heart check today?: ")
        try:
            guest_number = int(raw)
            if guest_number <= 0:
                print("Please enter a positive whole number like 3.")
                continue
            break
        except ValueError:
            print("That wasn’t a number. Try 1, 2, or 3.")

    print("-----")
    # create empty list (1)
    guest_summary = []
    # create emotions dictionary
    emotions_dict = {}
    # create an initial counter
    i = 0

    # allowed emotions (simple list to guide input)
    allowed = ["hopeful", "tired", "artistic", "defensive", "visionary"]

    # while i < guest number
    while i < guest_number:
        # ask for name
        name = input(f"\nGuest #{i+1}: ").strip()
        if name == "":
            print("Name can’t be empty. Try again.")
            continue

        # ask for what's in spiritual bag
        guest_emotions_raw = input("""What’s in your spiritual bag today? (3 emotions) out of these
(hopeful, tired, artistic, defensive, visionary): """).lower()

        # split on commas manually with beginner-style loop
        guest_emotions = []
        for emotion in guest_emotions_raw.split(","):
            emotion = emotion.strip()
            if emotion != "":   # skip blanks
                guest_emotions.append(emotion)

        # simple checks for beginners
        if len(guest_emotions) != 3:
            print("Please enter exactly 3 emotions separated by commas (e.g., hopeful, tired, artistic).")
            continue
        # make sure they’re on the allowed list
        invalid = []
        for emotion in guest_emotions:
            if emotion not in allowed:
                invalid.append(emotion)
        if invalid:
            print(f"Not on the list: {', '.join(invalid)}. Please choose only from: {', '.join(allowed)}.")
            continue

        print("-----")
        # create dictionary to store name and spiritual bag content
        guest_and_emotions = {
            "Name": name,
            "Emotion": guest_emotions
        }
        # append dictionary to empty list
        guest_summary.append(guest_and_emotions)
        # get counter to loop through again till i=i
        i += 1

    # print Emotion Frequency Report
    print("\nEmotion Frequency Report (for Sarah and Micah): ")
    # use for loop to access content in list
    for content in guest_summary:
        for emotion in content["Emotion"]:
            # check if content is in dictioanry as well
            # if so
            if emotion in emotions_dict:
                # use a counter to add 1 
                emotions_dict[emotion] += 1
            # if not
            else:
                # equate it to 1 (since it's only in the list)
                emotions_dict[emotion] = 1
    if not emotions_dict:
        print("- (No emotions recorded.)")
    else:
        for emotion, count in emotions_dict.items():
            print(f"- {emotion}: {count}")

    # print guest and emotion summary intro
    print("\nOverall SPiritual Bag Summary:")
    # use for loop to access the first list
    for content in guest_summary:
        # print the content in that list 
        print(f'- {content["Name"]}: {", ".join(content["Emotion"])}')

    # print final message
    print("Your heart is full, and so is your cup.")

# call the function
spirit_tracker()
