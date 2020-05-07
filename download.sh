# Download training data for the Behavioural Cloning Project
# Note data will be lost when workspace is reset

# Put data in /opt/data

mkdir /opt/data
cd /opt/data

# Get data from onedrive (mikecw@gmail.com account)

# Sample Data link
#wget -O sample_data.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21148&authkey=AEpzRSDtPGdZT3s"
#unzip sample_data.zip
#rm -r __MACOSX/
#rm sample_data.zip

# User Generated Data link
#wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21149&authkey=AOXLWZPtnFONfiY"

wget -O track1.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21151&authkey=AClFBjzrDCWwwyc"

unzip track1.zip
rm track1.zip

# Unzip 

