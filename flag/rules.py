from configuration import FLAG_DESTROYER
from widgets.message import MessageBox
from all_flag import Flag


def Rules(rule):

    if rule == "camp_on_notile" or rule == 1:
        Flag.FLAG_RULE_01 = True if FLAG_DESTROYER else False
        message = MessageBox()
        message.lab.text = "You can't place that in here."
        return message
    elif rule == "not_enough_energy" or rule == 2:
        Flag.FLAG_RULE_02 = True if FLAG_DESTROYER else False
        message = MessageBox()
        message.lab.text = "Unsufficient Energy."
        return message
    return MessageBox()
