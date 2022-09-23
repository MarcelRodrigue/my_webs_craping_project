
    # importing library

import requests
  # custom headers
headers = {
        "User-Agent": "Chrome/51.0.2704.103",
}
 # target url
url = "https://estatements.unmeetings.org/estatements/14.0447/20220801/oug8GrlV9JNU/rsX7YJvxNVCK_en.pdf"

def download_pdf(url, file_name, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    # ill write  function go generate custom file names
    file_name = "file1.pdf"
    download_pdf(url, file_name, headers)