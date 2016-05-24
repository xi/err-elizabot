import eliza
from errbot import botcmd, BotPlugin


class ElizaBot(BotPlugin):
    @botcmd
    def eliza(self, _, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return eliza.respond(args)
