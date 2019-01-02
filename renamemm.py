import os
from tinytag import TinyTag

path = input("Enter the desired folder path: ")
try :
    os.chdir(path)
except :
    print("Invalid path")
    quit()

Extensions =  frozenset([".mp3", ".flac", ".m4a", ".mp4", ".m4b", ".wav", ".wma", ".ogg", ".oga", ".opus"])
ReservedChars = frozenset(["<", ">", ":", "/", "\\", "|", "?", "*", "\""])

def WinSafeName(trackname) :
    """Edit the track name so as the resulting file name
    would be allowed in Windows"""
    trackname = trackname.strip()
    if trackname.endswith(".") :
        trackname = trackname[:len(trackname) - 1] + "_"
    for chr in trackname :
        if chr in ReservedChars :
            trackname = trackname.replace(chr, "_")
    return trackname

for filename in os.listdir() :
    if os.path.isfile(filename) :
        file, ext = os.path.splitext(filename)
        if ext in Extensions :
            tag=TinyTag.get(filename)
            tag.track = str(int(tag.track)) #getting rid of leading zeroes in track numbers
            if tag.disc is not None :
                tag.disc = str(int(tag.disc)) #same for discs
            tag.title = WinSafeName(tag.title)
            if tag.disc_total is None or int(tag.disc_total) == 1 :
                if int(tag.track) < 10 :
                    os.rename(filename, "0{} - {}{}".format(tag.track, tag.title, ext))
                else :
                    os.rename(filename, "{} - {}{}".format(tag.track, tag.title, ext))
            else :
                if int(tag.track) < 10 :
                    os.rename(filename, "{}.0{} - {}{}".format(tag.disc, tag.track, tag.title, ext))
                else :
                    os.rename(filename, "{}.{} - {}{}".format(tag.disc, tag.track, tag.title, ext))

print("Done")
                    
#Only tested in Windows. Theoretically should work on other platforms too
#TinyTag library is required to run this script
#Written using tinytag 1.0.0
#https://pypi.org/project/tinytag/