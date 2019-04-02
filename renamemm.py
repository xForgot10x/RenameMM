import os
from tinytag import TinyTag

path = input("Enter the desired folder path: ")
# Change directory or quit if it cannot be done
try:
    os.chdir(path)
except:
    print("Invalid path")
    quit()

def win_safe_name(trackname):
    """Edit the track name so as the resulting file name would be
    allowed in Windows
    """
    # In order: strip the whitespace at both ends, replace a trailing
    # full stop by an underscore.  Replace any forbidden characters by
    # underscores.
    trackname = trackname.strip()
    if trackname.endswith("."):
        trackname = trackname[:-1] + "_"
    for chr in trackname:
        if chr in ("<", ">", ":", "/", "\\", "|", "?", "*", "\""):
            trackname = trackname.replace(chr, "_")
    return trackname

# Iterate through the files in set folder
for filename in os.listdir():
    # Discard unsupported files and folders
    if TinyTag.is_supported(filename):
        file, ext = os.path.splitext(filename)
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
