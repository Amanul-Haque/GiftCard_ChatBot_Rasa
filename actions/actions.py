# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#from typing import Any, Text, Dict, List
#
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.forms import FormAction

#class ActionFormInfo(FormAction):
    #@staticmethod
    #def required_fields(tracker: Tracker) ->List[Text]:
        #return ["site" ,"amount" ,"mob_no"]
    #def name(self):
        #return 'action_take_info'
    #def submit(self,dispatcher,tracker,domain):
        #site = tracker.get_slot("site"),
        #mob_no = tracker.get_slot("mob_no")
        #amount = tracker.get_slot("amount")
        #dispatcher.utter_message("Your Gift card of Rupees")
        #dispatcher.utter_message(amount)
        #dispatcher.utter_message("from the website")
        #dispatcher.utter_message(site)
        #dispatcher.utter_message("Will be Delivered to you through Whatsapp on :")
        #dispatcher.utter_message(mob_no)
        #dispatcher.utter_message('Thankyou for shopping with us, Hope to see you soon!')