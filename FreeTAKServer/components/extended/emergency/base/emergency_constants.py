import json
import pathlib
from string import Template

COMPONENT_NAME = "Emergency"

CONFIGURATION_FORMAT = "json"

CURRENT_COMPONENT_PATH = pathlib.Path(__file__).parent.parent.absolute()

CONFIGURATION_PATH_TEMPLATE = Template(
    str(
        pathlib.PurePath(
            CURRENT_COMPONENT_PATH, "configuration/model_definitions/$message_type"
        )
    )
    + f".{CONFIGURATION_FORMAT}"
)

LOGGING_CONFIGURATION_PATH = str(
    pathlib.PurePath(CURRENT_COMPONENT_PATH, "configuration/logging.conf")
)

ACTION_MAPPING_PATH = str(
    pathlib.PurePath(
        CURRENT_COMPONENT_PATH, "configuration/emergency_action_mapping.ini"
    )
)

INTERNAL_ACTION_MAPPING_PATH = str(
    pathlib.PurePath(
        CURRENT_COMPONENT_PATH, "configuration/internal_emergency_action_mapping.ini"
    )
)

TYPE_MAPPINGS = json.load(
    open(
        str(
            pathlib.PurePath(
                CURRENT_COMPONENT_PATH, "configuration/emergency_type_mapping.json"
            )
        ),
        "r",
        encoding="utf-8",
    )
)

BUSINESS_RULES_PATH = str(
    pathlib.PurePath(CURRENT_COMPONENT_PATH, "configuration/business_rules.json")
)

BASE_OBJECT_NAME = "Event"

EMERGENCY_OFF = "emergency_delete"

EMERGENCY_ALERT = "emergency_alert"
