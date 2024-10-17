import requests
from bs4 import BeautifulSoup
from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
from concurrent.futures import ThreadPoolExecutor

def download_and_convert_image(url, dest_path):
    try:
        # Download image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Get filename from URL
            filename = url.split("/")[-1]
            # Ensure it has an extension (if not, assume.jpg for simplicity)
            if '.' not in filename:
                filename += '.jpg'
            # Full path for saving
            save_path = os.path.join(dest_path, filename)

            # Save and convert to JPEG if not already
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            # Convert to JPEG if necessary
            if filename.lower().endswith(('.png', '.gif', '.bmp', '.tiff')):
                img = Image.open(save_path)
                rgb_img = img.convert('RGB')  # Required for JPEG
                rgb_img.save(save_path, 'JPEG')
                os.remove(save_path.replace('.jpg', '.' + filename.split('.')[-1]))  # Remove original
                print(f"Converted and Saved: {filename}")
            else:
                print(f"Saved (already JPEG): {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

def main():
    # Create main window (will be withdrawn later, but necessary for dialog boxes)
    root = tk.Tk()
    root.withdraw()  # Hides the Tkinter window

    # Open dialog box to accept input link
    while True:
        url = simpledialog.askstring("Input", "Enter the website link (or 'Exit' to quit)")
        if url is None or url.lower() == 'exit':
            messagebox.showinfo("Exiting", "Goodbye!")
            return
        if url.startswith("http"):  # Basic validation
            break
        messagebox.showerror("Invalid URL", "Please enter a URL starting with 'http'.")

    # Open dialog box to choose destination
    dest_path = filedialog.askdirectory(title="Select Destination Folder")
    if not dest_path:
        messagebox.showinfo("No Directory Selected", "Exiting due to no directory selected.")
        return

    # Ensure directory exists (should, since we just selected it, but for completeness)
    os.makedirs(dest_path, exist_ok=True)

    # Download webpage and parse for images
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')

        # Extract image URLs (assuming they are absolute or will be correctly resolved by requests)
        image_urls = [img['src'] for img in images if img.has_attr('src')]

        # For any relative URLs, attempt to make them absolute (simple approach, might not cover all cases)
        for i, img_url in enumerate(image_urls):
            if not img_url.startswith("http"):
                image_urls[i] = url + img_url

        # Multi-threaded download and conversion
        with ThreadPoolExecutor() as executor:
            executor.map(lambda url: download_and_convert_image(url, dest_path), image_urls)

        messagebox.showinfo("Complete", "All images downloaded and converted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
