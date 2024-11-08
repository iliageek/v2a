from moviepy.editor import *

def v2a():
    
    # Hint
    print("\nFirst Put Your Video Near Your File.")

    # Get Video Name
    video_name = input("\nEnter Your Video's Name (Without Format):\n")
    video_format = input("\nEnter Your Video's Format:\n").lower()
    complete_video = (video_name + "." + video_format)

    # Get Audio Name
    audio_name = input("\nWhat Do You Want The Name of Your Output File To Be:\n")
    audio_format = "mp3"
    complete_audio = (audio_name + "." + audio_format)

    # Get Video & Audio
    video = VideoFileClip(complete_video)
    audio = video.audio

    print("\nPlease Wait...\n")
    
    # Writing Audio In Audio File
    audio.write_audiofile(complete_audio)

    # Done
    video.close()
    audio.close()
    
    print("\nDone!\n")
    
    use_again = input("\nDo You Want To Use V2A Again [Y/N]:\n").capitalize().strip()

    if use_again == "Y":
        print("\nStart V2A...\n")
        v2a()
        
    elif use_again == "N":
        print("\nOK...\nGoodbye!\n")
        exit()
        
    else:
        exit()
    
v2a()
