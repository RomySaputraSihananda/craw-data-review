from enum import Enum
from json import loads

class BaseEnum(Enum):
	@property
	def value(self):
		return loads(self._value_)

class StatistikEnum(BaseEnum):
	STATISTIK_WISATAWAN_NUSANTARA = '{"id":"640cd6f5-1edb-43bb-8053-b21161906d25","slug":"statistik-wisatawan-nusantara","title":"Statistik Wisatawan Nusantara","subtitle":"Data Statistik Wisatawan Nusantara Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"20"}'
	STATISTIK_WISATAWAN_MANCANEGARA = '{"id":"76b7f0c8-4a58-4f15-afe0-a3a69555d0f4","slug":"statistik-wisatawan-mancanegara","title":"Statistik Wisatawan Mancanegara","subtitle":"Data Statistik Wisatawan Mancanegara Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"21"}'
	STATISTIK_WISATAWAN_NASIONAL = '{"id":"fae3e9da-52b0-48c1-83ed-029ddcab8fd4","slug":"statistik-wisatawan-nasional","title":"Statistik Wisatawan Nasional","subtitle":"Data Statistik Wisatawan Nasional Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"22"}'
	STATISTIK_AKOMODASI = '{"id":"f13d4719-e397-47de-a348-6aa853f014af","slug":"statistik-akomodasi","title":"Statistik Akomodasi","subtitle":"Data Statistik Akomodasi Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"23"}'
	STATISTIK_USAHA_RESTORAN = '{"id":"2ebeda95-470c-4c52-aea5-ed1e476d3f9e","slug":"statistik-usaha-restoran","title":"Statistik Usaha Restoran","subtitle":"Data Statistik Usaha Restoran Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"24"}'
	STATISTIK_JASA_PERJALANAN = '{"id":"7aa6358c-4920-4234-84c9-a4f71559b27e","slug":"statistik-jasa-perjalanan","title":"Statistik Jasa Perjalanan","subtitle":"Data Statistik Jasa Perjalanan Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"25"}'
	STATISTIK_SATELIT_PARIWISATA = '{"id":"67173bed-fb5e-4502-ab72-286543a0d4e0","slug":"statistik-satelit-pariwisata","title":"Statistik Satelit Pariwisata","subtitle":"Data Statistik Satelit Pariwisata Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"26"}'
	STATISTIK_DEVISA_PARIWISATA = '{"id":"d3166608-3784-4620-8f47-27baae60904d","slug":"statistik-devisa-pariwisata","title":"Statistik Devisa Pariwisata","subtitle":"Data Statistik Devisa Pariwisata Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"27"}'
	NERACA_JASA_PERJALANAN_INDONESIA = '{"id":"bb52890d-18e5-454a-8592-f599f086b5d3","slug":"neraca-jasa-perjalanan-indonesia","title":"Neraca Jasa Perjalanan Indonesia","subtitle":"Data Neraca Jasa Perjalanan Indonesia Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"28"}'
	PUBLIKASI_STATISTIK_WISATAWAN_MANCANEGARA_DALAM_ANGKA = '{"id":"140d48aa-5a3e-4731-a19a-37fc4bdf4e0f","slug":"publikasi-statistik-kunjungan-wisatawan-mancanegara","title":"Publikasi Statistik Wisatawan Mancanegara Dalam Angka","subtitle":"Data Publikasi Statistik Wisatawan Mancanegara Dalam Angka Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"29"}'
	PUBLIKASI_PASSENGER_EXIT_SURVEY = '{"id":"cd52dd81-ab72-4de2-b7c0-009865ad9a16","slug":"publikasi-passenger-exit-survey","title":"Publikasi Passenger Exit Survey","subtitle":"Data Publikasi Passenger Exit Survey Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"30"}'
	PUBLIKASI_WISATAWAN_NUSANTARA = '{"id":"4ee4c672-435b-4140-a1ff-db7ffe8b3d15","slug":"publikasi-wisatawan-nusantara","title":"Publikasi Wisatawan Nusantara","subtitle":"Data Publikasi Wisatawan Nusantara Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"32"}'
	PUBLIKASI_NESPARNAS = '{"id":"a3be0d81-23ef-4374-a748-9bcc1a050c36","slug":"publikasi-nesparnas","title":"Publikasi Nesparnas","subtitle":"Data Publikasi Nesparnas Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"35"}'
	KLASIFIKASI_BAKU_LAPANGAN_USAHA_INDONESIA_PARIWISATA_DAN_EKONOMI_KREATIF = '{"id":"2fddac6b-da17-4bdb-907f-a015b80281de","slug":"klasifikasi-baku-lapangan-usaha-indonesia-pariwisata","title":"Klasifikasi Baku Lapangan Usaha Indonesia Pariwisata dan Ekonomi Kreatif","subtitle":"Data Klasifikasi Baku Lapangan Usaha Indonesia Pariwisata dan Ekonomi Kreatif Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"37"}'
	PUBLIKASI_STATISTIK_EKONOMI_KREATIF = '{"id":"f54548d9-b697-4ddd-bb89-e57a0bc2cd69","slug":"publikasi-statistik-ekonomi-kreatif","title":"Publikasi Statistik Ekonomi Kreatif","subtitle":"Data Publikasi Statistik Ekonomi Kreatif Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"60"}'
	STATISTIK_PARIWISATA_DAN_EKONOMI_KREATIF = '{"id":"fcf63e0a-4678-4ac0-8ca1-83364ada448d","slug":"statistik-pariwisata-dan-ekonomi-kreatif","title":"Statistik Pariwisata dan Ekonomi Kreatif","subtitle":"Data Statistik Pariwisata dan Ekonomi Kreatif Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"61"}'
	STATISTIK_EKONOMI_KREATIF = '{"id":"040d2d5c-ffb2-4143-9eaf-00628f66f0fd","slug":"statistik-ekonomi-kreatif","title":"Statistik Ekonomi Kreatif","subtitle":"Data Statistik Ekonomi Kreatif Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"62"}'
	DIREKTORI_STATISTIK = '{"id":"b439b172-76f5-49eb-ba6b-52f105e2ff29","slug":"direktori-statistik","title":"Direktori Statistik","subtitle":"Direktori Statistik Kemenparekraf / Baparekraf Republik Indonesia","category":true,"type":"grid","detail":true,"search":true,"badgeCategory":true,"tab":false,"tabData":null,"categoryFilter":"-1"}'
	VISUALISASI_STATISTIK_ = '{"id":"e2095b1a-4d8e-11ee-be56-0242ac120002","slug":"visualisasi-statistik","title":"Visualisasi Statistik ","subtitle":"Visualisasi Statistik Kemenparekraf / Baparekraf Republik Indonesia","category":false,"type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoryFilter":"63"}'

