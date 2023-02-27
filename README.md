<h1> ¡Video Dowloader! </h1>

This is a 🔵 **Python Script** 🔵 that uses the pytube library to download a video from YouTube. 


### The function takes three arguments: 
- The **URL** of the video to download. 
- The desired **quality** of the video. 
- The **path** where the video should be saved.

The function first creates an instance of the YouTube class using the provided URL. It then checks whether a specific video quality has been specified and filters the available streams accordingly. 
If no specific quality is requested, it selects the first available stream with an mp4 file extension. It then downloads the video to the specified path using the download() method of the selected stream object.

Before calling the function, the code checks if the specified path exists, and creates it if it does not. 
If an error occurs during the download process, the function prints an error message indicating that the URL may be incorrect.

Overall, this code provides a simple way to download a YouTube video using Python. 
However, it should be noted that downloading videos from YouTube without permission is against their terms of service, so it is important to use this code responsibly and only download videos that you have permission to use.
