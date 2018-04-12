#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2017, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Maxim Morskov"
__site__ = "http://0mind.net"

from components.base_handler import *


class ModelHandler(BaseHandler):
	_http_attributes = ['id']
	_model_id = None

	def prepare(self):
		self._validate_data(self.request.arguments, self.get_http_attributes(), container_type='HTTP')
		self._model_id = int(self.get_argument('id'))
		if not self.get_service().is_model_exists(self.get_model_id()):
			self._raise_error(
				404,
				'{}: model_id={} not found in pool_id={}'.format(
					self.__class__.__name__,
					self.get_model_id(),
					self.get_service().get_id()
				)
			)
		super().prepare()

	def get_model_id(self):
		return self._model_id

	def get_http_attributes(self):
		return self._http_attributes
