import moviepy as mpe
import os

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
    if os.path.exists(vidname):
        os.remove(vidname)
        os.remove(audname)

def main():
    pass

