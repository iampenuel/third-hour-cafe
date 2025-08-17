## PROJECT 3 - Prayer Request Logger

# define the function log_prayers
def log_prayers():
    # print welcome message
    print("Welcome to The Third Hour: Prayer Request Logger™")
    print("We’re honored to receive your request. Type 'done' at any time to stop.")
    
    # create empty dictionary
    # (note: we actually want a LIST to collect many prayer entries; each entry is a DICTIONARY)
    prayer_log = []
    
    # use while loop
    while True:
        # ask for name
        name = input("\nName: ").strip()
        # break loop if user enters "done"
        if name.lower() == "done":
            break
        # gentle guard: name can't be empty
        if not name:
            print("Name can’t be empty. You can type 'done' to finish.")
            continue

        # ask for prayer request
        raw_request = input("Prayer request (or 'IDK' if you don't know): ").strip()
        # allow 'done' at any time, as promised
        if raw_request.lower() == "done":
            break

        # normalize 'idk' without shouting their request
        if raw_request.lower() == "idk" or raw_request == "":
            print("That’s okay. God knows the details.")
            request = "(Unspoken / God knows the details)"
        else:
            request = raw_request  # keep their original casing

        # ask if public or private
        public = input("Do you want this to be public? (yes/no): ").strip().lower()
        # allow 'done' at any time
        if public == "done":
            break

        # if answer isn't clearly yes/no, ask again until it is (beginner-friendly loop)
        while public not in ("yes", "no"):
            print("please answer 'yes' or 'no' ")
            public = input("Do you want this to be public? (yes/no): ").strip().lower()
            if public == "done":
                # respect 'done' here too
                break
        if public == "done":
            break

        # if public: show name + request
        if public == "yes":
            print(f"{name}: {request}")
            print("\n-----")
        # if private: show anonymous (as name) + request
        elif public == "no":
            print(f"Anonymous request: {request}")
            print("\n-----")

        # store answers in a dictionary
        prayer_entry = {
            "Name": name,
            "Request": request,
            "Public": public  # "yes" or "no"
        }
        # add dictionary to list
        prayer_log.append(prayer_entry)

    # print summary
    print("\nHere’s what we’ll be lifting up this week:\n")
    if not prayer_log:
        print("- (No requests recorded this session.)")
    else:
        for content in prayer_log:
            if content["Public"] == "yes":
                print(f'- {content["Name"]}: {content["Request"]}')
            elif content["Public"] == "no":
                print(f'- Anonymous Request: {content["Request"]}')

    # print end message
    print("\nWe’ve received your prayers. Heaven heard you before we even ran this script.")

# call the function
log_prayers()
