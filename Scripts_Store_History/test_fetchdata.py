# test_fetchdata.py
import subprocess

def test_fetchdata_with_urls():
    urls = [
        "https://policies.google.com/privacy?hl=en-US",
        "https://privacy.umbc.edu/web-site-privacy-statement/",
        "https://github.com/about/developer-policy"
    ]

    # Run fetchdata.py with the URLs
    process = subprocess.run(['python', 'fetchdata.py'] + urls, capture_output=True, text=True)

    # Check the output or return code
    if process.returncode == 0:
        print("fetchdata.py ran successfully.")
        print(process.stdout)
    else:
        print("fetchdata.py encountered an error.")
        print(process.stderr)

if __name__ == "__main__":
    test_fetchdata_with_urls()
