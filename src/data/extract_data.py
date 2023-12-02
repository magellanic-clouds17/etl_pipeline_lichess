import requests
import os
import zstandard as zstd   

# URL of the file to download
file_url = 'https://database.lichess.org/standard/lichess_db_standard_rated_2013-01.pgn.zst'

# Local path where you want to save the downloaded file
local_path = r"C:\Users\Latitude\Desktop\Python\portfolio_project_lichess\data\raw"

def download_file(url, local_path):
    # Extract filename from URL
    filename = url.split("/")[-1]
    local_filename = os.path.join(local_path, filename)

    # Check if the file already exists
    if os.path.exists(local_filename):
        print(f"File {local_filename} already exists.")
    else:
    # Stream download to handle large files
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):  # 8KB chunks
                    f.write(chunk)
        return local_filename


# Download the file
downloaded_file = download_file(file_url, local_path)
if downloaded_file:
    print(f"File downloaded to: {downloaded_file}")
