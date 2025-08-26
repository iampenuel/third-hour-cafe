## PROJECT 5 - Guest Harmony Mapper
# define the function get_mapper
def get_mapper():
    # ask number of guests being evaluated
    while True:
        raw_number = input("How many guests are we evaluating today? (type a number or 'exit'): ").strip()
        if raw_number.lower() == "exit":
            print("Okay—no guests today.")
            return
        # try to turn the input into a number
        try:
            number = int(raw_number)
            if number <= 0:
                print("Please enter a positive whole number like 3.")
                continue
            break
        except ValueError:
            print("That wasn’t a number. Try again, e.g., 3.")

    # create empty list
    guest_evaluations = []
    # create an initial counter
    i = 0

    # while counter is less than number of guests
    while i < number:
        # ask for guest name
        name = input(f"\nGuest {i+1} name (or 'exit' to stop): ").strip()
        if name.lower() == "exit":
            print("Stopping early and saving what we have…")
            break
        if name == "":
            print("Name cannot be empty. Try again.")
            continue  

        # ask for their vibe
        vibe = input("What's your vibe? (e.g. chill, chaotic good, tense, weird):  ").strip()
        if vibe.lower() == "exit":
            print("Stopping early and saving what we have…")
            break
        if vibe == "":
            vibe = "(unspecified)"  

        print("-----")
        # have total summary established
        #total_summary = f"{name}: {vibe}"
        # store answers in a dictionary
        total_summary = {
           "Name": name.title(),  # show nicely; still easy to understand
           "Vibe": vibe
        }
        # append dictionary to the empty list
        guest_evaluations.append(total_summary)
        # get counter to loop through again till i=i
        i += 1

    # print the summary intro
    print("\nCategorized Guest Vibes:")
    # use a for loop to access the list content
    if len(guest_evaluations) == 0:
        print("- (No guests recorded.)")
    else:
        for content in guest_evaluations:
           # print out the list content
           print(f'{content["Name"]}: {content["Vibe"]}')

    # print out a message for Jordan to seat them according to their vibe
    print("\nSend info to Jordan and she will suggest a seat for the peeps")

# call the function
get_mapper()
