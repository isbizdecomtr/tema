#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İçerik Oluşturma Ajanı (Content Creation Agent)
Facebook profili için otomatik içerik üreten ajan

Bu ajan çeşitli türlerde sosyal medya içeriği oluşturabilir:
- Motivasyonel sözler
- İş ipuçları
- Etkileşim artırıcı gönderiler
- Eğitici içerikler
- Tanıtım içerikleri
"""

import random
import json
import datetime
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class ContentTemplate:
    """İçerik şablonu sınıfı"""
    category: str
    template: str
    hashtags: List[str]
    engagement_type: str


class ContentAgent:
    """İçerik oluşturma ajanı ana sınıfı"""
    
    def __init__(self, config_file: str = None):
        self.templates = self._load_templates()
        self.config = self._load_config(config_file) if config_file else self._default_config()
        
    def _default_config(self) -> Dict[str, Any]:
        """Varsayılan konfigürasyon ayarları"""
        return {
            "brand_name": "İş Dünyası",
            "target_audience": "girişimciler",
            "tone": "profesyonel ve motivasyonel",
            "posting_frequency": "günlük",
            "preferred_categories": ["motivasyon", "iş_ipuçları", "başarı"]
        }
    
    def _load_config(self, config_file: str) -> Dict[str, Any]:
        """Konfigürasyon dosyasından ayarları yükle"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Konfigürasyon dosyası bulunamadı: {config_file}")
            return self._default_config()
    
    def _load_templates(self) -> List[ContentTemplate]:
        """İçerik şablonlarını yükle"""
        templates = [
            # Motivasyonel İçerikler
            ContentTemplate(
                category="motivasyon",
                template="🌟 {motivational_quote}\n\n💪 Bugün kendine inan ve hedeflerine bir adım daha yaklaş!\n\n#motivasyon #başarı #hedefler",
                hashtags=["#motivasyon", "#başarı", "#hedefler", "#ilham"],
                engagement_type="inspiration"
            ),
            ContentTemplate(
                category="motivasyon",
                template="✨ Her başarı hikayesi bir rüya ile başlar.\n\n🎯 Sen de bugün kendi hikayeni yazmaya başla!\n\n{call_to_action}",
                hashtags=["#başarıhikayesi", "#rüyalar", "#motivasyon"],
                engagement_type="inspiration"
            ),
            
            # İş İpuçları
            ContentTemplate(
                category="iş_ipuçları",
                template="💼 İş Dünyasında Başarı İpucu #{tip_number}:\n\n{business_tip}\n\n👥 Bu ipucunu arkadaşlarınla paylaş!",
                hashtags=["#işipuçları", "#başarı", "#girişimcilik", "#profesyonelgelişim"],
                engagement_type="educational"
            ),
            ContentTemplate(
                category="iş_ipuçları",
                template="🚀 Girişimciler için altın tavsiye:\n\n{entrepreneurship_advice}\n\n💡 Sen de deneyimlerini yorumlarda paylaş!",
                hashtags=["#girişimcilik", "#iştavsiyeleri", "#başarı"],
                engagement_type="educational"
            ),
            
            # Etkileşim Artırıcı Gönderiler
            ContentTemplate(
                category="etkileşim",
                template="🤔 Soru: {question}\n\nA) {option_a}\nB) {option_b}\n\n👇 Cevabını yorumlarda paylaş ve arkadaşlarını etiketle!",
                hashtags=["#soru", "#etkileşim", "#topluluk"],
                engagement_type="question"
            ),
            ContentTemplate(
                category="etkileşim",
                template="📊 Hangi konuda daha fazla içerik görmek istersiniz?\n\n{poll_options}\n\n💬 Yorumlarda fikirlerinizi paylaşın!",
                hashtags=["#anket", "#içerik", "#geribildirim"],
                engagement_type="poll"
            ),
            
            # Eğitici İçerikler
            ContentTemplate(
                category="eğitim",
                template="📚 Bugünün Konusu: {topic}\n\n{educational_content}\n\n🔗 Daha fazlası için takipte kalın!",
                hashtags=["#eğitim", "#bilgi", "#öğrenme"],
                engagement_type="educational"
            ),
            
            # Tanıtım İçerikleri
            ContentTemplate(
                category="tanıtım",
                template="🎉 {announcement}\n\n{details}\n\n👆 Daha fazla bilgi için profil linkimizi ziyaret edin!",
                hashtags=["#duyuru", "#yenilik", "#heyecan"],
                engagement_type="promotional"
            )
        ]
        return templates
    
    def generate_content(self, category: str = None) -> Dict[str, str]:
        """Belirtilen kategoride içerik oluştur"""
        if category:
            available_templates = [t for t in self.templates if t.category == category]
        else:
            available_templates = self.templates
            
        if not available_templates:
            raise ValueError(f"Kategori bulunamadı: {category}")
            
        template = random.choice(available_templates)
        content = self._fill_template(template)
        
        return {
            "content": content,
            "category": template.category,
            "hashtags": " ".join(template.hashtags),
            "engagement_type": template.engagement_type,
            "created_at": datetime.datetime.now().isoformat()
        }
    
    def _fill_template(self, template: ContentTemplate) -> str:
        """Şablonu içerikle doldur"""
        content = template.template
        
        # Motivasyonel sözler
        motivational_quotes = [
            "Başarı, hazırlık fırsatla buluştuğunda doğar.",
            "Büyük işler yapabilmek için büyük düşünmek gerekir.",
            "Engeller yoldan çıkarmak için değil, hedefe ne kadar ulaşmak istediğini test etmek için vardır.",
            "Her uzman bir zamanlar acemiydi.",
            "Başarı bir gece oluşmaz, sürekli çalışmanın sonucudur."
        ]
        
        # İş ipuçları
        business_tips = [
            "Müşteri geri bildirimlerini düzenli olarak toplayın ve analiz edin. Bu size hizmetinizi geliştirmek için değerli ipuçları verir.",
            "Zaman yönetiminizi optimize edin. Öncelikli görevleri belirleyin ve günlük planınızı buna göre oluşturun.",
            "Ağınızı sürekli genişletin. Her yeni bağlantı potansiyel bir fırsat demektir.",
            "Teknolojik gelişmeleri takip edin ve işinize nasıl entegre edebileceğinizi düşünün.",
            "Sürekli öğrenmeyi bir yaşam tarzı haline getirin. Sektörünüzdeki yenilikleri takip edin."
        ]
        
        # Girişimcilik tavsiyeleri
        entrepreneurship_advice = [
            "Başlamadan önce mükemmel planı beklemeyin. Başlayın ve yol üzerinde düzeltin.",
            "Başarısızlıkları öğrenme fırsatı olarak görün. Her hata sizi hedefinize bir adım daha yaklaştırır.",
            "Müşteri odaklı düşünün. Çözdüğünüz problem ne kadar büyükse, başarı şansınız o kadar yüksektir.",
            "Ekip oluşturmaya yatırım yapın. Tek başınıza gidemeyeceğiniz yerlere ekibinizle gidebilirsiniz.",
            "Sabırlı olun ama kararlı da olun. Büyük başarılar zaman ister."
        ]
        
        # Sorular
        questions = [
            "Girişimcilikte en büyük zorluk sizce nedir?",
            "Başarı için en önemli özellik hangisidir?",
            "Yeni bir iş kuracak olsanız hangi sektörü seçerdiniz?",
            "İş hayatında en çok nelere öncelik verirsiniz?"
        ]
        
        # Seçenekler
        options_pairs = [
            ("Risk almak", "Güvenli oynamak"),
            ("Yaratıcılık", "Disiplin"),
            ("Teknoloji", "Geleneksel sektörler"),
            ("Kalite", "Hız")
        ]
        
        # Konular
        topics = [
            "Dijital Pazarlama Temelleri",
            "Etkili İletişim Teknikleri",
            "Zaman Yönetimi Stratejileri",
            "Müşteri Hizmetleri Excellence",
            "Liderlik Becerilerini Geliştirme"
        ]
        
        # Eğitici içerikler
        educational_contents = [
            "Dijital pazarlama bugünün dünyasında vazgeçilmez bir araçtır. Hedef kitlenizi tanıyın, doğru platformları seçin ve düzenli içerik üretin.",
            "Etkili iletişimin anahtarı dinlemektir. Konuşmadan önce karşınızdakini anlayın ve ona göre mesajınızı oluşturun.",
            "Zamanınızı verimli kullanmak için günlük, haftalık ve aylık hedefler belirleyin. Önemli-acil matrisini kullanın.",
            "Müşteri memnuniyeti işinizin temel taşıdır. Her müşteriyi özel hissettirin ve beklentilerini aşmaya çalışın.",
            "Liderlik pozisyon değil, eylemdir. Örnek olun, ekibinizi motive edin ve ortak hedeflere odaklanın."
        ]
        
        # Template doldurma
        replacements = {
            "{motivational_quote}": random.choice(motivational_quotes),
            "{business_tip}": random.choice(business_tips),
            "{entrepreneurship_advice}": random.choice(entrepreneurship_advice),
            "{question}": random.choice(questions),
            "{option_a}": options_pairs[0][0] if options_pairs else "Seçenek A",
            "{option_b}": options_pairs[0][1] if options_pairs else "Seçenek B",
            "{topic}": random.choice(topics),
            "{educational_content}": random.choice(educational_contents),
            "{tip_number}": str(random.randint(1, 100)),
            "{call_to_action}": "💬 Sen ne düşünüyorsun? Yorumlarda paylaş!",
            "{announcement}": "Heyecan verici yenilikler geliyor!",
            "{details}": "Yakında sizlerle paylaşacağımız özel içerikler için takipte kalın.",
            "{poll_options}": "🔹 Motivasyon\n🔹 İş İpuçları\n🔹 Başarı Hikayeleri\n🔹 Girişimcilik"
        }
        
        for placeholder, replacement in replacements.items():
            content = content.replace(placeholder, replacement)
            
        return content
    
    def generate_daily_content(self, count: int = 3) -> List[Dict[str, str]]:
        """Günlük içerik planı oluştur"""
        categories = ["motivasyon", "iş_ipuçları", "etkileşim"]
        daily_content = []
        
        for i in range(count):
            category = categories[i % len(categories)]
            content = self.generate_content(category)
            daily_content.append(content)
            
        return daily_content
    
    def save_content_plan(self, content_list: List[Dict[str, str]], filename: str = None):
        """İçerik planını dosyaya kaydet"""
        if not filename:
            filename = f"content_plan_{datetime.datetime.now().strftime('%Y%m%d')}.json"
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content_list, f, ensure_ascii=False, indent=2)
            
        print(f"İçerik planı kaydedildi: {filename}")


def main():
    """Ana çalıştırma fonksiyonu"""
    print("🤖 İçerik Oluşturma Ajanı Başlatılıyor...\n")
    
    # Ajanı başlat
    agent = ContentAgent()
    
    # Günlük içerik planı oluştur
    daily_content = agent.generate_daily_content(5)
    
    print("📅 Günlük İçerik Planı:")
    print("=" * 50)
    
    for i, content in enumerate(daily_content, 1):
        print(f"\n📝 İçerik #{i} - Kategori: {content['category'].title()}")
        print("-" * 30)
        print(content['content'])
        print(f"\n🏷️ Hashtags: {content['hashtags']}")
        print(f"🎯 Etkileşim Türü: {content['engagement_type']}")
        print(f"⏰ Oluşturulma: {content['created_at']}")
        print("\n" + "="*50)
    
    # İçerik planını kaydet
    agent.save_content_plan(daily_content)
    
    print("\n✅ İçerik oluşturma tamamlandı!")
    print("📁 İçerik planı JSON dosyası olarak kaydedildi.")
    print("\n💡 İpucu: Bu içerikleri Facebook profilinizde farklı zamanlarda paylaşabilirsiniz.")


if __name__ == "__main__":
    main()