from playsound import playsound
import eel
@eel.expose
# playing assistant sound function
def playAssistantSound():
    music_dir="www\\assests\\audio\\start_sound.mp3"
    playsound(music_dir)
