# Download training data for the Behavioural Cloning Project
# Note data will be lost when workspace is reset

# Put data in /opt/data

mkdir /opt/data
cd /opt/data

# Get data from onedrive (mikecw@gmail.com account)

# Sample Data link
wget -O sample_data.zip --no-check-certificate "https://onedrive.live.com/download?cid=B7BE61D821A6E0C4&resid=B7BE61D821A6E0C4%21148&authkey=AEpzRSDtPGdZT3s"
unzip sample_data.zip
rm -r __MACOSX/
rm sample_data.zip

# User Generated Data link
# wget --no-check-certificate "https://onedrive.live.com/download?cid=6EBB03E38A53ED3E&resid=6EBB03E38A53ED3E%21116&authkey=AC4lDqtLG8LqfiA"

# Unzip 

