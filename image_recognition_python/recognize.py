#!/usr/bin/env python

import argparse
import inception

# Load model and categories at startup                 
model, synsets = inception.load_inception_model()

# Detect image with MXNet
image = inception.load_image('images/banana.jpg')
prob = inception.predict(image, model)
topN = inception.get_top_categories(prob, synsets)
print(topN)
top1_message = inception.get_top1_message(topN)
print(top1_message)

def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()

if __name__ == "__main__":
    main()
