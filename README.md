                                                       <!-- AI Virtual Keyboard : -->

# AI_Virtual_Keyboard
 
AI Virtual Keyboard Using Computer vision

Overview:
Computer Vision:
Computer vision is a process by which we can understand the images and videos how they are stored and how we can manipulate and retrieve data from them. Computer Vision is the base or mostly used for Artificial Intelligence. Computer-Vision is playing a major role in self-driving cars, robotics as well as in photo correction apps. The best and the most often used library to use computer vision is Opencv.

OpenCV:
OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as NumPy, python is capable of processing the OpenCV array structure for analysis. To Identify image pattern and its various features we use vector space and perform mathematical operations on these features.

Applications of OpenCV:
There are lots of applications which are solved using OpenCV, some of them are listed below -

· Face Recognition (Most popular).

· Automated inspection and surveillance.

· Counting population of an area.

· Vehicle counting on highways along with their speeds.

· Anomaly (defect) detection in the manufacturing process.

· Image Processing (Used alongside AI in Photoshop to remove backgrounds).

· Video/image search and retrieval.

· Driver-less car navigation and control.

· Object recognition.

· Medical image analysis, etc.

Just like all these applications, there are also fun and unique ways to use Opencv, like I tried and created a virtual AI-based Keyboard which allows the person to type only by using his two fingers. Feels magical right, using only your 2 fingers you can type accurately and fast rather than having your 10 fingers and still typing slowly. The amazing this about this code is you can also type in Word or anywhere else.


Cvzone :
It is a library which comprises of cv2,mediapipe(another computer vision library) and other scientific libraries like math to create classes and functions which simplifies the whole detection process. It has Hand Detection, Pose Detection, etc. which are in use by most of the detection programs.



<!-- How mediapipe’s detection works -->
As per the above, the mediapipe spilts the hand into point segments on which numpy and other libraries are implemented to create a class HandTrackingModule.
Other modules work on the same principle of segmentation and it becomes easier for us to immplement it.


<!-- Building the project -->
1) Installing and Importing Dependencies :
The first stage to start any project is to finalize its libraries. We are going to use cv2,cvzone,numpy,time and pynput.

Cv2 — Used to capture real time video to recognize where is the hand.

Time — To record time between key presses (If it extends a certain period of time we can conclude that the key is pressed and not clicked)

Pynput — To type into directly into any application like NotePad, Whatsapp, etc.

Numpy — T o measure the distance between tips of fingers for pressing of a key.

Cvzone — This is a specialized which you have to install first and then import. It contains various popular modules like FaceTracking, HandTracking, PoseRecogition, etc which, in our case, are going to use to track our hand and fingers.



2) Setting up Global Variables :
After import packages we are going to create variables and assign values to them which we are going to use further in the project.

cap is used to capture the video from the camera 0 (most of the time it is the camera on your laptop) and cap.set sets the resolution of the video.

HandDetector() module is initialized to the variable detector through which we are going to access its functions.

We assigned keys variable to a list of all the alphabets which we are going to display on the screen

Keyboard is initialized to Controller() by which we can write in other applications.




3) Defining Function drawall() :

This function takes in the video getting captured by the camera and the buttons list which we created in the class and returns the formatted buttons.

When called, it displays the alphabets from the buttonList variable on the screen with font size, shape, colour, position mentioned in its loop.



4) Defining class Button() :

<!-- class Button() -->
It is a class which changes alphabets to buttons by assigning position, size, font to them.

It is called in a loop which takes in the alphabets from the list one by one and after changing them assigns them to a buttonList which is sent to the drawall() function.



5) Looping through the process :

<!-- For capturing and printing the data -->
As we are capturing a video and not a photo, we must set an infinite loop which can take in photo slides and also display the buttons on the screen.

The first 4 lines will take in the video from camera, display the buttons and check if there is hand is present in front of camera or not.

If hand(lmlist) is present then it will check the distance between the index finger and the middle finger

If the distance between them is less than 30 and their midpoint is on an alphabet then that alphabet gets printed.

The last four lines are used to display a textbox on screen where the pressed alphabets gets printed and displayed to the user.

And the now you can show this implementation to kids who will get excited and suprised.

I have made some some changes in the HandTrackingModule which I have posted below along with the Keyboard code. Have both the code files in same depository.



Output:


Interface

![1 (Interface)](https://github.com/user-attachments/assets/46aa65a3-1bf1-4070-90ef-99845130da7f)

Hand Position

![2 (Hand Position)](https://github.com/user-attachments/assets/650fb893-60e9-49fb-8085-f2f36b79f20d)

FingersWorks

   ![3  w(FingersWorks)](https://github.com/user-attachments/assets/90d3942d-f12c-488a-9278-ce3849c05b22)
   
