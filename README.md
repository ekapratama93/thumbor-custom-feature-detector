# thumbor-custom-feature-detector

[![codecov](https://codecov.io/gh/ekapratama93/thumbor-custom-feature-detector/branch/master/graph/badge.svg?token=ZXDhWC2oWO)](https://codecov.io/gh/ekapratama93/thumbor-custom-feature-detector)

This is a thumbor extension enabling a custom algorithm for feature detection. For comparison between algorithm, you can read this [paper](https://ieeexplore.ieee.org/document/8346440) or this [stackoverflow answer](https://stackoverflow.com/questions/49963061/what-is-the-best-feature-detection/56901836#56901836). You can compare it yourself using provided [Jupyter Notebook](FeatureDetection.ipynb).

This library only works with Thumbor >=7.0.0a1 and Python >=3.6.
Tested using Thumbor 7.0.0a5 and Python 3.6

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

### Randomize detections

In some threshold based algorithm, it might detects a lot of features. You can randomize which feature get selected using `CUSTOM_FEATURE_DETECTOR_RANDOMIZE_DETECTION`. The default behaviour is to select first 20 features detected. Beware that randomize the detection is not deterministic, which means that it might get different result on each processing. You might want to cache the detection result.

### Config file

```python
CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'ORB'
CUSTOM_FEATURE_DETECTOR_THRESHOLD = '100'
CUSTOM_FEATURE_DETECTOR_MAX_FEATURE= '20'

CUSTOM_FEATURE_DETECTOR_RANDOMIZE_DETECTION = 'False'

DETECTORS = ['thumbor_custom.detectors.feature_detector',]
```
