Most of the CCTV Camera output format as DAV files. Using ffmpeg we can convert Convert DAV format to Mp4 format. The ffmpeg already a "Multiprocessing" one. 

Authour : Bala Murugan N G

# Steps to run the Script:

1. Install ffmpeg for Windows and Ubuntu

For Windows 
```
http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/
```
For Ubuntu 
``` 
sudo apt-get update

sudo apt install ffmpeg

ffmpeg -v
```
https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg

http://www.petertheobald.com/tech/dav2mp4-convert-security-cam-dav-to-mp4/

2. Create "DAVFiles" and "MP4Files" folder and give the Input dir of DAV files , Output dir of Mp4 files and ffmpeg installed folder path in the DavtoMp4-config file.

3. Run the "DAV2MP4Convert.py" file. This script is written in Python 3.6 Version. If you have bigger file, surely it takes time.
