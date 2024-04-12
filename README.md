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
- Extract and create the following folder structure in the notebook
- Run cells (additional comments in notebook)
- Can test differnt omages by switching out test image from test directory

## YOLOv8 usage:
- Open the associated notebook
- Download data_yolo.zip (this contains the annotated dataset in YOLO format)
- Extract and create the following folder structure in the notebook
- Run cells (additional comments in notebook)
- Can test differnt omages by switching out test image from test directory
