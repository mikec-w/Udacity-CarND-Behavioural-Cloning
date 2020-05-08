# Download training data for the Behavioural Cloning Project
# Note data will be lost when workspace is reset

# Put data in /opt/data

mkdir /opt/data
cd /opt/data
rm -rf *


# Get data from onedrive (mikecw@gmail.com account)

# Sample Data link
#wget -O sample_data.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21148&authkey=AEpzRSDtPGdZT3s"
#unzip sample_data.zip
#rm -r __MACOSX/
#rm sample_data.zip

# User Generated Data link
#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21149&authkey=AOXLWZPtnFONfiY"

#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21152&authkey=ACidCPiXhczNa5E"
#unzip track1.zip
#rm track1.zip

# XBox Controller Data - 3 laps in each direction

#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21154&authkey=AIkotavr4gEpzlU"


# Xbox Controller as above but with some recovery driving... - No Good - deleted
#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21155&authkey=AEyXnzHGATWG9k8"


# Xbox Controller as above plus some driving to reinforce corner after bridge.

#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21156&authkey=AHtOO36JRTJ_8iY"


# Even more training of the corner!!!
#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?#cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21157&authkey=ACGxfpHs2L8IJFI"


# Basic one lap data

#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21158&authkey=ABBL0VGgnPzTVaE"

#mv driving_log.csv driving_log1.csv

# BEST ONE SO FAR
#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21159&authkey=AC8ZxbN8CQMpgEg"


wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21160&authkey=AGtiUB699xD8KbU"

# Unzip 
unzip track1.zip
rm track1.zip


