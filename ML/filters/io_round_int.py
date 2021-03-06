#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2017, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__license__ = "Proprietary"
__version__ = "0.7.1"
__maintainer__ = "Maxim Morskov"
__site__ = "http://0mind.net"

from ML.filters.base_filter import BaseFilter
import numpy as np


class RoundVectorFilter(BaseFilter):
	def _apply(self):
		return np.rint(self.get_data())
