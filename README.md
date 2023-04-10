# youtube_playlist_parser
Parse a YouTube playlist file in order to get a list of video title and URL's for each in a text file.



I made this script to save my playlist title and YouTube links in a text file. This same logic could probably be used in a Chrome (or other browser) extension or an online web service. I'm not going to be making those at this time but here is a script that you can use with minimal effort and time.

I gave a brief example text file and output so you can see what it will look like! Each line will be in this format. Keep in mind no modification of the YouTube title is done so a messy title will be messy in the file too.

Example Output<br />
`TITLE OF SONG 1,URL TO YOUTUBE 1`<br />
`TITLE OF SONG 2,URL TO YOUTUBE 2`

# Prerequisites
* Using Chrome is the easiest way to do this. You can do it in other browsers but I'll include instructions for Chrome only at this time.
* Get a text copy of your YouTube playlist and save it to a directory as a .txt file.
	* Use the steps below to get the information you need!

# Running The Script
* Place the files path into the `file_path` variable. I have left my example there.
	* The script will automatically parse out the directory for you and save there as well. **No need to modify anything else!**

# YouTube Playlist File
There is a easy way to do this in the browser. There is a faster way and a slower way and I'll give you both.

1. Start by going to YouTube and opening the playlist.
2. Scroll to the bottom of the playlist.
	* **Important** If you don't do this, you will not get all songs loaded into the DOM. This means your list will only consist of the first 100 videos!
3. Press **F12** to open the developer console. Select the **Elements** tab. Proceed to the **More Data** or **Less Data** technique.

## More Data
**Note**: This method will be easier since you won't need to do anything except copy the entire page. It's a larger file and slightly slower but overall will get the job done for you.

* Right-click the top line of the elements window, which starts with `<html style="font-size`.
* Select Copy > Copy outerHTML .

## Less Data
**Note**: This method will be faster to parse since it removes all page source code that isn't related to the playlist!

* In the Developer Console, press **Ctrl** + **Shift** + **C**.
	* This will allow you to select elements of the window that you want to find in the source code.
* Highlight the window so that the playlist where all of your videos are located.
	* It will look like you highlighted them all in blue. This will bring you to the line of code that you need.
* Right-Click the line (It will start with `<div id="contents"`).
*  Select Copy > Copy outerHTML.
<br />

4.  Paste this output into a text file and save it to the directory you want to use for this file.
5. Put the file into the program for the `file_path` variable. Include the entire file path (see example above the variable in the code if you need it).
6. Go back to the **Running The Script** section.
