# Crochet Companion
Instance Segmentation for Precise Crochet Stitch Recognition

This repository contains code and documentation for a project focused on automating the instance segmentation of crochet stitches using deep learning models. The goal is to develop robust solutions for accurately identifying individual stitches in crochet patterns. 

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
- Extract and create the following folder structure in the notebook (Only populate "test", "train" and "val" sub-dirs inside the "data" dir. Add an empty "models" dir containing "detectron2_models" sub-dir)
- ![Detectron2 File Structure](/detectron2_file_struct.png)
- Run cells (additional comments in notebook)
- Can test differnt images by switching out test image from test directory



## YOLOv8 usage:
- Open the associated notebook
- Download data_yolo.zip (this contains the annotated dataset in YOLO format)
- Create a dir called "data_yolo" within the main content dir in colab. (quick hack: create a folder in "sample_data", drag-drop to main section and proceed)
- Extract and create the following folder structure in the notebook (Only populate "test", "train" and "valid" sub-dirs inside the "data_yolo" dir. Add an empty "results" dir in the "data_yolo" dir. Add "data.yaml" from "daya_yolo.zip" to "data_yolo" dir)
- ![YOLOv8 File Structure](/yolov8_file_struct.png)
- Run cells (additional comments in notebook)
- Can test differnt images by switching out test image from test directory
