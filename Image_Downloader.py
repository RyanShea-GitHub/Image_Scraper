import os
from bs4 import BeautifulSoup
import requests

from tkinter import ttk
from tkinter import *
from tkinter import filedialog

###########################################
#-----------------------------------------#
#LOGIC FOR SCRAPING IMAGES OFF TARGET SITE#

#target URL for building app 'https://www.thewrap.com/celebrity-mugshots-locklear-downey-jr-photos/'

# Makes a new directory by joining the users chosen directory with the folder created by the user
# requests the text information from the users target URL and beautiful soup extracts and parses the HTML 
# changes directory based on the users chosen Directory
# finds all image tags and ensure that they contain links. story the link and name in variables.
# Open up the newly created file and download and write all of the images to your target destination
def image_Downloader(url_Entry, folder_Entry):
    
    os.makedirs(os.path.join(chosen_dir, folder_Entry))

    r = requests.get(url_Entry)
    soup = BeautifulSoup( r.text, "html.parser")
    images = soup.find_all('img',{"src":True})
    
    os.chdir(os.path.join(chosen_dir, folder_Entry))
    for image in images:                 
        link = image['src']
        name = image.get('alt')

        if link.endswith('.jpg'):
            with open(name.replace(' ', '_') + '.jpg', 'wb') as output_file:
                img = requests.get(link)
                output_file.write(img.content)


# Sets the chosen directory variable to global and passes it to the image scraper function to ensure that the new folder is in the right place
# Sets the starting location in the file explorer to the user tab of the C drive
# sets a label on the GUI to show which directory was chosen by the user
def open_directory_Button():
    global chosen_dir

    chosen_dir = filedialog.askdirectory(initialdir='~', title="Please Select A Directory")
    return ttk.Label(root, text='You have chosen: ' + chosen_dir + ' as your selected Directory').grid(column=1, row=4, columnspan=3)

# sets the variables to global so that they can be used in another function
# sets the strings from the Tkinter Entry fields into variables that the scraping function will use
# Calls the image scraper function and passes it the entry viables as the url and folder name paramaters
def collect_Info():
    global url_Entry, folder_Entry

    url_Entry = user_url_Name.get()
    folder_Entry = user_folder_Name.get()

    image_Downloader(url_Entry, folder_Entry)


##################
#----------------#
#TKINTER GUI CODE#

root = Tk()

window = ttk.Frame(root, padding=50, borderwidth=10)
root.geometry('550x125')
root.resizable(False, False)
root.title('Image Scraper')

window.grid()

# Welcome Message
ttk.Label(root, text='Welcome to the Image Downloader').grid(column=1, row=0, pady=5, ipadx=10, columnspan=3) 

# Label and entry field for user to paste the target URL to be scraped
# Stores the entered URL into a variable that is used later once the user pressed the "download images" button
ttk.Label(root, text='Enter URL: ').grid(column=0, row=2, padx=5) 
user_url_Name = StringVar()
ttk.Entry(root, width=45, textvariable=user_url_Name).grid(column=1, row=2, columnspan=2, pady=2)

# Lets the user enter their own name for the new created folder that will store the scraped images
# Stores the entered folder name into a variable that is used later once the user pressed the "download images" button
ttk.Label(root, text='Folder name: ').grid(column=0, row=3, padx=5) 
user_folder_Name = StringVar()
ttk.Entry(root, width=45, textvariable=user_folder_Name).grid(column=1, row=3, columnspan=2, pady=2)

# Opens up a file explorer for the user to enter their destination for the scraped images to be stored
open_File = ttk.Button(root, text='Choose Directory', command=open_directory_Button).grid(column=0, row=4, pady= 10,padx=10, sticky=E)

# Button that the user will hit once they have entered the proper information and are ready for the images to be scraped
# This button calls a function that will gather the entered data and push it to the main scraping function 
collect_img = ttk.Button(root, text='Download Images', command=collect_Info).grid(column=3, row=2, padx=25, columnspan=2, rowspan=2)

root.mainloop()






