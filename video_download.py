import warnings
import os
!pip install --upgrade youtube-dl
warnings.filterwarnings("ignore")

def download_list(urls, prefix):
  '''
  urls should pass a list of urls
  prefix should be a name to prefix file names e.g. 'Jone Doe - '
  filename will end with the video id by default
  =====================================
  Notebook originally done in Google Colab, so minor adaptions may be needed
  '''
  
  for url in urls:
      !youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {url}

    

    # Get the current working directory.
  path = '/content/videos'

    # Get a list of all files in the current working directory.
  files = os.listdir(path)

    # Rename each file by appending the prefix to the beginning of the file name.
  for file in files:
      idx = file.find('-')

      os.rename(file, os.path.join(prefix + file))
