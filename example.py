# identify current working directory
!pwd
# moves into videos directory
%cd videos

# list of urls I want to download
url = [
  'link',
  'link',
  'link',
]

#calls function, either copy and paste fuction from the video_download.py file or use sys library to append the pathway to import the py file into a notebook
downloadlist(url, 'John Doe - ')
