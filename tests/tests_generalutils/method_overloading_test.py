import logging
import sys

logger = logging.getLogger(__name__)

#pip install multidispatch==0.2
from multidispatch import multimethod
from alexber.utils.importer import importer


class Engine(object):


    @multimethod(object)
    def _set_playerA(self, player):
        logging.debug('instance')
        pass

    @_set_playerA.dispatch(str)
    def _(self, st):
        logging.debug('str')
        player_cls = importer(st)
        player = player_cls()
        player.say()
        pass

    #alternative (recent) syntax
    # @_set_playerA.dispatch
    # def _(self, st: str):
    #     print('str')
    #     player_cls = importer(st)
    #     player = player_cls()
    #     player.say()
    #     pass


    playerA = property(fset=_set_playerA)


class Player(object):
    def say(self):
        logging.debug('hello')

def test_overloading_object(request, mocker):
    logger.info(f'{request._pyfuncitem.name}()')
    namespace = sys.modules[__name__]

    importer = mocker.spy(namespace, 'importer')
    engine = Engine()
    input = Player()
    engine.playerA= input

    assert namespace.importer == importer
    assert importer.call_count ==0, "Engine.playerA(str) was called, when Engine.playerA(object) was expected"
                                                            # #we shouldn't use  importer when we have explicit object."
    logger.info(dir(importer))


def test_overloading_str(request, mocker):
    logger.info(f'{request._pyfuncitem.name}()')
    namespace = sys.modules[__name__]

    importer = mocker.spy(namespace, 'importer')
    engine = Engine()
    input = '.'.join([__name__, 'Player'])
    engine.playerA = input

    assert namespace.importer == importer
    importer.assert_called_once_with(input)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])