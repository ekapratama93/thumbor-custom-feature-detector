# thumbor-custom-feature-detector

[![codecov](https://codecov.io/gh/ekapratama93/thumbor-custom-feature-detector/branch/master/graph/badge.svg?token=ZXDhWC2oWO)](https://codecov.io/gh/ekapratama93/thumbor-custom-feature-detector)

This is a thumbor extension enabling a custom algorithm for feature detection. For comparison between algorithm, you can read this [paper](https://ieeexplore.ieee.org/document/8346440) or this [stackoverflow answer](https://stackoverflow.com/questions/49963061/what-is-the-best-feature-detection/56901836#56901836). You can compare it yourself using provided [Jupyter Notebook](FeatureDetection.ipynb).

## Configuration

You can control which algorithm is used by using `CUSTOM_FEATURE_DETECTOR_ALGORITHM`. The supported algorithm is:

1. ORB (default)
2. FAST
3. AGAST
4. AKAZE
5. BRISK
6. SIFT*

*Some articles say that SIFT is patent protected so be careful about using it for your business setup

Some algorithms also use threshold and max number of features you can control both using `CUSTOM_FEATURE_DETECTOR_THRESHOLD` and `CUSTOM_FEATURE_DETECTOR_MAX_FEATURE`.
