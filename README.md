# yolo-api-service
This repository consists of an example of how to create a API service for your YOLO model (https://pjreddie.com/darknet/yolo/). This is a very simple API implementation where you upload an image and then a the detected objects will appear in text form. You can very easily modify this code to work as an API to suit your needs.

![image](https://github.com/okyang/yolo-api-service/blob/master/api-demo.gif)


# Prerequisites
1. Linux Environment
2. Python 3
3. [Flask](https://pypi.org/project/Flask/)

# Set-up

**This code will only work in a Linux environment**

1. Set-up YOLO Darknet from either https://pjreddie.com/darknet/yolo/ or https://github.com/AlexeyAB/darknet in a Linux based environment. Make sure that you either have the your trained model ready (both a .cfg file and a .weights file).
2. Copy the `app.py` file into the `darknet` repository from step 1
3. In the `app.py` file. Change the function default parameters in `runModel` to match your cfg file location and weights file location. For Example:
```python
runModel(filename,cfgFile="cfg/yolov4.cfg", weightsFile="yolov4.weights")
```

# Run the server locally
1. You can run `python3 app.py` to get your local debugging server ready.
2. Open up the main webpage at `<your_ip_address:5000/predict-image>`
3. You can now upload a image file and get the predicted objects detected.
