import eliza
from errbot import BotPlugin


class ElizaBot(BotPlugin):
    def callback_message(self, msg):
        """El'cheapo shrink for you."""
        if msg.to == self.bot_identifier:
            self.send(msg.frm, eliza.respond(msg.body))
