# ## PROJECT 8 - The Heart Ledger™
# # define the function heart_ledger
def heart_ledger():
    # print welcome message
    print("Welcome to The Heart Ledger™")
    # ask number of guests checking in
    while True:
        raw_guest_num = input("How many guests are checking in today?: ").strip()
        try:
            guest_num = int(raw_guest_num)
            if guest_num < 0:
                print("Please enter 0 or a positive whole number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number like 3.")
    # create empty list
    guest_sum = []
    # create intial counter
    i = 0
     
    # while i < guest number checking in
    while i < guest_num:
        # print guest number
        print(f"Guest #{i+1}")
        # ask for name
        name = input("Name: ").strip().lower()
        while name == "":
            print("Name can’t be empty.")
            name = input("Name: ").strip().lower()
        # ask for current state
        state = input("Current state (hopeful, anxious, tired, grateful, lonely, peaceful): ").strip().lower()
        # ask for their journal entry
        entry = input("Journal entry (short note describing how you feel): ").strip().upper()
        # ask if public or anonymous
        is_public = input("Do you want this to be public? (yes/no): ").strip().lower()
        while is_public not in ("yes", "no"):
            print("Please answer 'yes' or 'no'.")
            is_public = input("Do you want this to be public? (yes/no): ").strip().lower()
        # if not public, name == 'anonymous'
        if is_public != "yes":
            name = "Anonymous"
        # create dictionary
        info = {
             "Name": name,
             "State": state,
             "Entry": entry
        }
        # append dictionary to list
        guest_sum.append(info)
        # make counter loop limit
        i += 1

    # print emotion frequency report intro
    print("🧾 EMOTION FREQUENCY REPORT:")
    # get the frequecy of the words (emotions) inputed by the user
    emotion_counts = {}
    for entry in guest_sum:
        state = entry["State"]
        if state in emotion_counts:
            emotion_counts[state] += 1
        else:
            emotion_counts[state] = 1
    # show the counts (beginner-friendly)
    if not emotion_counts:
        print("- (No entries recorded.)")
    else:
        for state, count in emotion_counts.items():
            print(f"- {state}: {count}")
    # list each guest and state (fixed f-string quotes)
    for guest in guest_sum:
        print(f"- {guest['Name']}: {guest['State']}")

    # print the request summary header
    print("SUMMARY OF ENTRIES:")
    # print the request summaries
    for contents in guest_sum:
        print(f'- {contents["Name"]}: {contents["State"]}')

    # print concluding note
    print(""" May peace find you today.
 Heaven received every line.
 """)

# call the function
heart_ledger()
