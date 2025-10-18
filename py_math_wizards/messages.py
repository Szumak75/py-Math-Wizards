"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Messages module for success and failure responses.
"""

import codecs
from typing import List

from jsktoolbox.attribtool import NoNewAttributes


class Messages(NoNewAttributes):
    """Container for success and failure messages."""

    # Success messages (ROT13 encoded)
    _SUCCESS: List[str] = [
        "Rkpryyrag wbo!",
        "Tbbq nafjre.",
        "Lbh'er nofbyhgryl evtug.",
        "Gung'f vg!",
        "Cresrpg!",
        "Terng jbex!",
        "Rknpgyl!",
        "Lbh'ir anvyrq vg.",
        "Fcbg ba.",
        "Gung'f pbeerpg.",
        "Jryy qbar.",
        "Snagnfgvp!",
        "Oevyyvnag!",
        "Lbh tbg vg.",
        "Gung'f gur jnl.",
        "Fhcreo.",
        "Bhgfgnaqvat.",
        "Cerpvfryl.",
        "Lbh'er n fgne!",
        "Gbc-abgpu.",
        "Jbaqreshy!",
        "Zneiryybhf!",
        "Lbh'er qbvat terng.",
        "Xrrc vg hc!",
        "Gung'f ernyyl vzcerffvir.",
        "Svefg-pynff jbex.",
        "Lbh'er ba gur evtug genpx.",
        "Gung'f n terng bofre‌ingvba.",
        "Lbhe jbex vf rkprcgvbany.",
        "V'z vzcerffrq.",
        "Lbh'ir znqr zl qnl.",
        "Gung'f fbzr uvtu-dhnyvgl jbex.",
        "Lbh'er n angheny.",
        "Lbh'er n travhf.",
        "Gung'f gur gvpxrg.",
        "Lbh'ir tbg n terng unaqyr ba guvf.",
        "Gung'f na rkpryyrag cbvag.",
        "Lbh'ir rkprrqrq rkcrpgngvbaf.",
        "N+ jbex.",
        "Lbh'er n gehr cebsrffvbany.",
        "Gung'f ubj vg'f qbar.",
        "Lbh'er n dhvpx yrneare.",
        "Lbh'er irel creprcgvir.",
        "Gung'f n pyrire fbyhgvba.",
        "Lbh'er znxvat terng cebterfff.",
        "Lbhe rssbegf ner cnlvat bss.",
        "Gung'f n znfgrecvrpr.",
        "Lbh'er n juvmm.",
        "Gung'f svefg-engr.",
        "Lbh'er ba sver!",
        "Lbh'er hafgbcnoyr.",
        "Gung'f gur fcvevg.",
        "Lbh'er n yrtraq.",
        "Gung'f jbeyq-pynff.",
        "Lbh'er n punzcvba.",
        "Gung'f rkrzcynel.",
        "Lbh'er n iveghbfb.",
        "Gung'f synjayrff.",
        "Lbh'er n znrfgeb.",
        "Gung'f vzcpppnoyr.",
        "Lbh'er n cebqvtl.",
        "Gung'f znfgreshy.",
        "Lbh'er n frafngvba.",
        "Gung'f fgryyne.",
        "Lbh'er n curabzraba.",
        "Gung'f fhoyvzr.",
        "Lbh'er n zneiyr.",
        "Gung'f genafpraqrag.",
        "Lbh'er n eriryngvba.",
        "Gung'f qvivnr.",
        "Lbh'er n zvenpr jbexre.",
        "Gung'f urnirayl.",
        "Lbh'er n gernfher.",
        "Gung'f tybevbhf.",
        "Lbh'er n tvsg.",
        "Gung'f zntavsvprag.",
        "Lbh'er n oyrffvat.",
        "Gung'f znwrfgvp.",
        "Lbh'er n qernz pbzr gehr.",
        "Gung'f rcvp.",
    ]

    # Failure messages (ROT13 encoded)
    _FAILURE: List[str] = [
        "Gung'f abg dhvgr evtug.",
        "Gurer frrzf gb or n zvfgnxr urer.",
        "Guvf nafjre vf vapbeerpg.",
        "Yrg'f gel ntnva.",
        "Abg dhvgr, gel bar zber gvzr.",
        "Bbbcf! Gung'f abg vg.",
        "Avpr gel, ohg abg pbeerpg.",
        "Fbeel, gung'f jebat.",
        "Guvax ntnva, cyrnfr.",
        "Gung'f abg gur nafjre jr'er ybbxvat sbe.",
        "Pyrfr, ohg ab pvtne.",
        "Gel ntnva, lbh'er nyzbfg gurer!",
        "Abg guvf gvzr.",
        "Xrrc gelvat!",
        "Qba'g jbeel, gel ntnva.",
        "Gung'f abg vg, gel bar zber gvzr.",
        "Fb pybfr! Gel ntnva.",
        "Abg dhvgr, ohg xrrc tbvat!",
        "Gung'f vapbeerpg, gel ntnva.",
        "Avpr rssbeg, ohg gel ntnva.",
    ]

    def __init__(self) -> None:
        """Initialize Messages."""
        pass

    @classmethod
    def get_success_message(cls) -> str:
        """Get a random success message.

        ### Returns:
        str - A decoded success message.
        """
        import random

        encoded = random.choice(cls._SUCCESS)
        return codecs.decode(encoded, "rot13")

    @classmethod
    def get_failure_message(cls) -> str:
        """Get a random failure message.

        ### Returns:
        str - A decoded failure message.
        """
        import random

        encoded = random.choice(cls._FAILURE)
        return codecs.decode(encoded, "rot13")
