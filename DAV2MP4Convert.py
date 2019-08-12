"""
Most of the CCTV Camera output format as DAV files. Using ffmpeg we can convert Convert DAV format to Mp4 format. The ffmpeg already processing as "Multiprocessing"

Authour : Bala Murugan N G

"""
import os
import subprocess
from configparser import ConfigParser
import time

totalstart = time.time()

Config_file = ConfigParser()

Config_file.read("DavtoMp4-config.conf")

DAV_INPUT = Config_file.get("DAVtoMP4","dav_inputpath")
MP4_OUTPUT = Config_file.get("DAVtoMP4","mp4_outputpath")
FFMPEG = Config_file.get("DAVtoMP4","FFMPEG_dir")



def convertDav2Mp4( davPath, mp4Path):
  start = time.time()

  command = [FFMPEG, '-y', '-i', davPath, mp4Path]
  pipe= subprocess.Popen( command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  pipe.communicate()

  end = time.time()

  print(f"Time taken in Minutes : {(end-start)/60}")


if __name__ == "__main__":
    print("------Listing the DAV Files------")
    # List the directories of DAV input path
    listdavfiles = os.listdir(DAV_INPUT)
    # list the directors if .dav extension is present and store in DAVfilesonly list
    DAVfilesonly = [davfiles for davfiles in listdavfiles if davfiles.endswith('.dav')]

    print("------Converting DAV files to MP4 files------")

    for i,DAVinput in enumerate(DAVfilesonly):

        # File name used as same as DAV but the extension is different
        MP4file = os.path.splitext(DAVinput)[0] + '.mp4'


        # Input file and output file path
        DAV_Videoinput = os.path.join(DAV_INPUT,DAVinput)
        MP4_Videooutput = os.path.join(MP4_OUTPUT,MP4file)
        print(f"Processing : {i+1} file")

        # Function to convert DAV to mp4
        convertDav2Mp4(DAV_Videoinput, MP4_Videooutput)

    totalend = time.time()
    print("------Converted into MP4 files------")
    print(f"Total time taken in Minutes : {(totalend - totalstart)/60}")



