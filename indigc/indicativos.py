from typing import List


class GCI:
    def __init__(self):
        self.dados_globais = {
            'AFEGANISTAO': 93,
            'AFRICA DO SUL': 27,
            'ALASKA': 1907,
            'ALBANIA': 355,
            'ALEMANHA': 49,
            'ANDORRA': 376,
            'ANGOLA': 244,
            'ANGUILLA': 1264,
            'ANTIGUA-BARBUDA': 1268,
            'ANTILHAS HOLANDESAS': 599,
            'ARABIA SAUDITA': 966,
            'ARGELIA': 213,
            'ARGENTINA': 54,
            'ARMENIA': 374,
            'ARUBA': 297,
            'ASCENSAO': 247,
            'AUSTRALIA': 61,
            'AUSTRIA': 43,
            'AZERBAIJAO': 994,
            'BAHAMAS': 1242,
            'BAHREIN': 973,
            'BANGLADESH': 880,
            'BARBADOS': 1246,
            'BELGICA': 32,
            'BELIZE': 501,
            'BENIN': 229,
            'BERMUDA': 1441,
            'BIELORUSSIA': 375,
            'BOLIVIA': 591,
            'BOSNIA-HERZEGOVINA': 387,
            'BOTSWANA': 267,
            'BRASIL': 55,
            'BRUNEI': 673,
            'BULGARIA': 359,
            'BURKINA FASO': 226,
            'BURUNDI': 257,
            'BUTAO': 975,
            'CABO VERDE': 238,
            'CAMAROES': 237,
            'CAMBOJA': 855,
            'CANADA': 1,
            'CARRIACOU': 1473,
            'CAYMAN': 1345,
            'CAZAQUISTAO': 7,
            'CHADE': 235,
            'CHILE': 56,
            'CHINA': 86,
            'CHIPRE': 357,
            'COLOMBIA': 57,
            'COMORES': 269,
            'CONGO': 242,
            'COOK': 682,
            'COREIA (REP. DEM.)': 850,
            'COREIA DO SUL': 82,
            'COSTA DO MARFIM': 225,
            'COSTA RICA': 506,
            'CROACIA': 385,
            'CUBA': 53,
            'DIEGO GARCIA': 246,
            'DIJIBUTI': 253,
            'DINAMARCA': 45,
            'DOMINICA': 1767,
            'EL SALVADOR': 503,
            'EGIPTO': 20,
            'EMIRADOS ARAB. UNIDOS': 971,
            'EQUADOR': 593,
            'ERITREIA': 291,
            'ESLOVAQUIA': 421,
            'ESLOVENIA': 386,
            'ESPANHA': 34,
            'ESTADOS UNIDOS AMERICA': 1,
            'ESTONIA': 372,
            'ETIOPIA': 251,
            'FEROE (ILHAS)': 298,
            'FIJI': 679,
            'FILIPINAS': 63,
            'FINLANDIA': 358,
            'FORMOSA (TAIWAN)': 886,
            'FRANCA': 33,
            'GABAO': 241,
            'GAMBIA': 220,
            'GANA': 233,
            'GEORGIA': 995,
            'GIBRALTAR': 350,
            'GRANADA': 1473,
            'GRECIA': 30,
            'GRONELANDIA': 299,
            'GUADALUPE': 590,
            'GUAM': 1671,
            'GUATEMALA': 502,
            'GUIANA': 592,
            'GUIANA FRANCESA': 594,
            'GUINE-BISSAU': 245,
            'GUINE-CONACRI': 224,
            'GUINE EQUATORIAL': 240,
            'HAITI': 509,
            'HAWAI': 1808,
            'HOLANDA': 31,
            'HONDURAS': 504,
            'HONG KONG': 852,
            'HUNGRIA': 36,
            'IEMEN (REP. ARABE)': 967,
            'INDIA': 91,
            'INDONESIA': 62,
            'IRAO': 98,
            'IRAQUE': 964,
            'IRLANDA': 353,
            'IRLANDA DO NORTE': 44,
            'ISLANDIA': 354,
            'ISRAEL': 972,
            'ITALIA': 39,
            'JAMAICA': 1876,
            'JAPAO': 81,
            'KOWEIT': 965,
            'LAOS': 856,
            'LESOTO': 266,
            'LETONIA': 371,
            'LIBANO': 961,
            'LIBERIA': 231,
            'LIBIA': 218,
            'LIECHTENSTEIN': 423,
            'LITUANIA': 370,
            'LUXEMBURGO': 352,
            'MACAU': 853,
            'MACEDONIA': 389,
            'MADAGASCAR': 261,
            'MALASIA': 60,
            'MALAWI': 265,
            'MALDIVAS': 960,
            'MALI': 223,
            'MALTA': 356,
            'MALVINAS-FALKLAND': 500,
            'MARROCOS': 212,
            'MARSHALL (ILHAS)': 692,
            'MARTINICA': 596,
            'MAURICIAS': 230,
            'MAURITANIA': 222,
            'MAYOTTE': 269,
            'MEXICO': 52,
            'MICRONESIA': 691,
            'MOCAMBIQUE': 258,
            'MOLDAVIA': 373,
            'MONACO': 377,
            'MONGOLIA': 976,
            'MONTSERRAT': 1664,
            'MYANMAR (BIRMANIA)': 95,
            'NAMIBIA': 264,
            'NAURU': 674,
            'NEPAL': 977,
            'NEVIS': 1869,
            'NICARAGUA': 505,
            'NIGER': 227,
            'NIGERIA': 234,
            'NIUE': 683,
            'NORFOLK': 672,
            'NORUEGA': 47,
            'NOVA NALEDONIA': 687,
            'NOVA ZELANDIA': 64,
            'OMA': 968,
            'PALAU': 680,
            'PALESTINA': 970,
            'PANAMA': 507,
            'PAPUA E NOVA GUINE': 675,
            'PAQUISTAO': 92,
            'PARAGUAI': 595,
            'PERU': 51,
            'PITCAIRN': 672,
            'POLINESIA FRANCESA': 689,
            'POLONIA': 48,
            'PORTO RICO': (1787, 1939),
            'QATAR': 974,
            'QUENIA': 254,
            'QUIRGUISTAO': 996,
            'QUIRIBATI': 686,
            'REINO UNIDO': 44,
            'REP. CENTRO AFRICANA': 236,
            'REPUBLICA CHECA': 420,
            'REP. DEM. CONGO (ZAIRE)': 243,
            'REP. DOMINICANA': 1809,
            'REUNIAO': 262,
            'ROMENIA': 40,
            'RUANDA': 250,
            'RUSSIA': 7,
            'S. CRISTOPHE': 1869,
            'S. CROIX': 1340,
            'S. HELENA': 290,
            'S. JOHN': 1340,
            'S. KITTS': 1869,
            'S. LUCIA': 1758,
            'S. MARINO': 378,
            'S. PIERRE E MIQUELON': 508,
            'S. THOMAS': 1340,
            'S. TOME E PRINCIPE': 239,
            'S. VICENTE E GRENADINES': 1784,
            'SAIPAN (ILHAS MARIANAS)': 1670,
            'SALOMAO': 677,
            'SAMOA AMERICANA': 684,
            'SAMOA OCIDENTAL': 685,
            'SEICHELES': 248,
            'SENEGAL': 221,
            'SERRA LEOA': 232,
            'SERVIA E MONTENEGRO': 381,
            'SINGAPURA': 65,
            'SIRIA': 963,
            'SOMALIA': 252,
            'SRI LANKA': 94,
            'SUAZILANDIA': 268,
            'SUDAO': 249,
            'SUECIA': 46,
            'SUICA': 41,
            'SURINAME': 597,
            'TAILANDIA': 66,
            'TAJIQUISTAO': 992,
            'TANZANIA': 255,
            'TIMOR LOROSAE': 670,
            'TOBAGO': 1868,
            'TOGO': 228,
            'TOKELAU': 690,
            'TONGA': 676,
            'TORTOLA': 1284,
            'TRINDADE': 1868,
            'TRISTAO DA CUNHA': 290,
            'TUNISIA': 216,
            'TURKS E CAICOS': 1649,
            'TURQUEMENISTAO': 993,
            'TURQUIA': 90,
            'TUVALU': 688,
            'UCRANIA': 380,
            'UGANDA': 256,
            'URUGUAI': 598,
            'USBEQUISTAO': 998,
            'VANUATU': 678,
            'VATICANO': 39,
            'VENEZUELA': 58,
            'VIETNAME': 84,
            'VIRGENS AMERICANAS': 1340,
            'VIRGENS BRITANICAS': 1284,
            'WALLIS E FUTUNA': 681,
            'ZAMBIA': 260,
            'ZIMBABWE': 263
        }

    def paises(self) -> List:
        paises = []
        for pais in self.dados_globais:
            paises.append(pais)
        return paises

    def indicativos(self) -> List:
        indicativos = []
        for pais in self.paises():
            indicativo = self.dados_globais[pais]
            indicativos.append(indicativo)
        return indicativos

    def indicativo_especifico(self, _pais: str) -> str:
        try:
            return self.dados_globais[_pais]
        except KeyError:
            return f"nenhum indicativo correspondente a {_pais}, " \
                   f"certifique-se de escrever correctamente o nome do pais!"
