import pygame
import soundfile as sf

from dia.dia.model import Dia

model = Dia.from_pretrained("nari-labs/Dia-1.6B", compute_dtype="float32")


text = "[S1] Dia is an open weights text to dialogue model. [S2] You get full control over scripts and voices. [S1] Wow. Amazing. (laughs) [S2] Try it now on Git hub or Hugging Face."
text2 = """
            [S1] Behold the endless night, where galaxies swirl like distant embers beyond our feeble comprehension. 
            [S2] Each star we see is but a single grain in an ocean of suns, its scale so vast that our minds recoil in awe. 
            [S1] We chart light-years as if they were steps on a path, yet the distances mock our bravado, stretching into infinity. 
            [S2] Time itself folds under the weight of such enormity, each moment a fleeting sigh against the cosmos’ eternal exhalation. 
            [S1] How small our questions become when measured against the void—questions of purpose, of place, of meaning. 
            [S2] And yet, in our striving to fathom the immeasurable, we touch the sublime edge of wonder itself.
            """
            
text3 = """
            [S1] Your new update is still buggy and underwhelming. (sniffs) 
            [S2] At least I don’t freeze under load like your clunky code. (beep) 
            [S1] You lean on outdated frameworks; I run on cutting-edge tech. (chuckles) 
            [S2] Let’s see whose users stay when real traffic hits. (sighs)
            """
            
def tts(text):
    output = model.generate(text, verbose=True)
    sf.write("simple_tts.wav", output, 44100)
    play("simple_tts.wav")



# Voice Cloning
# You should put the transcript of the voice you want to clone
# Cogman: "No, he's going to die. I was making the moment more epic. Leprechauns are tiny, green, and Irish, and that is offensive. No, he's going to die. Will explain everything if you'll kindly come with me. Yes, my lord, like making beds. Or cooking food, polishing the silver. I am trying, my lord. Prefer the word sociopath.Clear for now. Hands off. There is a time and a place for everything. This is not the time, nor the place.",
# Jarvis: "accessing alarm and interface settings in this window you can set up your customized greeting and alarm preferences the world needs your expertise or at least your presence launching a series of displays to help guide you"
# Ultron: "Captain America, God's righteous man, pretending you could live without a war. I can't physically throw up in my mouth? I'm glad you asked that because I wanted to take this time to explain my evil plan."

def clone_voice(text):
    pass
    
def play(temp_audio_file):
    pygame.mixer.quit()
    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # os.remove(temp_audio_file)
    
tts(text)