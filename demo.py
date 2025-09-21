#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script - İçerik Ajanı Tanıtımı
Facebook profili için oluşturulan içerik ajanının demo gösterimi
"""

import os
import sys
from content_agent import ContentAgent


def demo_content_agent():
    """İçerik ajanı demo fonksiyonu"""
    print("🎭 İçerik Oluşturma Ajanı - DEMO")
    print("=" * 50)
    print("Facebook Profili: https://www.facebook.com/profile.php?id=61579971112511")
    print("=" * 50)
    
    # Ajanı başlat
    agent = ContentAgent("config.json")
    
    print("\n📋 Mevcut Kategoriler:")
    categories = ["motivasyon", "iş_ipuçları", "etkileşim", "eğitim", "tanıtım"]
    for i, cat in enumerate(categories, 1):
        print(f"   {i}. {cat.replace('_', ' ').title()}")
    
    print("\n" + "="*50)
    print("🎯 Her kategoriden örnek içerik oluşturuluyor...")
    print("="*50)
    
    demo_contents = []
    
    for category in categories:
        try:
            content = agent.generate_content(category)
            demo_contents.append(content)
            
            print(f"\n📝 {category.replace('_', ' ').title()} Kategorisi:")
            print("-" * 30)
            print(content['content'])
            print(f"\n🏷️ Hashtags: {content['hashtags']}")
            print(f"🎯 Etkileşim Türü: {content['engagement_type']}")
            print("\n" + "="*50)
            
        except Exception as e:
            print(f"❌ {category} kategorisinde hata: {e}")
    
    # Demo içerikleri kaydet
    demo_filename = "demo_content_examples.json"
    agent.save_content_plan(demo_contents, demo_filename)
    
    print(f"\n💾 Demo içerikleri {demo_filename} dosyasına kaydedildi.")
    print("\n✨ Demo tamamlandı!")
    
    print("\n📖 Kullanım Örnekleri:")
    print("   • Tek içerik: python cli.py --generate")
    print("   • Belirli kategori: python cli.py --category motivasyon")
    print("   • Günlük plan: python cli.py --daily 5")
    print("   • Kaydetme: python cli.py --daily 3 --save plan.json")
    
    return demo_contents


def show_config_info():
    """Konfigürasyon bilgilerini göster"""
    print("\n⚙️ Konfigürasyon Bilgileri:")
    print("-" * 30)
    
    try:
        import json
        with open("config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
            
        print(f"📊 Marka: {config.get('brand_name', 'N/A')}")
        print(f"🎯 Hedef Kitle: {config.get('target_audience', 'N/A')}")
        print(f"🗣️ Ton: {config.get('tone', 'N/A')}")
        print(f"📅 Paylaşım Sıklığı: {config.get('posting_frequency', 'N/A')}")
        print(f"🔗 Facebook: {config.get('facebook_profile', {}).get('url', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Konfigürasyon okunamadı: {e}")


if __name__ == "__main__":
    try:
        # Demo'yu çalıştır
        demo_contents = demo_content_agent()
        
        # Konfigürasyon bilgilerini göster
        show_config_info()
        
        print(f"\n🎉 Demo başarıyla tamamlandı!")
        print(f"📊 Toplam {len(demo_contents)} farklı kategoride içerik oluşturuldu.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo kullanıcı tarafından sonlandırıldı.")
        
    except Exception as e:
        print(f"\n❌ Demo sırasında hata oluştu: {e}")
        sys.exit(1)