# Object-Detection-Model-Cat-and-Dog
Train and Deploy an object detection model to recognize cat and dog in an image.
     
     (NB: Please read the Description of Model Implementation and Analysis pdf file for details description with visual.)

                                               1. Data Annotation and Pre-processing

1.1	Given dataset consists images of cat and dog and for computer vision project build up we need to annotate our data first. As it is mentioned in the task to annotate the images using bounding box, we use “Roboflow” to annotate our dataset using bounding box. As shown below red highlighted dataset is annotated for further implementation.

1.2	Total 102 images are provided for the task, where one image skipped which seems pretty low quality to be annotated and eventually will responsible for poor performance. As we can see, there are 101 annotated images with two classes (cat and dog).
 
 Annotated dataset in Roboflow: https://app.roboflow.com/urmi/object-detection-model-to-recognize-cat-and-dog/generate/preprocessing
	
1.3	Pre-processing and Augmentation: We did some preprocessing like: auto-orientation, re-sizing, auto-adjust contrast, etc for enhancing our dataset. Also augmented our dataset like: did crop, shear, etc in order to get precise performance from our dataset.

                                                  2. Object Detection Model using Yolov5

    Step: 01 (Installing and Importing prerequisites and Dataset)
2.1	After annotating dataset we implemented our model in google colab. Here we used Yolov5 for our object Detection Model. We clone yolov5 also install, import essentials prerequisites to build our model.

2.2	We already installed Roboflow and below we’re importing roboflow in order to generating API key of our dataset in roboflow.
	
2.3	Using API key from above we getting  path like this and which we define in the  cell for further implementation.
	
	
    Step: 02 (Training Dataset using Yolov5)
2.4 Our image is given 640x640 size, taking image as 640, total batches are 16 and we ran 100 epochs in order to train our dataset. 
Locating the dataset, our dataset location is saved in (dataset.location). Specify a path to weights to start transfer learning, we choose generic pretrained checkpoint.

So, we ran our model using 100 epochs and finally got the score or model summary: where we can see all the layers, parameters, performance measurement scores and also model object, class, and box losses.                                   

    Step: 03 (Evaluate YOLOv5 Detector Performance)
2.5	Training loss and performance metrics are saved to Tensorboard and to a logfile. As shown below dashboard, a complete overview of our trained models. Tensorboard showing our models performance measurement scores graphs (Precision, recall scores in increasing manner). Also showing losses like: class, object, box losses (are in decreasing manner). More analysis and visualization can be found in the Tensorboard.



    Step: 04 (Run Inference with Trained Weights)
2.6	Running inference with a pretrained checkpoints on context of test/images folder downloaded from Roboflow so that we can move on test model.
 
    Step: 05 (Test Model Using Test Dataset)
2.7	Before move into testing phase, we must be careful about the path above. Importing glob to define the path and uploading test images. Now we’ll use above saved result in the path to test our model using test dataset.

2.8	Test image in the model showed confidence score of detecting a dog as .53 and a cat is 0.79 in a bounding box which established as a pretty good model. Since dog image is quite blur that’s why it’s score poor than cat.

    Step: 06 (Model Validation)
2.8	Model Validation included Class of image, total instances. Performance measurement scores and Our model Performance measures are getting from precision, recall scores. Also, Model class, object, bounding box loss analysis (which we can also find in Tesnorboard dashboard above).

2.9	Traditional precision-confidence curve showing below to give an overview of the result of detection of cat and dog.

	Step: 07 (Test model performance using random image from internet)
3.0	We can upload random image and copy path in the source to test our model performance randomly. As below, we can see our model did pretty well on detecting cat and dog on random image (performance score can vary based on environment and set up). As we can see, confidence score is 0.74 for dog and 0.67 for cat.

    Step: 08 (Save the Model)
3.1	 We are saving our model so that we can build API in streamlit using .pt file for common usages of our model. Convenient User Interface to understand our work and implemented model.	
In the next step, we are saving and downloading .pt file and yolov5 model. We’re going to use .pt file for making API using streamlit in the VSCode.

                                            3. Python API framework to Recognize Cat and Dog

3.1	For API we made a folder called ObjectDetection and where we saved .pt file which downloaded from our previously saved model. Now in VSCode we installed streamlit and other required python packages to build our API and import those libraries in the app.py file.

    We define .pt file path in the model for recall all model implementation.

3.2	After defining function, streamlit app, creating uploader using st.file uploader and initializing type, loading images and performing object detection, displaying list of image using bounding box and confidence score in the app.py file.  Run the command streamlit run app.py

3.3	“local url” going to shift us to the browser showing “Cat and Dog Detection Model” and ask to browse image. And then detect the image and confidence score.
	
	We need to click on browse files icon and provide random cat and dog image.

