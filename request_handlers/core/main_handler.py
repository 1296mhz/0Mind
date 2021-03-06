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


class MainHandler(BaseHandler):

	def __get_service_info(self)->dict:
		return {
			'service': self.get_service().__class__.__name__,
			'id': self.get_service().get_id(),
			'options': self.get_service().get_options()
		}

	def get(self):
		self.write(self.__get_service_info())
		self.finish()

	def post(self):
		self.write(self.__get_service_info())
		self.finish()

