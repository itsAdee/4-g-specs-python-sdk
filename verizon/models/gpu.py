# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class GPU(object):

    """Implementation of the 'GPU' model.

    GPU resources of a service profile.

    Attributes:
        min_core_clock_m_hz (int): Minimum Core Clock value in megahertz.
        min_memory_clock_m_hz (int): Minimum Memory Clock value in megahertz.
        min_bandwidth_g_bs (int): Minimum GPU bandwidth in GB/s.
        min_tflops (int): Minimum Floating Point Operations Per Second in
            Teraflops.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "min_core_clock_m_hz": 'minCoreClockMHz',
        "min_memory_clock_m_hz": 'minMemoryClockMHz',
        "min_bandwidth_g_bs": 'minBandwidthGBs',
        "min_tflops": 'minTFLOPS'
    }

    _optionals = [
        'min_core_clock_m_hz',
        'min_memory_clock_m_hz',
        'min_bandwidth_g_bs',
        'min_tflops',
    ]

    def __init__(self,
                 min_core_clock_m_hz=APIHelper.SKIP,
                 min_memory_clock_m_hz=APIHelper.SKIP,
                 min_bandwidth_g_bs=APIHelper.SKIP,
                 min_tflops=APIHelper.SKIP):
        """Constructor for the GPU class"""

        # Initialize members of the class
        if min_core_clock_m_hz is not APIHelper.SKIP:
            self.min_core_clock_m_hz = min_core_clock_m_hz 
        if min_memory_clock_m_hz is not APIHelper.SKIP:
            self.min_memory_clock_m_hz = min_memory_clock_m_hz 
        if min_bandwidth_g_bs is not APIHelper.SKIP:
            self.min_bandwidth_g_bs = min_bandwidth_g_bs 
        if min_tflops is not APIHelper.SKIP:
            self.min_tflops = min_tflops 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        min_core_clock_m_hz = dictionary.get("minCoreClockMHz") if dictionary.get("minCoreClockMHz") else APIHelper.SKIP
        min_memory_clock_m_hz = dictionary.get("minMemoryClockMHz") if dictionary.get("minMemoryClockMHz") else APIHelper.SKIP
        min_bandwidth_g_bs = dictionary.get("minBandwidthGBs") if dictionary.get("minBandwidthGBs") else APIHelper.SKIP
        min_tflops = dictionary.get("minTFLOPS") if dictionary.get("minTFLOPS") else APIHelper.SKIP
        # Return an object of this model
        return cls(min_core_clock_m_hz,
                   min_memory_clock_m_hz,
                   min_bandwidth_g_bs,
                   min_tflops)