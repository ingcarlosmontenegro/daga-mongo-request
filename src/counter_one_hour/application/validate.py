"""Module of Validation for Measure One Hour"""

# Develop: vmgabriel

# Libraries
from datetime import datetime
from typing import List, Any

# My Libraries
from src.utils.validations.validation_handler import Validate_Handler

# Domains
from src.domain.models.validation_interface import Validate_Interface

# Structures
from src.counter_one_hour.domain.measure_one_hour import MeasureOneHour


class MeasureOneHourValidate(Validate_Interface[MeasureOneHour]):
    """Validation for Input of Measure in One Hour"""
    def __init__(self):
        self._v = Validate_Handler()
        self.not_verify = lambda x: True

    @staticmethod
    def validate_object(data: Any) -> (str, MeasureOneHour):
        """Validation of Object Complete"""
        # pylint: disable=invalid-name
        datas = []
        datas.append(data['_id'] if ('_id' in data) else None)
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(data['min'] if ('min' in data) else 0.0)
        datas.append(data['max'] if ('max' in data) else 0.0)
        datas.append(data['counter'] if ('counter' in data) else 0)
        datas.append(data['gr1'] if ('gr1' in data) else 0.0)
        datas.append(data['gr2'] if ('gr2' in data) else 0.0)
        datas.append(data['gr3'] if ('gr3' in data) else 0.0)
        datas.append(data['gr4'] if ('gr4' in data) else 0.0)
        datas.append(data['idReader'] if ('idReader' in data) else None)
        datas.append(data['nameReader'] if ('nameReader' in data) else None)
        datas.append(
            data['idController'] if ('idController' in data) else None
        )
        datas.append(
            data['nameController'] if ('nameController' in data) else None
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )

        return ('done correctly', MeasureOneHour(*tuple(datas)))

    @staticmethod
    def validate_object_update(data: Any) -> (str, MeasureOneHour):
        """Validate Object Update"""
        # pylint: disable=invalid-name
        datas = []
        datas.append(data['_id'] if ('_id' in data) else None)
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(data['min'] if ('min' in data) else 0.0)
        datas.append(data['max'] if ('max' in data) else 0.0)
        datas.append(data['counter'] if ('counter' in data) else 0)
        datas.append(data['gr1'] if ('gr1' in data) else 0.0)
        datas.append(data['gr2'] if ('gr2' in data) else 0.0)
        datas.append(data['gr3'] if ('gr3' in data) else 0.0)
        datas.append(data['gr4'] if ('gr4' in data) else 0.0)
        datas.append(data['idReader'] if ('idReader' in data) else None)
        datas.append(data['nameReader'] if ('nameReader' in data) else None)
        datas.append(
            data['idController'] if ('idController' in data) else None
        )
        datas.append(
            data['nameController'] if ('nameController' in data) else None
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )
        datas.append(
            data['tookTime'] if ('tookTime' in data) else datetime.now()
        )

        return ('done correctly', MeasureOneHour(*tuple(datas)))

    def data_filter_content(self, limit: int, offset: int) -> str:
        """Validate Filter content Data"""
        return self._v.data_filter_content(limit, offset)

    def data_order_content(self, order: List[str]) -> bool:
        """Data order Content"""
        return self._v_base.data_order_content(order)
