from verval.base import BaseVerval


class BaseVervalSp(BaseVerval):
    DOMAIN: str = "http://vervalsp.data.kemdikbud.go.id/"

    def __init__(self):
        super().__init__()

    @property
    def url_verval_index(self) -> str:
        return self.DOMAIN + "verval/index.php/"

    @property
    def url_perbaikan_identitas(self) -> str:
        return (
            self.url_verval_index
            + "cpengelolaan/pencarianperbaikandataidentitassekolah"
        )

    @property
    def url_perbaika_spasial(self) -> str:
        return self.url_verval_index + "cspasial/pencarianperbaikandataspasial"

    @property
    def url_perbaika_citra(self) -> str:
        return self.url_verval_index + "ccitra/pencarianperbaikandatacitra"

    @property
    def url_perbaika_citra_prasarana(self) -> str:
        return self.url_verval_index + "ccitra/pencarianperbaikandatacitraprasarana"
