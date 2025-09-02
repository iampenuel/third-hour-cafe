# 📦 Lost & Found Tracker™  
*“Because nothing is ever truly lost in the Kingdom.”*

---

## 🌿 THE UNIVERSAL STORY CONTEXT  

**Welcome to The Third Hour Café Chronicles**  

It’s a spiritually aesthetic Python coding series rooted in Christian themes, soft startup energy, and narrative design. The story follows **P** (our rookie dev), **Sarah**, **Micah**, **Jordan**, and a rotating cast of chaotic-faithful co-founders as they build quirky terminal-based tools inside a sunlit café somewhere between *Acts 2* and a *Pinterest board.*  

Each code project is born out of emotional/spiritual needs the team experiences in the storyline—debugging love, taking prayer requests, logging lost items, etc. Every README, code comment, and social post carries that narrative energy.  

Think: **GitHub meets a devotional, LinkedIn meets a worship night, terminal meets testimony.**

---

## 📖 Devotional Prelude  
### _“Nothing lost, only waiting to be found.”_

It started with a single left glove.  
Then a library book. Then someone’s annotated Bible with three different colors of highlighter and a coffee ring that felt like destiny.  

The Lost & Found box at The Third Hour was filling up with holy clutter. Jordan called it “chaotic stewardship.” Sarah called it “proof of revival.” Micah wanted to track it in Notion (of course).  

But you? You opened a terminal window and whispered to the console:  
> “We need a system.”  

Not because things are *just things*.  
But because every lost object has a story attached.  
Every claim is a reunion.  
Every list of “unclaimed” is a prayer for return.  

And so: **Lost & Found Tracker™** was born.  
A ledger for the overlooked.  
A witness for the misplaced.  
A reminder that *nothing is wasted when it’s logged with care.*  

---

## 🛠️ What It Does  

**Lost & Found Tracker™** is a terminal tool for logging items, checking claim status, and updating the record.  

- Prompts for the number of items being logged  
- Records **name, date, location, claim status** for each  
- Displays a list of **current unclaimed items**  
- Allows users to claim an item by name  
- Prints a **final report** showing all items and their statuses  

---

## 🧠 How It Works  

- Function: `lost_found()`  
- Uses a loop to log `item_num` entries  
- Each item stored as a **dictionary**:  

  ```python
  info = {
      "Name": name,
      "Date": date,
      "Location": location,
      "Claimed": claim_status
  }

- Appends each dictionary to **`docs`** (a list)  
- Prints unclaimed items (where `"Claimed" == "no"`)  
- Allows claims by matching **Name** input against list entries  
- Updates status in place  
- Prints final report showing **Claimed / Unclaimed**  

---

## 📚 What It Teaches (Code + Soul)  

### 🧑‍💻 *Python Concepts*  
- Lists of dictionaries (nested data structures)  
- For loops for searching & displaying data  
- Guard clauses for claim validation  
- String normalization (`.lower()`)  
- Updating dictionary values in place  

### 🙏 *Spiritual Concepts*  
- Stewardship of what’s left behind  
- Treating overlooked details with care  
- Celebrating reunions, even small ones  
- Remembering that “lost” is rarely permanent  

---

This is **logistics as liturgy.**  
Every dictionary entry is a waiting story.  
Every claim is a resurrection.  

## 🖥️ Sample Run
$ python lost_found.py  
How many items are you logging today?: 3  

Item #1  
Name of item: Umbrella  
Date found (MM/DD): 10/02  
Where was it found?: Back booth  
Has it been claimed? (yes/no): no  

Item #2  
Name of item: Bible  
Date found (MM/DD): 10/02  
Where was it found?: Window seat  
Has it been claimed? (yes/no): yes  

Item #3  
Name of item: AirPod  
Date found (MM/DD): 10/03  
Where was it found?: Near espresso machine  
Has it been claimed? (yes/no): no  

🧾 CURRENT UNCLAIMED ITEMS:  
- Umbrella (found 10/02, Back booth)  
- AirPod (found 10/03, Near espresso machine)  

Would you like to claim an item? (yes/no): yes  
Which item would you like to claim?: AirPod  

✅ Item 'AirPod' marked as claimed!  

📦 FINAL LOST & FOUND REPORT:  
- Umbrella — Unclaimed  
- Bible — Claimed  
- AirPod — Claimed  
