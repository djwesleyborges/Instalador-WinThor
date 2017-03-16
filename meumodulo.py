import platform

class Modulo(object):

    def __init__(self):
        self._instancia = ""
        self._adminInstancia = ""
        self._senhaOracle = ""
        self._senhaDMP = ""
        self._usuarioASerCriado = ""
        self._senhaASerCriada = ""
        self._diretorioWinthor = ""
        self._diretorioDMP = ""
        self._ajustarCodcli = ""
        self._hostname = platform.node()


    # hostname
    @property
    def hostname(self):
        # Do something if you want
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        # Do something if you want
        self._hostname = value

    # instancia
    @property
    def instancia(self):
        # Do something if you want
        return self._instancia

    @instancia.setter
    def instancia(self, value):
        # Do something if you want
        self._instancia = value

    # _adminInstancia
    @property
    def adminInstancia(cls):
        return cls._adminInstancia

    @adminInstancia.setter
    def adminInstancia(cls, value):
        cls._adminInstancia = value

    # _senhaOracle
    @property
    def senhaOracle(cls):
        return cls._senhaOracle

    @senhaOracle.setter
    def senhaOracle(cls, value):
        cls._senhaOracle = value

    # _senhaDMP
    @property
    def senhaDMP(cls):
        return cls._senhaDMP

    @senhaDMP.setter
    def senhaDMP(cls, value):
        cls._senhaDMP = value

    # _usuarioASerCriado
    @property
    def usuarioASerCriado(cls):
        return cls._usuarioASerCriado

    @usuarioASerCriado.setter
    def usuarioASerCriado(cls, value):
        cls._usuarioASerCriado = value


    # _senhaASerCriada
    @property
    def senhaASerCriada(cls):
        return cls._senhaASerCriada

    @senhaASerCriada.setter
    def senhaASerCriada(cls, value):
        cls._senhaASerCriada = value


    # diretorioWinthor
    @property
    def diretorioWinthor(cls):
        return cls._diretorioWinthor

    @diretorioWinthor.setter
    def diretorioWinthor(cls, value):
        cls._diretorioWinthor = value


    # diretorioDMP
    @property
    def diretorioDMP(cls):
        return cls._diretorioDMP

    @diretorioDMP.setter
    def diretorioDMP(cls, value):
        cls._diretorioDMP = value


    # ajustarCodcli
    @property
    def ajustarCodcli(cls):
        return cls._ajustarCodcli

    @ajustarCodcli.setter
    def ajustarCodcli(cls, value):
        cls._ajustarCodcli = value