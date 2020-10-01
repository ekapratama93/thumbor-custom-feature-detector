#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2020 Eka Cahya Pratama <ekapratama93@gmail.com>

import cv2
import numpy as np

from thumbor.detectors import BaseDetector
from thumbor.point import FocalPoint
from thumbor.utils import logger


class Detector(BaseDetector):
    async def detect(self):
        engine = self.context.modules.engine
        try:
            img = np.copy(
                engine.convert_to_grayscale(update_image=False, alpha=False)
            )
        except Exception as error:
            logger.exception(error)
            logger.warning(
                "Error during feature detection; skipping to next detector")
            return await self.next()

        mode = 'ORB'
        if hasattr(self.context.config, 'CUSTOM_FEATURE_DETECTOR_ALGORITHM'):
            mode = self.context.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM\
                    .upper()

        max_feature = 20
        if hasattr(self.context.config, 'CUSTOM_FEATURE_DETECTOR_MAX_FEATURE'):
            max_feature = int(
                self.context.config.CUSTOM_FEATURE_DETECTOR_MAX_FEATURE
            )

        threshold = 100
        if hasattr(self.context.config, 'CUSTOM_FEATURE_DETECTOR_THRESHOLD'):
            threshold = int(
                self.context.config.CUSTOM_FEATURE_DETECTOR_THRESHOLD
            )

        # default ORB detector
        detector = None
        if mode == 'FAST':
            detector = cv2.FastFeatureDetector_create(threshold=threshold)
        elif mode == 'AGAST':
            detector = cv2.AgastFeatureDetector_create(threshold=threshold)
        elif mode == 'AKAZE':
            detector = cv2.AKAZE_create(threshold=0.008)
        elif mode == 'BRISK':
            detector = cv2.BRISK_create(thresh=threshold)
        elif mode == 'SIFT':
            detector = cv2.SIFT_create(nfeatures=max_feature)
        else:
            detector = cv2.ORB_create(nfeatures=max_feature)

        try:
            keypoints = detector.detect(img)
        except Exception as error:
            logger.exception(error)
            logger.warning(
                "Error during feature detection; no keypoint detected")
            return await self.next()

        points = cv2.KeyPoint_convert(keypoints)

        if points is not None:
            for point in points:
                x_pos, y_pos = point
                self.context.request.focal_points.append(
                    FocalPoint(x_pos.item(), y_pos.item(), 1)
                )
            return

        await self.next()
