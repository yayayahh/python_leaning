# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/7 0007 10:59
# @Project : python_leaning
# @FileName: demo_logging.py

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('debug.........')
logging.info('info...........')
logging.warning('warning.......')
logging.error('error............')
logging.critical('critical...........')