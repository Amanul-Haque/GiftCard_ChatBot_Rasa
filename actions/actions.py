# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
#
class SendGiftCard(Action):

     def name(self) -> Text:
         return "send_gift_card"

     def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            site = tracker.get_slot("site"),
            to_mail = tracker.get_slot("email")
            amount = tracker.get_slot("amount")
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("sendergiftcard@gmail.com", "gift@123")
            message = "Your gift card code for {} of Rs. {} is ZXCV-1234-ASDF".format(site,amount)
            s.sendmail("sendergiftcard@gmail.com", to_mail, message)
            s.quit()

#            return []
