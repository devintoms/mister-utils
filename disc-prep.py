import os
import re


# gets the appropriate folder name for file
def get_folder_name(name):

	folder_name = re.sub(" \(Disc [+0123456789]\)", "", name) # shave disc number from multi-disc CHD/ISO games
	folder_name = re.sub(" \(Track [+0123456789]\)", "", folder_name) # shave track number from multi-disc BIN/CUE games
	folder_name = re.sub("\.(bin|chd|cue|iso)", "", folder_name) # shave file extension 
	return folder_name

# --------------- MAIN SCRIPT ---------------

root_dir = os.path.realpath(os.path.dirname(__file__))

# prepare files
files = os.listdir(root_dir)
for f in files:
    if f.endswith((".bin", ".chd", ".cue", ".iso")): 
    	# move file in folder of similar name, making that folder if necessary
        folder_path = os.path.join(root_dir, get_folder_name(f))
        os.makedirs(folder_path, exist_ok = True)
        os.replace(os.path.join(root_dir, f), os.path.join(folder_path, f))
        # print("Move " +  + " to " + os.path.join(folder_path, f), sep="\n")
        continue

    elif f.endswith((".m3u", ".xml", ".txt")):
    	# these files are not supported by MiSTer, and can therefore be safely deleted
    	os.remove(os.path.join(root_dir, f))
    	# print("Delete " + os.path.join(root_dir, f), sep="\n")

	# if f.endswith(".m3u"): 
	# # .m3u files are not supported by MiSTer, and can therefore be safely deleted
	# 	# os.remove(os.path.join(root_dir, f))
	# 	print("Delete " + os.path.join(root_dir, f), sep="\n")