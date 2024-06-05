# device_type
type_map = {
    "switch": {
        "1-002": "on",
        "1-003": "on",
        "1-005": "on",
        "1-006": "on",
        "107-001": "on",
    },
    "light": {
        "1-001": "on",
        "1-004": "on",
        "3-001": "dim",
        "3-002": "temp",
        "3-003": "dim_temp",
        "3-004": "rgbw",
        "3-005": "rgb",
        "3-006": "rgbcw",
    },
    "cover": {
        "4-001": "roll",
        "4-002": "roll",
        "4-003": "shutter",
        "4-004": "shutter",
    },
}

group_type_map = {
    "switch": {
        "breaker": "on",
    },
    "light": {
        "light": "dim",
        "color": "temp",
        "lightcolor": "dim_temp",
        "rgbw": "rgbw",
        "rgb": "rGB",
    },
    "cover": {
        "retractable": "roll",
        "roller": "roll",
    },
}


media_type_map = {
    "8-001-001": "hua_ersi_music",
    "8-001-002": "xiang_wang_music_s7_mini_3s",
    "8-001-003": "xiang_wang_music_s8",
    "8-001-004": "sheng_bi_ke_music",
    "8-001-005": "bo_sheng_music",
    "8-001-006": "sonos_music",
}

sensor_type_map = {
    "7-001-001": ["temperature"],
    "7-002-001": ["humidity"],
    "7-003-001": ["light"],
    "7-004-001": ["formaldehyde"],
    "7-005-001": ["pm25"],
    "7-006-001": ["carbon_dioxide"],
    "7-007-001": ["air_quality"],
    "7-008-001": ["human"],
    "7-008-002": ["human"],
    "7-008-003": ["human", "light"],
    "7-009-001": ["trigger"],
    "7-009-002": ["human"],
    "7-009-003": ["human", "light"],
    "7-009-004": ["trigger"],
    "7-009-005": ["trigger"],
    "7-009-006": ["trigger"],
    "7-009-007": ["trigger"],
    "7-009-008": ["trigger"],
    "7-009-009": ["human"],
    "7-009-010": ["human"],
    "7-010-001": ["carbon_monoxide"],
    "7-011-001": ["tvoc"],
    "7-012-001": ["temperature", "humidity", "tvoc", "pm25", "formaldehyde", "carbon_dioxide", "pm10"],
    "7-012-002": ["carbon_monoxide"],
    "7-013-001": ["light", "human"],
}
