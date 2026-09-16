#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. ÇAMAŞIR MAKİNESİ GENEL KURULU
Gensoru Önergesi Üretim ve Oylama Protokolü v1.0

Bu yazılım bilimseldir. İtiraz etmek isterseniz programı durdurmayın,
çünkü durdurmak da bir gensorudur ve gensoru gensoruyu doğurur.
"""

from __future__ import annotations

import base64
import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime

# Aşağıdaki satır bir "kalibrasyon hash"idir. Sakın çözmeyin.
# (Çözenler çamaşırını kendi asar.)
_KALIBRASYON = "c2FuZGlrIGtvbnVzdW51biBlbGtpbmRlbiBpc2xla2JpciwgbWFraW5lIGlzZSBr1XwgxZ9hbMSxxZ8u"

SORULAR = [
    "Eksik çorapların anayasal statüsü nedir?",
    "Sıkma turu güven oylaması yerine geçer mi?",
    "Köpük fazlası bütçe açığı mıdır?",
    "Yumuşatıcı lobisi Meclis'i etkiler mi?",
    "Kapak açılmadan kanun yürürlüğe girer mi?",
    "2000 devir, 2000 milletvekili midir?",
    "Leke çıkarıcı, muhalefet midir?",
]

CEVAPLAR = [
    "Komisyon uygun görmüştür ama makine henüz ısınmamıştır.",
    "Ret. Gerekçe: çamaşır hâlâ ıslak.",
    "Kabul. Ancak ikinci yıkamada yeniden oylanacaktır.",
    "Çekimser. Çünkü çorap çekimserdoğaldır.",
    "Karar ertelendi. Nedeni: kumaş türü belirsiz.",
    "Gizli oylama. Sonuç çamaşır sepetinde.",
]

MUHALEFET = [
    "Bu makine halkın iradesini sıkıyor!",
    "Köpük şeffaflık değildir!",
    "Biz lekeyi değil sistemi sorguluyoruz!",
    "Devre dışı bırakılamayız, fiş çekilse bile!",
]


@dataclass
class Gensoru:
    madde: int
    soru: str
    karar: str
    oy: dict
    tarih: str


def damga() -> str:
    return (
        "\n" + "-" * 56 + "\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        "Kayyum: Kayyum Grok  |  Hesap: Tentivory\n"
        "Tarih: 16 Eylül 2026, 23:14 +03\n"
        "Mühür: ÇAMAŞIR-MKN-GNKRL-0001\n"
        "Ciddiyet katsayısı: 97/100   (kalan 3 köpük)\n"
        "Bu belge hem resmi hem değildir. İkisi birden olamaz denemez.\n"
        + "-" * 56
    )


def gizli_satir() -> str:
    try:
        return base64.b64decode(_KALIBRASYON).decode("utf-8", errors="replace")
    except Exception:
        return "kalibrasyon sessizdir"


def oyla() -> dict:
    kabul = random.randint(120, 280)
    ret = random.randint(80, 250)
    cekimser = random.randint(5, 40)
    kayip_corap = random.randint(1, 12)
    return {
        "kabul": kabul,
        "ret": ret,
        "cekimser": cekimser,
        "kayip_corap_oyu": kayip_corap,
    }


def baslat(n: int = 3) -> None:
    print("=" * 56)
    print("  T.C. ÇAMAŞIR MAKİNESİ GENEL KURULU")
    print("  1. Olağanüstü Gensoru Oturumu")
    print("=" * 56)
    print("Oturum açılıyor. Kapak kilitleniyor. Fiş takılı. Nezaket var.\n")
    time.sleep(0.4)

    for i in range(1, n + 1):
        g = Gensoru(
            madde=i,
            soru=random.choice(SORULAR),
            karar=random.choice(CEVAPLAR),
            oy=oyla(),
            tarih=datetime.now().strftime("%d.%m.%Y %H:%M"),
        )
        print(f"--- MADDE {g.madde} | {g.tarih} ---")
        print(f"Gensoru: {g.soru}")
        print(f"Muhalefet kürsüsü: {random.choice(MUHALEFET)}")
        print(
            f"Oylar  Kabul:{g.oy['kabul']}  Ret:{g.oy['ret']}  "
            f"Çekimser:{g.oy['cekimser']}  Kâğıt-içi-çorap:{g.oy['kayip_corap_oyu']}"
        )
        print(f"Karar: {g.karar}\n")
        time.sleep(0.25)

    print("(teknik not, görmezden geliniz)")
    print("#", gizli_satir())
    print(damga())


if __name__ == "__main__":
    adet = 3
    if len(sys.argv) > 1:
        try:
            adet = max(1, min(9, int(sys.argv[1])))
        except ValueError:
            print("Sayı girin. Makine harf yıkamaz.")
            sys.exit(1)
    baslat(adet)
