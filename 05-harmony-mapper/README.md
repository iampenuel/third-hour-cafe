# 🪑 Guest Harmony Mapper™  
*“Categorizing the vibes before someone gets seated next to chaos.”*

---

## 🌿 THE UNIVERSAL STORY CONTEXT  

**Welcome to The Third Hour Café Chronicles**

It’s a spiritually aesthetic Python coding series rooted in Christian themes, soft startup energy, and narrative design. The story follows **P** (our rookie dev), **Sarah**, **Micah**, **Jordan**, and a rotating cast of chaotic-faithful co-founders as they build quirky terminal-based tools inside a sunlit café somewhere between *Acts 2* and a *Pinterest board*.  

Each code project is born out of emotional/spiritual needs the team experiences in the storyline—debugging love, taking prayer requests, logging lost items, etc. Every README, code comment, and social post carries that narrative energy.  

Think: **GitHub meets a devotional, LinkedIn meets a worship night, terminal meets testimony.**

---

## 📖 Devotional Prelude  
### _“Seat them wisely.”_

Scene: The Third Hour, 6:48PM.  
The windows are golden, the cupcakes are frosted, and Jordan’s playlist just slipped into ambient trap (by accident—or divine design).  

Then it happens.  

Micah freezes mid-sip, Notion printouts trembling in his hand. The door opens.  
She walks in. **The Ex.**  
The one who argued theology until the love cracked.  
The one who left faith, left him, and is suddenly… here again, smiling, in a *Psalm 46:5* crewneck.  

“Hey Micah,” she says, like no time has passed.  
Then she looks over at you.  
> “You’re the one building the prayer tools, right?”  

The air shifts.  
This café isn’t just about coffee anymore.  
It’s a sanctuary where vibes collide, where seating plans are spiritual strategy.  
Because Zeke’s tense, Amirah’s glowing with birthday joy, Hoodie Guy is steady as ever—and now Micah’s ex is in the mix.  

And so: **Guest Harmony Mapper™** is born.  

Not just a list. Not just a log.  
A way of discerning where to seat each soul,  
so the table becomes more than furniture—  
it becomes formation.  

---

## 🛠️ What It Does  

**Guest Harmony Mapper™** is a terminal-based tool that:  

- Prompts for the number of guests to evaluate  
- Collects each guest’s **name** and **vibe**  
- Stores responses as dictionaries inside a list  
- Prints a categorized list of guest vibes  
- Provides output that Jordan (resident vibe curator) can use for seating  

---

## 🧠 How It Works  

- Wrapped in a function: `get_mapper()`  
- Uses a `while True` loop to validate guest count  
- Guard clauses handle non-numeric, empty, or early exits  
- Each guest recorded as a dictionary:  

  ```python
  total_summary = {
      "Name": name.title(),
      "Vibe": vibe
  }

- Appends each dictionary to **`guest_evaluations`** (a list)  
- Prints categorized guest vibes in a clean list  
- Ends with a note to Jordan to *“seat them according to their vibe”*  

---

## 📚 What It Teaches (Code + Soul)  

### 🧑‍💻 *Python Concepts*  
- Input validation with `try/except`  
- Guard clauses for exit and empty strings  
- Lists of dictionaries (multi-structured data)  
- While loops for controlled iteration  
- For loops for output formatting  
- String handling (`.strip()`, `.title()`)  

### 🙏 *Spiritual Concepts*  
- Discernment in community  
- Recognizing the unique vibe each person carries  
- Making space at the table with intention  
- Turning a seating chart into a practice of hospitality  

---

This is **hospitality as algorithm.**  
Every dictionary entry is a soul.  
Every seat is a chance for harmony.  

## 🖥️ Sample Run  

```bash
$ python guest_mapper.py  
How many guests are we evaluating today? 
> 4  

Guest 1 name: Zeke  
What's your vibe? (e.g. chill, chaotic good, tense, weird): tense  
-----  

Guest 2 name: Amirah (birthday girl)  
Vibe? > joyous  
-----  

Guest 3 name: Micah’s Ex  
Vibe? > soft-spoken but potentially disruptive  
-----  

Guest 4 name: Hoodie Guy (Eli)  
Vibe? > grounded  
-----  

Categorized Guest Vibes:  
- Zeke: tense  
- Amirah (Birthday Girl): joyous  
- Micah’s Ex: soft-spoken but potentially disruptive  
- Hoodie Guy (Eli): grounded  

Send info to Jordan and she will suggest a seat for the peeps.  
