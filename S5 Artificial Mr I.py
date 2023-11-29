#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:35:08 2023

@author: ASUS
"""

from opentrons import protocol_api
from opentrons import simulate

requirements = {'robotType': 'Flex', 'apiLevel': '2.15'}

metadata = {
    'apiLevel': '2.15',
    "author": "Warren <whh120@ic.ac.uk>",
    'protocolName': 'iGEM serial dilution tutorial',
    'description': 'protocol for serial dilution for the iGEM dye calibration'
}

def run(protocol: protocol_api.ProtocolContext):
    # define labware
    tiprack = protocol.load_labware(
        "opentrons_96_tiprack_300ul", location="1")
    reservoir = protocol.load_labware(
        "4ti0131_12_reservoir_21000ul", location="2")
    plate = protocol.load_labware(
        "costar3370flatbottomtransparent_96_wellplate_200ul", location="3")  

    # pipettes
    left_pipette = protocol.load_instrument(
        "p300_multi_gen2", mount="left", tip_racks=[tiprack])
    
    # PBS loading
    left_pipette.pick_up_tip()
    row = plate.row()[0]
    left_pipette.transfer(100, reservoir['A1'], row[1:])
    left_pipette.drop_tip()
    
    # Fluorescein loading + SD
    left_pipette.pick_up_tip()
    left_pipette.transfer(200, reservoir['A2'], row[0], mix_after=(3,50))
    left_pipette.transfer(100, row[:10], row[1:11], mix_after=(3,50), blow_out = True)
    left_pipette.aspirate(100, row[10]) 
    left_pipette.drop_tip()
