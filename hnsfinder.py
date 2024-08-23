import requests
from bs4 import BeautifulSoup
import argparse
import sys

def find_hidden_links(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            hidden_links = []
            for link in soup.find_all('a', attrs={'style': 'display:none'}):
                href = link.get('href')
                if href and href not in hidden_links:
                    hidden_links.append(href)
            return hidden_links
        else:
            sys.exit(f"[ERROR] Failed to retrieve page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"[ERROR] An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Hidden Links Finder Tool")
    parser.add_argument('url', type=str, help="URL of the website to scan for hidden links")
    args = parser.parse_args()

    print(f"[INFO] Scanning {args.url} for hidden links...\n")
    hidden_links = find_hidden_links(args.url)
    
    if hidden_links:
        print("[SUCCESS] Hidden links found:")
        for link in hidden_links:
            print(f"  - {link}")
    else:
        print("[INFO] No hidden links found.")

if __name__ == "__main__":
    main()
