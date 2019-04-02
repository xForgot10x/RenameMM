# RenameMM
A little script for renaming music files in accordance with the following mask: "[disc number].[track number] - [track title].ext", based on ID tags included in the files. I always found it too bothersome to rename files, whilst tags are usually fine out of the box or require very little tweaks (and it is more pleasant anyway if you use an audio player like foobar2000).

Usage:

  * Make sure your ID3 tags are correct!
  * Run the script (you need Python 3.7+ and TinyTag 1.0.0+)
  * Point it to a folder with music files you want renamed
  * Enjoy!

Warning - the script is designed to work with "clean" data. If you run it on real files, the implication is that the necessary tags are not empty and contain only what they are supposed to. "Track title" and "track number" are mandatory, "disc number" and "total discs" are optional, but are also looked at in case the album is a multi-CD one.

Supports the following formats:

  * mp3
  * flac
  * wave
  * ogg
  * opus
  * wma
  * mp4/m4a

Uses TinyTag library to access metadata. Written using TinyTag 1.0.0. You can grab it here:

  * https://pypi.org/project/tinytag/
  * https://github.com/devsnd/tinytag/

Only tested in Windows 10. Theoretically should work with other OS too.
