from cherrypy.lib import sessions
from model.athlete import Athlete
import temporaryUser

class CQRamSession(sessions.RamSession):
    def clean_up(self):
        now = self.now()
        for id, (data, expiration_time) in self.cache.items():
            if expiration_time <= now:
                temporaryUser.expire(data.get('id'))
        super(CQRamSession, self).clean_up()

sessions.CqramSession = CQRamSession

