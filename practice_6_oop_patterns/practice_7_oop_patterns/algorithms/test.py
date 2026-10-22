import numpy as np
import cv2

from object_analysis import MonochromeImage, FilteredAnalysis

if __name__ == "__main__":
    img_name = "/home/var/python/practice_6_oop_patterns/practice_7_oop_patterns/data/1.jpg"
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    
    
    filt_bin = FilteredAnalysis(MonochromeImage())
    (x, y, w, h, area) = filt_bin.template_method(
        cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    )
    print("using FilteredAnalysis")
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])