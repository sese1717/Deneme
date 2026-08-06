veksa_sistemi = {
    "kompresor":{
        "model":"Mitsubishi SVB220FLGMC-LS",
        "kapasite_kw":10.0,
        "durum":"Aktif",
        "ortalama_hiz":60
    },
    "filtre_drayer":{
        "gorev":"Nem ve pislik tutucu",
        "kontrol":"temiz",
        "kritik_parca": True
    },
    "gozetleme_cami" :{
        "gorev":"Akis ve nem görmek icin",
        "durum":"Cam gibi berrak",
        "kritik_parca": False
    }
}

print("---VEM-1 Sisteminde Kayıtlı Modüller---")
# DÜZELTME 1: Buradaki parantezler kaldırıldı (.keys() yerine doğrudan sözlük taranıyor)
for gereksiz in veksa_sistemi:
    print(f"- {gereksiz}")

print("="*40)

aranan = "kompresor"
if aranan in veksa_sistemi:
    print(f"[{aranan.upper()}] Detayları:")
    print(f"  Model: {veksa_sistemi[aranan]['model']}")
    print(f"  Kapasite: {veksa_sistemi[aranan]['kapasite_kw']} kW")
    # DÜZELTME 2: 'ortalama_hz' yerine yukarıda tanımladığımız 'ortalama_hiz' yazıldı
    print(f"  Çalışma Frekansı: {veksa_sistemi[aranan]['ortalama_hiz']} Hz")

print("=" * 40)

veksa_sistemi["tank_sicaklik"] = 42.5
print(f"Sisteme sonradan eklenen Tank Sıcaklığı Sensörü: {veksa_sistemi['tank_sicaklik']} °C")

