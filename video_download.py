!pip install --upgrade youtube-dl
import os
import warnings
warnings.filterwarnings("ignore")



def download_list(urls, prefix):
  '''
  urls should pass a list of urls
  prefix should be a name to prefix file names e.g. 'Jone Doe - '
  filename will end with the video id by default
  =====================================
  Notebook originally done in Google Colab, so minor adaptions may be needed
  '''
 
  # The path to the directory / folder to store videos; this example is specifically for Google Colab.
  path = '/content/videos'
  # Checks to see if the directory / folder exist and if it doesnt it will generate it 
  if not os.path.exists(path):
    os.mkdir(path)
  # Loops through each url in the list and downloads the url
  for url in urls:
      !youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {url}

    


    # Get a list of all files in the specified directory.
  files = os.listdir(path)

    # Rename each file by appending the prefix to the beginning of the file name. This is so I know what project each video is for.
  for file in files:
      idx = file.find('-')

      os.rename(file, os.path.join(prefix + file))
