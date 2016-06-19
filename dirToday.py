# This script creates a folder with today's date on it and
# moves all image files in the current folder into it.
# By Ross Llewallyn

import datetime
import os
import shutil

# Get time and its string representation
today = datetime.datetime.now()
todayStr = today.strftime('%Y_%m_%d')

# Check if directory already exists
if os.path.isdir(todayStr):
    # If so, append the time to make it unique
    todayStr = today.strftime('%Y_%m_%d__%H_%M')

# Now make it!
os.mkdir(todayStr)

# Finally, move all files in the current directory
# into the new one (except the script itself!)

files = os.listdir()
for filename in files:
    if (os.path.isfile(filename) and filename != "dirToday.py"):
        shutil.move(filename, ".\\" + todayStr)
