#!/bin/bash

while getopts ":m:" opt; do
  case $opt in
  m) yolov8_model_file=$OPTARG ;;
  \?)
    echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  :)
    echo "Option -$OPTARG requires an argument." >&2
    exit 1
    ;;
  esac
done

if [ ! -e "$yolov8_model_file" ]; then
  echo "Input model file (.pt) does not exist → $yolov8_model_file" >&2
  exit 1
fi
