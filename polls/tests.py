# api_kassa = '2e574c37168046cc75c47666d7d878dc'
# secret_one = 'TKLTf3c+?7*8=]4'
# secret_two = '.t0nFJlrd!D2VAz'
#token_viber = '4df31bb7e3e7e775-3ab72da0bcb99231-e172281618acc1dc
# from freekassa import FreeKassaApi
#
# client = FreeKassaApi(
#     first_secret='TKLTf3c+?7*8=]4',
#     second_secret='.t0nFJlrd!D2VAz',
#     merchant_id='1',
#     wallet_id='4201')
#
#
# payment_link = client.generate_payment_link(4201, 150)
#
# print(payment_link)
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
#
bot_configuration = BotConfiguration(
	name='test123454sad',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4df31bb7e3e7e775-3ab72da0bcb99231-e172281618acc1dc'
)
viber = Api(bot_configuration)
# viber_request = viber.parse_request(requests.get_data())
# viber.send_messages(to=viber_requests.get_sender().get_id(), messages=[TextMessage(text='как дела ?')])
from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)
from viberbot.api.messages.data_types.contact import Contact

# creation of text message
text_message = TextMessage(text="sample text message!")

# creation of contact message
contact = Contact(phone_number="0682325298")
contact_message = ContactMessage(contact=contact)

viber.send_messages(to=contact, messages=[TextMessage(text='как дела ?')])