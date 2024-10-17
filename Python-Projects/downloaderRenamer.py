import os
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from tkinter import filedialog, messagebox, simpledialog

import requests
from bs4 import BeautifulSoup
from PIL import Image


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

def process_images_in_directory(dest_path):
    """
    Renames images in the chosen directory to 'img-(i).jpg' where 'i' is the increment.
    Identifies 4K+ resolution images, moves them to a '4K Images' sub-dir, and renames them.
    Ignores non-image files.
    """
    # Create '4K Images' sub-directory if it doesn't exist
    R4k_dir = os.path.join(dest_path, '4K Images')
    os.makedirs(R4k_dir, exist_ok=True)

    image_files = [f for f in os.listdir(dest_path) if f.lower().endswith(('.png', '.jpg', '.gif', '.bmp', '.tiff', '.jpeg'))]
    img_counter = 1  # Counter for all images
    img_4k_counter = 1  # Counter for 4K+ images

    for filename in image_files:
        file_path = os.path.join(dest_path, filename)
        try:
            # Attempt to open as image to verify it's a valid image file
            with Image.open(file_path) as img:
                width, height = img.size
                resolution = width * height

                # Assuming 4K resolution is approximately above 8 million pixels (e.g., 3840x2160)
                if resolution > 8000000:
                    # Move to '4K Images' dir and rename
                    new_filename = f"4K-img-{img_4k_counter}.jpg"
                    new_path = os.path.join(R4k_dir, new_filename)
                    os.rename(file_path, new_path)
                    print(f"Moved & Renamed (4K+): {new_filename}")
                    img_4k_counter += 1
                else:
                    # Rename in original directory
                    original_extension = os.path.splitext(filename)[1].lower()
                    new_filename = f"img-{img_counter}{original_extension if original_extension!= '.jpeg' else '.jpg'}"
                    os.rename(file_path, os.path.join(dest_path, new_filename))
                    print(f"Renamed: {new_filename}")
                    img_counter += 1
        except IOError:
            print(f"Ignoring non-image file: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

def main():
    # Create main window (will be withdrawn later, but necessary for dialog boxes)
    root = tk.Tk()
    root.withdraw()  # Hides the Tkinter window

    # Open dialog box to accept input link (optional)
    url = simpledialog.askstring("Input (Optional)", "Enter the website link (leave blank or type 'Exit' to quit, or just choose a directory for renaming)")
    if url is not None and url.lower() == 'exit':
        messagebox.showinfo("Exiting", "Goodbye!")
        return

    # Open dialog box to choose destination (always required now)
    dest_path = filedialog.askdirectory(title="Select Directory (for downloading images or renaming existing ones)")
    if not dest_path:
        messagebox.showinfo("No Directory Selected", "Exiting due to no directory selected.")
        return

    # Ensure directory exists (should, since we just selected it, but for completeness)
    os.makedirs(dest_path, exist_ok=True)

    if url is None or not url.startswith("http"):  # Skip downloading if no valid URL
        messagebox.showinfo("Skipping Download", "No valid URL provided. Proceeding to rename images in the chosen directory.")
        process_images_in_directory(dest_path)
        messagebox.showinfo("Complete", "Images in the directory have been processed.")
    else:
        try:
            # Download webpage and parse for images
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

            # Process images after download
            process_images_in_directory(dest_path)
            messagebox.showinfo("Complete", "All images downloaded, processed, and renamed accordingly.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
