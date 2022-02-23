# py-cam
Experimented with **cv2** for pulling and manipulating webcam frames, and then sending the results with **pyvirtualcam** to an OBS Virtual Camera

# Notes

| File | Experiment |
|---|---|
| `textimage` | Fills up a blank image with a single charcter |
| `asciify` | - Turns an image greyscale </br> - Matches each pixel to a char by brightness </br> - Creates an output image of characters |
| `sobel_edge_det` | Experiments with the CV2 Sobel edge detection method. The algorithm params are adjustable with sliders |
| `canny_edge_det` | Experiments with the CV2 Canny edge detection method. The algorithm params are adjustable with sliders |
| `cam_capture` | How can webcam iamges be captured with CV2 |
| `use_obs_vcam` | How can you send custom frames to an OBS Virtual Cam with pyvirtualcam |
| `ascii-cam` | - Gets the current webcam frame </br> - Applies Canny edge detection </br> - ASCII-fies it </br> - Sends the output to the OBS Virtual Cam|

To use the OBS Virtual Cam, all you need to do is
1. Install OBS
2. Start it once
3. Start the Virtual Camera
4. You can now close OBS, and you don't have to have it open when using the Virtual Cam   