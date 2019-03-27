import os
from tinytag import TinyTag

path = input("Enter the desired folder path: ")
# Change directory or quit if it cannot be done
try:
    os.chdir(path)
except:
    print("Invalid path")
    quit()

# Supported file extensions
extensions =  frozenset([".mp3", ".flac", ".m4a", ".mp4", ".m4b",
                         ".wav", ".wma", ".ogg", ".oga", ".opus"])
# List of charachers not allowed in file names under Windows
reserved_chars = frozenset(["<", ">", ":", "/", "\\", "|", "?", "*", "\""])

def win_safe_name(trackname):
    """Edit the track name so as the resulting file name
    would be allowed in Windows"""
    # In order: strip the whitespace at both ends, replace a trailing
    # full stop by an underscore. Replace any forbidden characters by
    # underscores.
    trackname = trackname.strip()
    if trackname.endswith("."):
        trackname = trackname[:len(trackname) - 1] + "_"
    for chr in trackname:
        if chr in reserved_chars:
            trackname = trackname.replace(chr, "_")
    return trackname

# Iterate through the files in set folder
for filename in os.listdir():
    if os.path.isfile(filename):
        file, ext = os.path.splitext(filename)
        # Discard files with unsupported extensions
        if ext in extensions:
            tag=TinyTag.get(filename)
            # Get rid of leading zeroes in track numbers
            tag.track = str(int(tag.track))
            # Get rid of leading zeroes in disc numbers
            if tag.disc is not None:
                tag.disc = str(int(tag.disc))
            tag.title = win_safe_name(tag.title)
            # Rename files for single-disc albums
            if tag.disc_total is None or int(tag.disc_total) == 1:
                if int(tag.track) < 10:
                    os.rename(filename, F"0{tag.track} - {tag.title}{ext}")
                else:
                    os.rename(filename, F"{tag.track} - {tag.title}{ext}")
            # Rename files for multiple-disc albums
            else:
                if int(tag.track) < 10:
                    os.rename(filename,
                              F"{tag.disc}.0{tag.track} - {tag.title}{ext}")
                else:
                    os.rename(filename,
                              F"{tag.disc}.{tag.track} - {tag.title}{ext}")

print("Done")
