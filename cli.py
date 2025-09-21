#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İçerik Ajanı CLI - Komut Satırı Arayüzü
Content Agent Command Line Interface

Bu script ile içerik ajanını kolayca kullanabilirsiniz.
"""

import argparse
import sys
import os
from content_agent import ContentAgent


def main():
    parser = argparse.ArgumentParser(
        description="Facebook profili için içerik oluşturma ajanı",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Kullanım Örnekleri:
  python cli.py --generate                    # Tek içerik oluştur
  python cli.py --category motivasyon         # Belirli kategoride içerik
  python cli.py --daily 5                     # 5 günlük plan oluştur
  python cli.py --daily 3 --save plan.json   # Planı kaydet
        """
    )
    
    parser.add_argument(
        '--generate', 
        action='store_true',
        help='Tek bir içerik oluştur'
    )
    
    parser.add_argument(
        '--category',
        choices=['motivasyon', 'iş_ipuçları', 'etkileşim', 'eğitim', 'tanıtım'],
        help='Belirli kategoride içerik oluştur'
    )
    
    parser.add_argument(
        '--daily',
        type=int,
        metavar='N',
        help='N adet günlük içerik oluştur'
    )
    
    parser.add_argument(
        '--save',
        metavar='DOSYA',
        help='İçerikleri belirtilen dosyaya kaydet'
    )
    
    parser.add_argument(
        '--config',
        metavar='CONFIG_FILE',
        default='config.json',
        help='Konfigürasyon dosyası (varsayılan: config.json)'
    )
    
    args = parser.parse_args()
    
    # Eğer hiç argüman verilmemişse help göster
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    try:
        # Konfigürasyon dosyası kontrolü
        config_file = args.config if os.path.exists(args.config) else None
        agent = ContentAgent(config_file)
        
        print("🤖 İçerik Oluşturma Ajanı")
        print("=" * 40)
        
        if args.generate:
            # Tek içerik oluştur
            content = agent.generate_content(args.category)
            print_content(content)
            
            if args.save:
                agent.save_content_plan([content], args.save)
                
        elif args.daily:
            # Günlük içerik planı
            daily_content = agent.generate_daily_content(args.daily)
            
            print(f"\n📅 {args.daily} Adet İçerik Planı:")
            print("=" * 40)
            
            for i, content in enumerate(daily_content, 1):
                print(f"\n📝 İçerik #{i}")
                print_content(content)
                
            if args.save:
                agent.save_content_plan(daily_content, args.save)
                print(f"\n💾 İçerikler {args.save} dosyasına kaydedildi.")
                
        elif args.category:
            # Kategori bazlı içerik
            content = agent.generate_content(args.category)
            print_content(content)
            
            if args.save:
                agent.save_content_plan([content], args.save)
                
    except Exception as e:
        print(f"❌ Hata: {e}")
        sys.exit(1)


def print_content(content):
    """İçeriği formatlı şekilde yazdır"""
    print(f"\n🏷️ Kategori: {content['category'].title()}")
    print("-" * 30)
    print(content['content'])
    print(f"\n🔗 Hashtags: {content['hashtags']}")
    print(f"🎯 Tür: {content['engagement_type']}")
    print(f"⏰ Tarih: {content['created_at']}")
    print("-" * 40)


if __name__ == "__main__":
    main()