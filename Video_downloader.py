from pytube import YouTube

videotype = ['video','видео','відео']
allvideotype = [video.title() for video in videotype]
audiotype = ['audio','аудио','аудіо']
allaudiotype = [audio.title() for audio in audiotype]

def main():
    url = str(input("Url for video: "))
    folder = str(input("Folder full path: "))
    youtube = YouTube(url)
    questintype = str(input('Format(audio or video): '))
    TypeVideo(questintype = questintype,youtube = youtube,folder=folder)


def TypeVideo(questintype,youtube,folder):
    res_list = []
    itag_list = []
    if questintype in videotype or questintype in allvideotype:

        for stream in youtube.streams.filter(type='video', progressive=True):

            stream = str(stream).split(' ')
            itag_list.append(((''.join([i for i in stream if i.startswith('itag')])).replace('itag="','')).replace('"',''))
            res_list.append(((''.join([i for i in stream if i.startswith('res')])).replace('res="','')).replace('"',''))

        questinres = input('Video resolution '+ str(' '.join(res_list) + " : "))
        Itag_Res_dict = dict(zip(itag_list,res_list))

        for tag,res in Itag_Res_dict.items():
            if questinres == res or questinres == res.replace("p",""):
                stream_download = youtube.streams.get_by_itag(tag)
                stream_download.download(folder)
                print("Video download! Folder: ",folder)

    elif questintype in audiotype or questintype in allaudiotype:

        for stream in youtube.streams.filter(type='audio',file_extension='mp4'):

            stream = str(stream).split(' ')
            itag_list.append(((''.join([i for i in stream if i.startswith('itag')])).replace('itag="','')).replace('"',''))
        stream_download = youtube.streams.get_by_itag(itag_list[-1])
        stream_download.download(folder)
        print("Video download! Folder: ",folder)
    

    else:
        print('Error!')

if __name__ == "__main__":
    main()

