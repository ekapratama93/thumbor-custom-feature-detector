#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2020 Eka Cahya Pratama <ekapratama93@gmail.com>

from os.path import abspath

import mock
from preggy import expect
from tornado.testing import gen_test

from thumbor.config import Config
from thumbor.engines.pil import Engine as PilEngine
from thumbor.testing import DetectorTestCase
from thumbor_custom.detectors.feature_detector \
    import Detector as FeatureDetector


class FeatureDetectorTestCase(DetectorTestCase):
    _multiprocess_can_split_ = True

    def get_config(self):
        return Config(
            CUSTOM_FEATURE_DETECTOR_ALGORITHM='ORB',
            CUSTOM_FEATURE_DETECTOR_MAX_FEATURE='20',
            CUSTOM_FEATURE_DETECTOR_THRESHOLD='100',
        )

    def setUp(self):
        super(FeatureDetectorTestCase, self).setUp()
        self.context.config = self.get_config()
        self.context.request = mock.Mock(focal_points=[])
        self.engine = PilEngine(self.context)
        self.context.modules.engine = self.engine

    @gen_test
    async def test_should_detect_multiple_points(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)

        await FeatureDetector(self.context, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_not_detect_points(self):
        with open(abspath("./tests/fixtures/images/1x1.png"), "rb") as fixt:
            self.engine.load(fixt.read(), None)

        await FeatureDetector(self.context, 0, []).detect()
        detection_result = self.context.request.focal_points
        expect(detection_result).to_length(0)

    @gen_test
    async def test_should_use_orb(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'ORB'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_orb_and_limit_1(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'ORB'
        ctx.config.CUSTOM_FEATURE_DETECTOR_MAX_FEATURE = 1
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_equal(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_sift(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'sift'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_sift_and_limit_1(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'sift'
        ctx.config.CUSTOM_FEATURE_DETECTOR_MAX_FEATURE = 1
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_equal(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_fast(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'fast'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_fast_and_no_detection(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'fast'
        ctx.config.CUSTOM_FEATURE_DETECTOR_THRESHOLD = 200
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(detection_result).to_length(0)

    @gen_test
    async def test_should_use_agast(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'agast'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_agast_and_no_detection(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'agast'
        ctx.config.CUSTOM_FEATURE_DETECTOR_THRESHOLD = 200
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(detection_result).to_length(0)

    @gen_test
    async def test_should_use_akaze(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'akaze'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_brisk(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'brisk'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")

    @gen_test
    async def test_should_use_brisk_and_no_detection(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'brisk'
        ctx.config.CUSTOM_FEATURE_DETECTOR_THRESHOLD = 200
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(detection_result).to_length(0)

    @gen_test
    async def test_should_use_default_algorithm(self):
        with open(abspath("./tests/fixtures/images/city.jpg"), "rb") as fixt:
            self.engine.load(fixt.read(), None)
        ctx = self.context
        ctx.config.CUSTOM_FEATURE_DETECTOR_ALGORITHM = 'none'
        await FeatureDetector(ctx, 0, None).detect()
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal("alignment")
