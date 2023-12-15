## openopensource

# This Python code uses the OpenCV to capture video from webcam, detect face, and overlay random Christmas stickers on detected faces. Lastly, add red frames on up and down edges and green frames on left and right edges.

1. import Libraries
	cv2: OpenCV
	numpy: numerical operation
	random: generating random number
	time: time-related function

2. Load the Haar Cascade classifier for face detection

3. Capture video from the default webcam ( index 0 )

4. Wait for 5 seconds before capturing frame

5. Release the webcam after the initial waiting period

6. Use the Haar Cascade classifier to detect faces in the captured frame

7. Load Christmas stickers ( Santa, Snowman, Rudolph, Wreath, Tree ) with an alpha channel ( -1 for loading transparency )

8. Set up variables for decorating the frame with red and green frame

9. Create a copy of the original image to overlay stickers and frames

10. Add red and green frames at the top, bottom, left, and right edges of the image

11. Overlay random stickers on detected faces
	randomly select a sticker for each detected face
	resize the sticker to fit within the face region
	randomly position the sticker within the face region
	overlay the sticker on the face, considering transparency

12. Display the result image with overlaid stickers and frames

13. Save the result image as 'result_image.png'

14. Wait for a key press and then close all OpenCV window

# How to implement it
If you enter 'python + code file name' in Anaconda, the webcam screen will appear. And if you keep your pose so that your face is visible within the time limit, you will get a pretty picture using Christmas stickers.

![result](https://github.com/SaNaEEEEE/openopensource/blob/main/result_image.png?raw=true)
