from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, vfx, CompositeAudioClip, afx

# Chemins des fichiers vidéo et musique
chemin_intro = "videos/Intro16_4k.mp4"
chemin_principale = "videos/160124_4k.mp4"

# Charger les vidéos et les musiques
video_intro = VideoFileClip(chemin_intro).fx(vfx.fadeout, 0.75)

video_principale = VideoFileClip(chemin_principale).fx(vfx.fadein, 0.75).fx(vfx.fadeout, 1)
# video_principale = video_principale.subclip(0,5)
video_finale = concatenate_videoclips([video_intro, video_principale])
# video_finale = concatenate_videoclips([video_intro])
# Sauvegarder la vidéo finale
video_finale.write_videofile("test164k.mp4")