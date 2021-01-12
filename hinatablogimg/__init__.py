__name__ = 'hinatablogimg'

import os
from pathlib import Path

HINATADIR = os.environ.get("HINATABLOGIMG_HINATADIR", "./img")
CREATEDIR = True
LOGCONFPATH = os.environ.get("HINATABLOGIMG_LOGCONFPATH",
                             Path(__file__).parent.joinpath('logconfig.yml'))
MEMBER = {
    "潮 紗理菜": "ushio_sarina",
    "影山 優佳": "kageyama_yuuka",
    "加藤 史帆": "katou_shiho",
    "齊藤 京子": "saitou_kyouko",
    "佐々木 久美": "sasaki_kumi",
    "佐々木 美玲": "sasaki_mirei",
    "高瀬 愛奈": "takase_mana",
    "高本 彩花": "takamoto_ayaka",
    "東村 芽依": "higasimura_mei",
    "金村 美玖": "kanemura_miku",
    "河田 陽菜": "kawata_hina",
    "小坂 菜緒": "kosaka_nao",
    "富田 鈴花": "tomita_suzuka",
    "丹生 明里": "nibu_akari",
    "濱岸 ひより": "hamagishi_hiyori",
    "松田 好花": "maruda_konoka",
    "宮田 愛萌": "miyata_manamo",
    "渡邉 美穂": "watanabe_miho",
    "上村 ひなの": "kamimura_hinano",
    "髙橋 未来虹": "takahashi_mikuni",
    "森本 茉莉": "morimoto_marili",
    "山口 陽世": "yamaguchi_haruyo",
}
