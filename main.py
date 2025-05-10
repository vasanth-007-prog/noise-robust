import speech_recognition as sr


recognizer = sr.Recognizer()

print("Welcome to the Enhanced Speech Recognition Program")
print("Speak clearly into the microphone.")


with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    print("Microphone is ready, you can start speaking...")

    while True:
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing your speech...")

           
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

            save_option = input("Do you want to save the transcript? (yes/no): ").lower()
            if save_option == "yes":
                with open("transcript.txt", "a") as file:
                    file.write(text + "\n")
                    print("Transcript saved successfully.")

            continue_option = input("Do you want to continue? (yes/no): ").lower()
            if continue_option != "yes":
                print("Exiting the program.")
                break

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google API; {e}")
        except KeyboardInterrupt:
            print("Program interrupted. Exiting...")
            break
import speech_recognition as sr

recognizer = sr.Recognizer()

print("Welcome to the Enhanced Speech Recognition Program")
print("Speak clearly into the microphone.")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    print("Microphone is ready, you can start speaking...")

    while True:
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing your speech...")

           
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

   
            save_option = input("Do you want to save the transcript? (yes/no): ").lower()
            if save_option == "yes":
                with open("transcript.txt", "a") as file:
                    file.write(text + "\n")
                    print("Transcript saved successfully.")

          
            continue_option = input("Do you want to continue? (yes/no): ").lower()
            if continue_option != "yes":
                print("Exiting the program.")
                break

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google API; {e}")
        except KeyboardInterrupt:
            print("Program interrupted. Exiting...")
            break
