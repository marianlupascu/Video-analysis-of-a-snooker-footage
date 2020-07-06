Computer Vision - Project 1
Automatic grading of multiple choice tests
Lupascu Marian

1. Packages and libraries used:
google-colab==1.0.0
numpy==1.18.5
opencv-python==4.1.2.30

2. Running each task separately
First you need to make a series of initializations and imports from the 'Imports' section, namely: cells #3, 4, 7

2.1 Task 1
You receive a test set of 57 images of a snooker table seen from above at a random time of a
game (for example the black ball might be potted). The task is to count the number of balls
on the table and specify their color for each of the 57 images in the test set.

init: First you need to make a series of initializations from the 'Task 1' section, namely: cells #1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15
script: cell #1, 2 from 'Running the entire code' section
function: run_task_1(), from cell #1, where the test folder needs to be changed, but because I don't know exactly what the test files will be called
output: the output files is in data_dir_drive + '/output_data/lupascu_marian_407/Task1/i.txt' or './output_data/lupascu_marian_407/Task1/i.txt', i in 1,57

2.2 Task 2
You receive a test set of 25 videos containing a player making a shot. In each of the 25
videos the snooker table is seen from above. The task is to decide whether a ball was potted
into a pocket and if so recognize the color of the potted ball and the pocket (one of the six
pockets) where the ball was potted (1 - top left corner, 2 - top right corner, 3 - bottom left
corner, 4 - bottom right corner, 5 - middle left corner, 6 - middle right corner). In each of
the 25 videos there will be a maximum of one ball being potted.

init: First you need to make a series of initializations: from the 'Task 1' section, namely: cells #1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13
      and from the 'Task 2' section, namely: cells #1, 3, 4, 6, 7, 8, 10
script: cell #3, 4 from 'Running the entire code' section
function: run_task_2(), from cell #3, where the test folder needs to be changed, but because I don't know exactly what the test files will be called
output: the output files is in data_dir_drive + '/output_data/lupascu_marian_407/Task2/i.txt' or './output_data/lupascu_marian_407/Task2/i.txt', i in 1,25

2.3 Task 3
You receive a test set of 25 videos containing a player making a shot. In each of the 25 videos
the snooker table is seen from above. The task is to track the cue ball (the white ball) and
another specifed ball. The initial bounding boxes of the two balls to be tracked are provided
for the frst frame (they follow the format [xmin ymin xmax ymax], where (xmin,ymin) is
the top left corner and (xmax,ymax) is the bottom right corner of the initial bounding-box).
In each video we will consider that your algorithm correctly tracks a ball if in more (greater
or equal) than 80% of the frames your algorithm correctly localizes the ball to be tracked. We
consider that your algorithm correctly localizes the ball to be tracked in a specic frame if the
value of the IOU (intersection over union) beetween the window provided by your algorithm
and the ground-truth window is more than 20%.

init: First you need to make a series of initializations: from the 'Task 1' section, namely: cells #1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13
      from the 'Task 2' section, namely: cells #1, 3, 4, 6, 7, 8 and from the 'Task 3' section, namely: cells #1, 2, 3, 4, 6, 7, 13
script: cell #5, 6 from 'Running the entire code' section
function: run_task_3(), from cell #5, where the test folder needs to be changed, but because I don't know exactly what the test files will be called
output: the output files is in data_dir_drive + '/output_data/lupascu_marian_407/Task3/i_ball_j.txt' or 
'./output_data/lupascu_marian_407/Task3/i_ball_j.txt', i in 1,25, j = 1 and 2

2.4 (bonus) Task 4
You receive a test set of 25 videos containing a player making a shot. Dierent than the
previous tasks, in this videos the snooker table can be flmed from dierent viewpoints (not
only from above). The task is to track the cue ball. The task here is much harder as you have
diferent scales of the cue ball, changes in camera viewpoint, the initial bounding box of the
white ball is not provided. The initial bounding box of the cue ball to be tracked is provided
for the frst frame (it follows the format [xmin ymin xmax ymax], where (xmin,ymin) is the
top left corner and (xmax,ymax) is the bottom right corner of the initial bounding-box). The
rules described at Task 3 apply here, meaning that your algorithm should correctly localizes
the cue ball in more than 80% of the frames, at each frame correctly localization means that
the window provided by your algorithm should have IOU more than 20% with respect to the
ground-truth window.

This task has not been addressed.