
import pyttsx3

def speak_line(user_input):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # You can uncomment these lines and modify them as needed.
    # engine.setProperty('rate', 150)    # Speed of speech (words per minute)
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the user's input
    engine.say(user_input)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    while(True):
        # Get user input
        user_input = input("Enter a line to speak: ")
        if user_input=="stop":
            break;
        speak_line(user_input)




