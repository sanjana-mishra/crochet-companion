# Crochet Companion
Instance Segmentation for Precise Crochet Stitch Recognition

This repository contains code and documentation for a project focused on automating the instance segmentation of crochet stitches using deep learning models. The goal is to develop robust ssolutions to accurately identify individual stitches within crochet patterns.
![Intro](/face.png)

## The stitches used in this project are:
- Single Crochet Stitch (sc)
- Double Crochet Stitch (dc)
- Treble Crochet Stitch (tr)
- Slip Stitch (slst)

## Code usage:
2 models have been used with respective notebooks (ipynb):
- Detectron2 with Mask-RCNN
- YOLOv8


## Detectron2 with Mask-RCNN usage:
- Open the associated notebook
- Download data_coco.zip (this contains the annotated dataset in COCO format)
- Create a dir called "data" within the main content dir in colab. (quick hack: create a folder in "sample_data", drag-drop to main section and proceed)
- Extract and create the following folder structure in the notebook as shown and upload corresponding images and json files in "train" and "val" dirs (Only populate "test", "train" and "val" sub-dirs inside the "data" dir. Add an empty "models" dir containing "detectron2_models" sub-dir)
- ![Detectron2 File Structure](/detectron2_file_struct.png)
- Run cells (additional comments in notebook)
- Can test different images by switching out test image from test dir



## YOLOv8 usage:
- Open the associated notebook
- Download data_yolo.zip (this contains the annotated dataset in YOLO format)
- Create a dir called "data_yolo" within the main content dir in colab. (quick hack: create a folder in "sample_data", drag-drop to main section and proceed)
- Extract and create the following folder structure in the notebook as shown and upload corresponding images, labels in "train" and "vaid" dirs after creating respective "images" and "labels" dirs within them (Only populate "test", "train" and "valid" sub-dirs inside the "data_yolo" dir. Add an empty "results" dir in the "data_yolo" dir. Add "data.yaml" from "data_yolo.zip" to "data_yolo" dir)
- ![YOLOv8 File Structure](/yolov8_file_struct.png)
- Run cells (additional comments in notebook)
- Can test different images by switching out test image from test dir
