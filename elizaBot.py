from eliza import Eliza
from errbot import botcmd, BotPlugin


class ElizaBot(BotPlugin):
    eliza_daemon = Eliza()

    @botcmd
    def eliza(self, _, args):
        """ El'cheapo shrink for you """
        args = args.strip()
        return self.eliza_daemon.respond(args)
