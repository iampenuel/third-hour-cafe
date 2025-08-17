# 🕊️ Prayer Request Logger™  
*“Submit & Be Still.” — a terminal liturgy for recording the cries of the heart.*

---

## 🌿 THE UNIVERSAL STORY CONTEXT  

**Welcome to The Third Hour Café Chronicles**

It’s a spiritually aesthetic Python coding series rooted in Christian themes, soft startup energy, and narrative design. The story follows **P** (our rookie dev), **Sarah**, **Micah**, **Jordan**, and a rotating cast of chaotic-faithful co-founders as they build quirky terminal-based tools inside a sunlit café somewhere between *Acts 2* and a *Pinterest board*.

Each code project is born out of emotional/spiritual needs the team experiences in the storyline—debugging love, taking prayer requests, logging lost items, etc. Every README, code comment, and social post carries that narrative energy.

Think: **GitHub meets a devotional, LinkedIn meets a worship night, terminal meets testimony.**

---

## 📖 Devotional Prelude  
### _“Submit & Be Still.”_

Golden hour spills through the café windows like it’s auditioning for a Hillsong music video.  
Your laptop hums quietly on the counter. There’s one crumb left from a croissant that could only be described as *spiritually flaky.*  

Sarah slides into the booth beside you, sunglasses on indoors (as always), whisper-yelling about the smell of “toasted almond and conviction.”  
Jordan sketches a UI concept that looks less like software and more like a psalm in grayscale.  
Micah waves around a Notion printout like Moses holding tablets, muttering about “divine appointment data points.”  

And then—just outside the tall café window—a stranger leaves a folded note in the frame.  
He doesn’t come in.  
He just leaves it, quietly, and walks away.  

Jordan whispers:  
> “P... I think he came for more than coffee.”  

This is the moment.  
No more sticky notes. No more tote bags full of loose prayers.  
The café needs a system that’s soft enough to hold someone’s heart, and structured enough to steward their words.  

And so: **Prayer Request Logger™** is born.  
Not as corporate-church-software.  
Not as another task manager.  

But as a **terminal altar**,  
a list of dictionaries disguised as intercession,  
a space where even an “IDK” counts as holy.  

Because sometimes the holiest code you can write is a function that listens.

---

## 🛠️ What It Does  

**Prayer Request Logger™** is a terminal-based tool that receives prayer requests and stores them in a structured way.  

- Prompts for **name, request, and privacy setting**  
- Allows “done” at any time to stop gracefully  
- Handles “IDK” or blank entries with gentleness (“God knows the details”)  
- Saves each entry as a **dictionary** inside a **list**  
- Prints a final **prayer log**:  
  - If public → shows name + request  
  - If private → shows “Anonymous request”  
- Ends with a pastoral confirmation:  
  _“We’ve received your prayers. Heaven heard you before we even ran this script.”_

---

## 🧠 How It Works  

- Wrapped in a function: `log_prayers()`  
- Uses a `while True` loop for continuous submissions  
- Guard clauses to handle empty names or “done” input  
- Each request stored in a **dictionary**:  

  ```python
  prayer_entry = {
      "Name": name,
      "Request": request,
      "Public": public
  }

- `.append()` adds each entry to **`prayer_log`** (a list)  
- `if/else` decides whether to print the request as public or anonymous  
- Includes print dividers (`"-----"`) for readability  

---

## 📚 What It Teaches (Code + Soul)  

### 🧑‍💻 *Python Concepts*  
- Functions with logic encapsulated inside  
- Lists + dictionaries (data structures in tandem)  
- Input validation & guard clauses  
- While loops for repeated input  
- Nested conditionals (`if/else`)  
- Gentle error handling  

### 🙏 *Spiritual Concepts*  
- Logging as listening  
- Privacy as compassion  
- Making space for the “unspoken” request  
- Turning raw input into intercession  
- Seeing code not just as execution, but as care  

---

This is **DSA as doxology.**  
Every dictionary is a story.  
Every loop is an invitation to speak.  

## 🖥️ Sample Run  

```bash
$ python prayer_logger.py  
Welcome to The Third Hour: Prayer Request Logger™  
We’re honored to receive your request. Type 'done' at any time to stop.  

Name: Jade  
Prayer request (or 'IDK' if you don't know): My anxiety’s been creeping in again lately. Just want peace.  
Do you want this to be public? (yes/no): yes  

Jade: My anxiety’s been creeping in again lately. Just want peace.  

-----  

Name: Michael  
Prayer request (or 'IDK' if you don't know): My grandma's surgery tomorrow.  
Do you want this to be public? (yes/no): no  

Anonymous request: My grandma's surgery tomorrow.  

-----  

Name: done  

Here’s what we’ll be lifting up this week:  

- Jade: My anxiety’s been creeping in again lately. Just want peace.  
- Anonymous Request: My grandma's surgery tomorrow.  

We’ve received your prayers. Heaven heard you before we even ran this script.  
