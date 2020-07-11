# Develop: vmgabriel
# Libraries
from typing import List, TypeVar, Generic, Any

# Domains
from domain.models.validation_interface import Validate_Interface
from utils.validations.validation_handler import Validate_Handler

from sensor_data.domain.sensor_data import SensorData

class SensorDataValidate(Validate_Interface[SensorData]):
    def __init__(self):
        self.v = Validate_Handler()
        self.not_verify = lambda x: True


    def validate_object(self, data: Any) -> (str, SensorData):
        _id = data['_id'] if ('_id' in data) else None
        tookTime = data['tookTime'] if ('tookTime' in data) else None
        gas = data['gas'] if ('gas' in data) else None
        carbon = data['carbon'] if ('carbon' in data) else None
        humedity = data['humedity'] if ('humedity' in data) else None
        temperature = data['temperature'] if ('temperature' in data) else None
        lightUV = data['lightUV'] if ('lightUV' in data) else None
        soilMoisture = data['soilMoisture'] if ('soilMoisture' in data) else None
        createdAt = data['createdAt'] if ('createdAt' in data) else None
        updatedAt = data['updatedAt'] if ('updatedAt' in data) else None
        deletedAt = data['deletedAt'] if ('deletedAt' in data) else None

        if not (self.not_verify(tookTime)):
            return('tookTime valid', {})
        if not (self.not_verify(gas)):
            return('gas not valid', {})
        if not (self.not_verify(carbon)):
            return('carbon not valid', {})
        if not (self.not_verify(humedity)):
            return('humedity not valid', {})
        if not (self.not_verify(temperature)):
            return('temperature not valid', {})
        if not (self.not_verify(lightUV)):
            return('lightUV not valid', {})
        if not (self.not_verify(soilMoisture)):
            return('soilMoisture not valid', {})
        if not (self.not_verify(createdAt)):
            return('created at not valid', {})
        if not (self.not_verify(updatedAt)):
            return('updated at not valid', {})

        return ('done correctly', SensorData(
            _id,
            tookTime,
            gas,
            carbon,
            humedity,
            temperature,
            lightUV,
            soilMoisture,
            createdAt,
            updatedAt,
            deletedAt
        ))

    def validate_object_update(self, data: Any) -> (str, SensorData):
        _id = data['_id'] if ('_id' in data) else None
        tookTime = data['tookTime'] if ('tookTime' in data) else None
        gas = data['gas'] if ('gas' in data) else None
        carbon = data['carbon'] if ('carbon' in data) else None
        humedity = data['humedity'] if ('humedity' in data) else None
        temperature = data['temperature'] if ('temperature' in data) else None
        lightUV = data['lightUV'] if ('lightUV' in data) else None
        soilMoisture = data['soilMoisture'] if ('soilMoisture' in data) else None
        createdAt = data['createdAt'] if ('createdAt' in data) else None
        updatedAt = data['updatedAt'] if ('updatedAt' in data) else None
        deletedAt = data['deletedAt'] if ('deletedAt' in data) else None

        if not (self.not_verify(tookTime)):
            return('tookTime valid', {})
        if not (self.not_verify(gas)):
            return('gas not valid', {})
        if not (self.not_verify(carbon)):
            return('carbon not valid', {})
        if not (self.not_verify(humedity)):
            return('humedity not valid', {})
        if not (self.not_verify(temperature)):
            return('temperature not valid', {})
        if not (self.not_verify(lightUV)):
            return('lightUV not valid', {})
        if not (self.not_verify(soilMoisture)):
            return('soilMoisture not valid', {})
        if not (self.not_verify(createdAt)):
            return('created at not valid', {})
        if not (self.not_verify(updatedAt)):
            return('updated at not valid', {})

        return ('done correctly', SensorData(
            _id,
            tookTime,
            gas,
            carbon,
            humedity,
            temperature,
            lightUV,
            soilMoisture,
            createdAt,
            updatedAt,
            deletedAt
        ))


    def data_filter_content(self, limit: int, offset: int) -> str:
        return self.validation_base.data_filter_content(limit, offset)

    def data_order_content(self, order: List[str]) -> bool:
        return self.validation_base.data_order_content(order)
