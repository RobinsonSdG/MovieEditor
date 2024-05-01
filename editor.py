from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, vfx, CompositeAudioClip, afx

# Chemins des fichiers vidéo et musique
chemin_intro = "videos/220124.mp4"
chemin_generique = "videos/WithNewLogo_4k.mp4"
chemin_principale = "videos/220124.mp4"

chemin_voix = "musics/220124.wav"
chemin_ronin = "musics/ronin2.mp3"
chemin_musique_principale = "musics/ronin2.mp3"

voix_intro = AudioFileClip(chemin_voix)
voix_principale = AudioFileClip(chemin_voix)
ronin = AudioFileClip(chemin_ronin)
musique_principale = AudioFileClip(chemin_musique_principale)

# Charger les vidéos et les musiques
video_intro = VideoFileClip(chemin_intro).subclip(0,30).fx(vfx.fadeout, 1)
audio_intro = CompositeAudioClip([ronin.subclip(0, int(video_intro.audio.duration)), voix_intro.subclip(0, int(video_intro.audio.duration))])
video_intro = video_intro.set_audio(audio_intro)

video_generique = VideoFileClip(chemin_generique).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

video_principale = VideoFileClip(chemin_principale).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
ronin_loop = afx.audio_loop(musique_principale, duration=video_principale.duration)
audio_principale = CompositeAudioClip([ronin_loop, voix_principale])
video_principale = video_principale.set_audio(audio_principale)
video_principale = video_principale.subclip(31.3,video_principale.duration)
# video_principale = video_principale.subclip(31,32)

# Ajouter la musique à l'introduction et à la partie principale
# video_generique.without_audio()

# # Créer les transitions entre les vidéos
# transition = VideoFileClip("chemin_vers_transition.mp4")

# Joindre les vidéos avec les transitions
video_finale = concatenate_videoclips([video_intro, video_generique, video_principale])
# video_finale = concatenate_videoclips([video_intro])
# Sauvegarder la vidéo finale
video_finale.write_videofile("finale220124.mp4")