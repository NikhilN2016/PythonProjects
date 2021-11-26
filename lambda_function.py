# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
StatesCapitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson city', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Colombus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

class IllinoisIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("IllinoisIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Illinois is Springfield"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class AlabamaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AlabamaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Alabama is Montgomery"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class AlaskaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AlaskaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Alaska is Juneau"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class ArizonaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ArizonaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Arizona is Phoenix"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class ArkansasIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ArkansasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Arkansas is little rock"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class CaliforniaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaliforniaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of California is Sacramento"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class ColoradoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ColoradoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Colorado is Denver"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class IndianaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("IndianaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Indiana is Indianapolis"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class ConnecticutIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ConnecticutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Connecticut is Hartford"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class IdahoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("IdahoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Idaho is Boise"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class DelawareIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DelawareIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Delaware is Dover"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class FloridaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FloridaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Florida is Tallahassee"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class GeorgiaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GeorgiaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Georgia is Atlanta"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )
class HawaiiIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HawaiiIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Hawaii is Honolulu"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class IowaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("IowaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Iowa is Des Moines"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class KansasIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KansasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Kansas is Topeka"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class KentuckyIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("KentuckyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Kentucky is Frankfort"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class LouisianaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LouisianaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Louisiana is Baton Rouge"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MaineIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MaineIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Maine is Augusta"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MarylandIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MarylandIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Maryland is Annapolis"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MassachusettsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MassachusettsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Massachusetts is Boston"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MichiganIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MichiganIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Michigan is Lansing"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MinnesotaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MinnesotaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Minnesota is St. Paul"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MississippiIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MississippiIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Mississippi is Jackson"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MissouriIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MissouriIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Missouri is Jefferson City"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class MontanaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MontanaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Montana is Helena"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NebraskaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NebraskaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Nebraska is Lincoln"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NevadaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NevadaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Nevada is Carson City"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NewHampshireIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NewHampshireIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of New Hampshire is Concord"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NewJerseyIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NewJerseyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of New Jersey is Trenton"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NewMexicoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NewMexicoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of New Mexico is Santa Fe"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NewYorkIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NewYorkIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of New York is Albany"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NorthCarolinaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NorthCarolinaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of North Carolina is Raleigh"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class NorthDakotaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NorthDakotaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of North Dakota is Bismarck"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class OhioIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OhioIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Ohio is Columbus"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class OklahomaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OklahomaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Oklahoma is Oklahoma City"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class OregonIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OregonIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Oregon is Salem"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class PennsylvaniaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PennsylvaniaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Pennsylvania is Harrisburg"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class RhodeIslandIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RhodeIslandIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Rhode Island is Providence"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class SouthCarolinaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SouthCarolinaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of South Carolina is Columbia"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class SouthDakotaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SouthDakotaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of South Dakota is Pierre"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class TennesseeIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TennesseeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Tennessee is Nashville"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class TexasIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TexasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Texas is Austin"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class UtahIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("UtahIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Utah is Salt Lake City"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class VermontIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VermontIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Vermont is Montpelier"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class VirginiaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VirginiaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Virginia is Richmond"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class WashingtonIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WashingtonIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Washington is Olympia"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class WestVirginiaIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WestVirginiaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of West Virginia is Charleston"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class WisconsinIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WisconsinIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Wisconsin is Madison"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class WyomingIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WyomingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The capital of Wyoming is Cheyenne"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Say 'I want to find the capital of [desired state]' to find capital of your desired state"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )





class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What other state and capital would you like to find?")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IllinoisIntentHandler())
sb.add_request_handler(AlabamaIntentHandler())
sb.add_request_handler(AlaskaIntentHandler())
sb.add_request_handler(ArizonaIntentHandler())
sb.add_request_handler(ArkansasIntentHandler())
sb.add_request_handler(CaliforniaIntentHandler())
sb.add_request_handler(ColoradoIntentHandler())
sb.add_request_handler(IndianaIntentHandler())
sb.add_request_handler(ConnecticutIntentHandler())
sb.add_request_handler(IdahoIntentHandler())
sb.add_request_handler(DelawareIntentHandler())
sb.add_request_handler(FloridaIntentHandler())
sb.add_request_handler(GeorgiaIntentHandler())
sb.add_request_handler(HawaiiIntentHandler())
sb.add_request_handler(IowaIntentHandler())
sb.add_request_handler(KansasIntentHandler())
sb.add_request_handler(KentuckyIntentHandler())
sb.add_request_handler(LouisianaIntentHandler())
sb.add_request_handler(MarylandIntentHandler())
sb.add_request_handler(MassachusettsIntentHandler())
sb.add_request_handler(MichiganIntentHandler())
sb.add_request_handler(MinnesotaIntentHandler())
sb.add_request_handler(MississippiIntentHandler())
sb.add_request_handler(MissouriIntentHandler())
sb.add_request_handler(MontanaIntentHandler())
sb.add_request_handler(NebraskaIntentHandler())
sb.add_request_handler(NevadaIntentHandler())
sb.add_request_handler(NewHampshireIntentHandler())
sb.add_request_handler(NewJerseyIntentHandler())
sb.add_request_handler(NewMexicoIntentHandler())
sb.add_request_handler(NewYorkIntentHandler())
sb.add_request_handler(NorthCarolinaIntentHandler())
sb.add_request_handler(NorthDakotaIntentHandler())
sb.add_request_handler(OhioIntentHandler())
sb.add_request_handler(OklahomaIntentHandler())
sb.add_request_handler(OregonIntentHandler())
sb.add_request_handler(PennsylvaniaIntentHandler())
sb.add_request_handler(RhodeIslandIntentHandler())
sb.add_request_handler(SouthCarolinaIntentHandler())
sb.add_request_handler(SouthDakotaIntentHandler())
sb.add_request_handler(TennesseeIntentHandler())
sb.add_request_handler(TexasIntentHandler())
sb.add_request_handler(UtahIntentHandler())
sb.add_request_handler(VermontIntentHandler())
sb.add_request_handler(VirginiaIntentHandler())
sb.add_request_handler(WashingtonIntentHandler())
sb.add_request_handler(WestVirginiaIntentHandler())
sb.add_request_handler(WisconsinIntentHandler())
sb.add_request_handler(WyomingIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()