import os
import subprocess

#short script to convert media files to a format specified. Basically just a bash script, but the bash scripts I tried for this never worked.

def strip_period(period_check):
	#strip periods from inputs, seemed easier than adding periods
	if period_check.startswith("."):
		period_check = period_check[len("."):]
		return period_check

#I dont wanna add ffmpeg to my system variables, so I add the path below. Strip if needed.
ffmpeg = "G:\\ffmpeg\\ffmpeg-20200821-412d63f-win64-static\\bin\\ffmpeg.exe"
f_path = input("Enter path to file to convert: ") #Enter path like G:\Projects\GodotProjects\ShopliftingGodot\Music
target_type = input("Enter filetype to target: ").lower() #Enter filetype of files to target for conversion
f_type = input("Enter filetype to convert audiofiles to: ").lower() #something like wav,mp3,etc. Will strip period

target_type = strip_period(target_type)
f_type = strip_period(f_type)

os.chdir(f_path) #change to provided path

for contents in os.listdir(): #for folder contents
	if contents[-3:] == target_type: #confirm if file should be targeted
		base_name = contents[:-3]
		newstring = '{} -i "{}" "{}{}"'.format(ffmpeg,contents,base_name,f_type) #constructing windows command as a string
		subprocess.run(newstring,shell=True) #running windows command to take in all parameters and complete work
