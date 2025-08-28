# 📊 Spiritual Inventory Tracker™  
*“Map the emotional weather of the café today—and gently recommend beverages.”*

---

## 🌿 THE UNIVERSAL STORY CONTEXT  

**Welcome to The Third Hour Café Chronicles**

It’s a spiritually aesthetic Python coding series rooted in Christian themes, soft startup energy, and narrative design. The story follows **P** (our rookie dev), **Sarah**, **Micah**, **Jordan**, and a rotating cast of chaotic-faithful co-founders as they build quirky terminal-based tools inside a sunlit café somewhere between *Acts 2* and a *Pinterest board*.  

Each code project is born out of emotional/spiritual needs the team experiences in the storyline—debugging love, taking prayer requests, logging lost items, etc. Every README, code comment, and social post carries that narrative energy.  

Think: **GitHub meets a devotional, LinkedIn meets a worship night, terminal meets testimony.**

---

## 📖 Devotional Prelude  
### _“Taking stock of the soul.”_

Scene: The Third Hour, 6:48PM.  
Golden light on the windows. Cupcakes lined up like sacraments.  
Jazz bleeding into a lo-fi trap beat Jordan queued (maybe by accident, maybe by God).  

And then: **HER.**  
Micah’s ex. The one who left, lost her faith, and somehow circled back.  
She walks in smiling, in a *Psalm 46:5* crewneck, carrying a tote bag that screams ironic Comic Sans theology.  

Micah’s face does a reboot. Sarah whisper-yells. Jordan grips her sketchbook like it’s holy writ. Eli drifts by with a cupcake like an undercover prophet.  

And you?  
You realize something.  

It’s not enough to log requests.  
It’s not enough to hand out blessings.  
What this café needs tonight is an *inventory of the heart.*  
A way to check the room, count the emotions, name them out loud—  
and then serve drinks like sacraments.  

Enter: **Spiritual Inventory Tracker™.**  
A tool for tallying feelings, mapping frequencies, and gently recommending lattes for souls in process.  

---

## 🛠️ What It Does  

**Spiritual Inventory Tracker™** is a terminal tool that:  

- Prompts for how many guests will share an *emotional bag check*  
- For each guest: records their **name** and up to 3 emotions  
- Collects all emotions into a frequency count (like tallying the room’s weather)  
- Suggests drinks based on select emotions (hopeful, defensive, cake-craving, etc.)  
- Ends with a benediction: *“Your heart is full, and so is your cup.”*  

---

## 🧠 How It Works  

- Wrapped in a function: `inventory_tracker()`  
- Uses a loop to gather guest names + emotions  
- Splits emotions on commas, trims whitespace with `.strip()`  
- Adds each emotion to a master list  
- Builds a frequency dictionary to count occurrences  
- Maps select emotions to drink suggestions via another dictionary  
- Prints both the **frequency report** and the **suggested menu**  

---

## 📚 What It Teaches (Code + Soul)  

### 🧑‍💻 *Python Concepts*  
- Collecting user input in loops  
- Lists and string parsing (`.split(",")`)  
- Frequency counting with dictionaries  
- Conditionals for drink suggestions  
- Clean output formatting  

### 🙏 *Spiritual Concepts*  
- Naming emotions as a holy act  
- Recognizing patterns in community life  
- Responding with gentleness (even if someone’s “defensive”)  
- Hospitality as a form of discernment  
- Turning raw data into pastoral care  

This is **data structures as devotion.**  
Every key-value pair is a soul check-in.  
Every count is a reminder: you are not alone in how you feel.  

---

## 🖥️ Sample Run  

```bash
$ python inventory_tracker.py  
Welcome to The Third Hour: Emotional Inventory Tracker™  

How many guests are submitting a heart check today?  
> 3  

Name: Jordan  
What’s in your spiritual bag today? (3 emotions)  
> hopeful, tired, artistic  

Name: Zeke  
What’s in your spiritual bag?  
> defensive, visionary, controlling  

Name: Amirah  
What’s in your spiritual bag?  
> gratitude, wonder, cake-craving  

---  

📊 Emotion Frequency Report:  
- hopeful: 1  
- tired: 1  
- artistic: 1  
- defensive: 1  
- visionary: 1  
- controlling: 1  
- gratitude: 1  
- wonder: 1  
- cake-craving: 1  

☕ Drink Suggestions Based on Emotional Inventory:  
- hopeful → Honey lavender cold brew  
- defensive → Iced chamomile with oat milk  
- cake-craving → Birthday latte with rainbow sprinkles  

Your heart is full, and so is your cup.  
