import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices and set a female voice if available
voices = engine.getProperty('voices')
female_voice = None
for voice in voices:
    if "female" in voice.name.lower():
        female_voice = voice.id
        break

if female_voice:
    engine.setProperty('voice', female_voice)

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9) # Volume level (0.0 to 1.0)

# The text you want to convert
text = "This is an offline text-to-speech demonstration using pyttsx3. Just give me under a minute and I'll change the way you look at your life. Just listen. Motivation isn't given. It's built through consistent action. It's not something you're born with. It's the reward you get from making consistent progress over time. You don't get inspired without first doing the work. Every single second you waste waiting for motivation to strike, you lose the opportunity to build your dream. You don't need motivation. What you need is discipline. The truth is, motion always beats motivation. Stop waiting to feel ready for a moment that'll never arrive because you've never leveled up while you were drifting on autopilot. So stop waiting to make the right decision. Instead, make the decision, then make it right. That's how you get motivated."

# Convert the text and speak it aloud
engine.say(text)
engine.runAndWait()

# Stop the engine
engine.stop()
