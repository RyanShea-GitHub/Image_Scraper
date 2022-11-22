#############################################
#-------------------------------------------#
#----------PYTHON IMAGE SCRAPER-------------#
#-------------------------------------------#
#############################################

ABOUT
-----------------------------
Used to download images from a target website. You can choose the target directory for your new folder to be added. 
You can also name the folder that you will be creating. This only scrapes .JPG files as that is the most commonly
used extension on web pages. This can be modified for future use if necessary.


HOW TO USE
------------------------------
Paste/Enter the URL that you are trying to scrape. 

Click on the Directory button, and choose the target folder. The created folder containing the images will be 
a subfolder of this chosen directory. You will have this destination confirmed once you have selected it.

You can enter the name of the folder that you will be creating.


Once you are satisfied with the URL, Directory, and Folder name, you can click on the Download button at the 
bottom of the GUI. 


FUTURE IMPLEMENTATION IDEAS
-------------------------------
Choose more than just the .jpg extension, and have selector buttons to toggle only the entension you would like

A window that check the target URL and return the extensions found on the page and the names ('alt' tags) of the
images to help narrow down your needs without having to check the HTML yourself

Choose a maximum number of images that the application will scrape.

Have the user enter a naming scheme for the images, as it currently only tages the name associated with the scraped
tag and removes and disallowed characters/spaces. 

Choose if the user wants to add a new subdirectory or just put the scraped images into the target destination 