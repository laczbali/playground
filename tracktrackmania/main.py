from mss import mss
import numpy as np
import cv2
import math

class Main:

    slider_on = False
    slider_value = 0

    def run():
        # generate distance measurement lines
        num_lines = 15
        line_angle_diff = 180 / (num_lines+1)
        line_length = 640
        start_point = (320, 300)
        dist_lines = []
        for i in range(1, num_lines + 1):
            end_point = (
                math.floor(start_point[0] + math.cos(math.radians(i * line_angle_diff)) * line_length),
                math.floor(start_point[1] + math.sin(math.radians(i * line_angle_diff)) * line_length * -1)
            )
            dist_lines.append((start_point, end_point))


        # process frame
        while True:
            with mss() as sct:
                # capture the relevant part of the game window
                frame = np.array(
                    sct.grab(
                        {'top': 150, 'left': 0, 'width': 640, 'height': 300}
                    )
                )

                # frame pre-processing
                fr_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                fr_blur = cv2.GaussianBlur(fr_grey, (5, 5), 0)
                fr_wallmask = cv2.inRange(fr_blur, 0, 43)
                fr_edges = cv2.Canny(fr_wallmask, 50, 150)
                fr_lines = np.zeros(frame.shape, np.uint8)
                    
                # generate hough lines
                lines = cv2.HoughLinesP(fr_edges, 1, np.pi / 180, 50, maxLineGap=50)
                if lines is None:
                    lines = []
                # for line in lines:
                #     x1, y1, x2, y2 = line[0]
                #     cv2.line(fr_lines, (x1, y1), (x2, y2), (0, 255, 0), 1)

                # draw distance measurement lines, and calculate distances
                for dist_line in dist_lines:
                    # get intersections with hough lines
                    intersections = []
                    for hough_line in lines:
                        intersection = Main.line_intersection(
                            dist_line[0][0], dist_line[0][1],
                            dist_line[1][0], dist_line[1][1],
                            hough_line[0][0], hough_line[0][1],
                            hough_line[0][2], hough_line[0][3]
                        )
                        if intersection is not None:
                            intersection[0] = int(intersection[0])
                            intersection[1] = int(intersection[1])
                            hough_x = range(
                                min(hough_line[0][0], hough_line[0][2]),
                                max(hough_line[0][0], hough_line[0][2])
                            )
                            hough_y = range(
                                min(hough_line[0][1], hough_line[0][3]),
                                max(hough_line[0][1], hough_line[0][3])
                            )
                            if intersection[0] in hough_x and intersection[1] in hough_y:
                                intersections.append(intersection)


                    # draw intersection, if there is one
                    if len(intersections) > 0:
                        # get closest intersection (highest Y coordinate)
                        intersections.sort(key=lambda x: x[1])
                        closest_intersection = intersections[-1]

                        # draw red circle at closest intersection
                        cv2.circle(frame, (int(closest_intersection[0]), int(closest_intersection[1])), 5, (0, 0, 255), -1)

                    # draw distance measurement line
                    cv2.line(
                        frame,
                        dist_line[0],
                        dist_line[1],
                        (255, 0, 0),
                        1
                    )

                # display
                # cv2.imshow('blur', fr_blur)
                # cv2.imshow('mask', fr_wallmask)
                # cv2.imshow('edges', fr_edges)
                # cv2.imshow('lines', fr_lines)
                cv2.imshow('frame', frame)

                if not Main.slider_on:
                    # cv2.createTrackbar('slider', 'mask', 0, 255, Main.slider_change)
                    Main.slider_on = True

                if (cv2.waitKey(1) & 0xFF) == ord('q'):
                    cv2.destroyAllWindows()
                    break

    def slider_change(value):
        Main.slider_value = value

    def line_intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        try:
            A = np.array([[ax1, ay1], [ax2, ay2]])
            B = np.array([[bx1, by1], [bx2, by2]])
            t, s = np.linalg.solve(np.array([A[1]-A[0], B[0]-B[1]]).T, B[0]-A[0])
            return (1-t)*A[0] + t*A[1]
        except:
            # no intersection
            return None

if __name__ == "__main__":
    Main.run()