class ProfilEnum(BaseEnum):
	AGENDA_PIMPINAN = '{"id":"6fd86ab5-6aca-47e1-9163-b70692fdc633","slug":"agenda-pimpinan","title":"Agenda Pimpinan","subtitle":"Agenda Kegiatan Pimpinan Kementerian Pariwisata dan Ekonomi Kreatif/ Badan Pariwisata dan Ekonomi Kreatif Republik Indonesia","type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoriesFilter":[54],"cardsFilter":[],"tagsFilter":[],"dppsFilter":[]}'
	DATA_KEPEGAWAIAN = '{"id":"9b91f7d6-a8a0-4bb2-9f9e-7db6de8c0b1c","slug":"data-kepegawaian","title":"Data Kepegawaian","subtitle":"Data Kepegawaian Kementerian Pariwisata dan Ekonomi Kreatif/ Badan Pariwisata dan Ekonomi Kreatif Republik Indonesia","type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoriesFilter":[52],"cardsFilter":[],"tagsFilter":[],"dppsFilter":[]}'
	REALISASI_ANGGARAN = '{"id":"526f9cea-325e-4ee2-87dd-60c0836228e1","slug":"realisasi-anggaran","title":"Realisasi Anggaran","subtitle":"Laporan Realisasi Anggaran Kementerian Pariwisata dan Ekonomi Kreatif/ Badan Pariwisata dan Ekonomi Kreatif Republik Indonesia","type":"grid","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoriesFilter":[53],"cardsFilter":[],"tagsFilter":[],"dppsFilter":[]}'
	LAPORAN_HARTA_KEKAYAAN_PEJABAT_NEGARA_DAN_APARATUR_SIPIL_NEGARA = '{"id":"526f9cea-325e-4ee2-87dd-60c0836228e1","slug":"lhkpn-lhkasn","title":"Laporan Harta Kekayaan Pejabat Negara dan Aparatur Sipil Negara","subtitle":"Laporan Harta Kekayaan Pejabat Negara dan Aparatur Sipil Negara di lingkungan Kementerian Pariwisata dan Ekonomi Kreatif/ Badan Pariwisata dan Ekonomi Kreatif Republik Indonesia","type":"list","detail":true,"search":true,"badgeCategory":false,"tab":false,"tabData":null,"categoriesFilter":[72],"cardsFilter":[],"tagsFilter":[],"dppsFilter":[]}'
