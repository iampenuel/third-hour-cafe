## PROJECT 7 - Lost & Found Tracker™
# define the funtion lost_found
def lost_found():
    # ask how many items being logged
    item_num = int(input("How many items are you logging today?: "))
    # create empty list
    docs = []
    # create final claim status list
    final_claim_status = []
    # create an initial counter
    i = 0

    # while i < number of items being logged
    while i < item_num:
        # print item number
        print(f"Item #{i+1}")
        # ask for name of item
        name = input("Name ot item: ")
        # ask for date found
        date = input("Date found (MM/DD): ")
        # ask where item was found
        location = input("Where was it found?: ")
        # ask if item has been claimed 
        claim_status = input("Has it been claimed? (yes/no): ").lower()
        # total this in a dictionary and append to empty list
        info = {
            "Name": name,
            "Date": date,
            "Location": location,
            "Claimed": claim_status
        }
        docs.append(info)
        # get counter to loop through again till i=i
        i += 1
        
    # print current unclaimed items header
    print("\n🧾 CURRENT UNCLAIMED ITEMS:")
    for item in docs:
        if item["Claimed"] == "no":
            print(f"- {item['Name']} (found {item['Date']}, {item['Location']})")

    # ask if they would like to claim items
    claim_request = input("\nWould you like to claim an item? (yes/no): ").lower()
    if claim_request == "yes":
        # ask what item they would like to claim
        specific_claim_request = input("Which item would you like to claim?: ").lower()
        found_item = False
        for item in docs:
            if item["Name"].lower() == specific_claim_request and item["Claimed"] == "no":
                item["Claimed"] = "yes"
                print(f"\n✅ Item '{item['Name']}' marked as claimed!")
                found_item = True
                break
        if not found_item:
            print("Item is not here or has already been claimed.")

    # print final lost and found report header
    print("\n📦 FINAL LOST & FOUND REPORT:")
    for item in docs:
        status = "Claimed" if item["Claimed"] == "yes" else "Unclaimed"
        print(f"- {item['Name']} — {status}")
# call the function
lost_found()