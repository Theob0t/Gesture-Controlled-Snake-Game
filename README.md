## :snake: Gesture Gaming  :snake:
## Gesture Controlled Snake Game 
with Pygame, OpenCV and Keras

## :dart: PROJECT GOAL
The goal of the project is to create a Gesture Conrtolled Snake game for Windows machine.

<p align="center">
  <img src="./data/snake_game.gif" width="800" height="400">

## :memo: REQUIREMENTS

### Software:
-	Welcome Menu (select difficulty)
-	Display current score and store best score locally
-	User plays using gesture (on camera/webcam)

<img src="./data/screen_menu.png" alt="alt text" width="350" height="400" align="left"/> <img src="./data/screen_wasted.png" alt="alt text" width="350" height="400" align="right"/>

<br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/>


### Rules:
-	Snake starts in the center of the screen with size of 10x10 pixels
-	Place food somewhere randomly in the screen
-	Food size is 10x10 pixels
-	Snake can move up, down, right and left
-	When Snake eat food it grows of one block (10x10 pixels)
-	Snake dies if it hits itself or a border of the screen

  
### Capture gestures and predict the move:
- Using OpenCV library you can open your webcam and save each new frame into a jpeg
<img src="./data/opencv.jpeg" alt="alt text" width="800" height="400" align="center"/>
</br>

- Use this jpeg as an input for the neural network model
<img src="./data/move.jpg" alt="alt text" width="1200" height="40" align="center"/>
</br>

- Neural Network built using Teachable Machine by Google https://teachablemachine.withgoogle.com/train
('./model/keras_model.h5' and 'keras_model.py')
<img src="./data/model.jpeg" alt="alt text" width="1200" height="40" align="center"/>
</br>
