from django.template.defaultfilters import stringfilter
from chat.models import Message
from django import template

register = template.Library()


@register.filter(name="decmsg")
@stringfilter
def decrypt_message(value):
    try:
        decrypted_message = Message.decrypt_text(value)
    except:
        # todo: inja emkan ijad bug hast. masalan 'value' yek message encrypt shode ya yek 'token' valid
        #  nabashe ya 'key' i ke 'value' bahash encrypt shode ba 'ENCRYPTION_KEY' fargh dashte bashe.
        #  In code bayad ba sharayet mokhtalef test beshe.
        decrypted_message = "Message is not available!"

    return decrypted_message
