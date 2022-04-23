from typing import List
import cv2
import numpy as np

from node import Node
from point import Point

class Main:

    points: List[Point] = []
    training_index = 0

    def run():
        FRAME_SIDE_PX = 800

        # create node
        node = Node(2)

        # generate points
        for i in range(0, 100):
            x = np.random.randint(0, FRAME_SIDE_PX)
            y = np.random.randint(0, FRAME_SIDE_PX)
            label = 1 if x > y else -1
            Main.points.append(
                Point(x, y, label)
            )

        # run train/draw loop, until Q is pressed
        while(True):

            # train node, one point at a time
            trainer_point = Main.points[Main.training_index]
            node.train([trainer_point.x, trainer_point.y], trainer_point.label)
            Main.training_index += 1
            if Main.training_index >= len(Main.points):
                Main.training_index = 0

            # guess point labels
            for point in Main.points:
                point.guessed_label = node.guess([point.x, point.y])

            # --------------------------------------------------
            # display results
            # --------------------------------------------------

            # create empty frame: (px width, px height, 3 channels), fillvalue
            frame = np.full((FRAME_SIDE_PX, FRAME_SIDE_PX, 3), 255, np.uint8)
            # draw class separator line (for debug)
            cv2.line(
                img=frame,
                pt1=(0, 0),
                pt2=(FRAME_SIDE_PX, FRAME_SIDE_PX),
                color=(255, 0, 0),
                thickness=1
            )
            # add points
            for point in Main.points:
                point_color = (0, 0, 0)
                if point.guessed_label != 0:
                    # point is green, if it's guessed correctly
                    # point is red, if it's guessed incorrectly
                    point_color = (0, 255, 0) if point.guessed_label == point.label else (0, 0, 255)
                    
                cv2.circle(
                    img=frame,
                    center=(point.x, point.y),
                    radius=5,
                    color=point_color,
                    thickness=-1
                )
            # display current weights
            cv2.putText(
                img=frame,
                text=f"w1: {node.weights[0]:.2f} w2: {node.weights[1]:.2f} wb: {node.weights[2]:.2f}",
                org=(0, FRAME_SIDE_PX-10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5,
                color=(0, 0, 0),
                thickness=1
            )
            # handle mouse click
            cv2.namedWindow('frame')
            cv2.setMouseCallback('frame', Main.on_mouse_click)
            # draw frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def on_mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # add new point at mouse position
            Main.points.append(
                Point(x, y, (1 if x > y else -1))
            )
    


if __name__ == '__main__':
    Main.run()