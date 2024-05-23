# 设备类型映射
type_map = {
    "SWITCH": {
        "1-002": "On",
        "1-003": "On",
        "1-005": "On",
        "1-006": "On",
    },
    "LIGHT": {
        "1-001": "On",
        "1-004": "On",
        "3-001": "Dim",
        "3-002": "Temp",
        "3-003": "DimTemp",
        "3-004": "RGBW",
        "3-005": "RGB",
        "3-006": "RGBCW",
    },
    "COVER": {
        "4-001": "Roll",
        "4-002": "Roll",
        "4-003": "Shutter",
        "4-004": "Shutter",
    },
    # "CLIMATE": {
    #     "5-001": "HeatCool",
    #     "5-002": "Underfloor",
    #     "5-003": "Ventilation",
    #     "5-004": "HeatPump",
    #     "5-005": "Combo",
    # },
    # "BINARY_SENSOR": {
    #     "7-008-001": "Human",
    #     "7-008-002": "Human",
    #     "7-008-003": "Human",
    # },
    # "SENSOR": {
    #     "7-001-001": "temperature",
    #     "7-002-001": "humidity",
    #     "7-003-001": "light",
    #     "7-011-001": "volatileOrganicCompounds",
    #     "7-005-001": "pm25",
    #     "7-006-001": "carbonDioxide",
    #     "7-010-001": "carbonMonoxide",
    # }
}

group_type_map = {
    "SWITCH": {
        "Breaker": "On",
    },
    "LIGHT": {
        "Light": "Dim",
        "Color": "Temp",
        "LightColor": "DimTemp",
        "RGBW": "RGBW",
        "RGB": "RGB",
    },
    "COVER": {
        "Retractable": "Roll",
        "Roller": "Roll",
    },
}
