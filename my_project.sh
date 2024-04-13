#!/bin/bash

# GitHub depo URL'si
github_repo="https://github.com/kullanici/depom"

# Depoyu klonla
git clone "$github_repo" indirilen_dosyalar

# Başarı durumunu kontrol et
if [ $? -eq 0 ]; then
    echo "GitHub'daki dosyalar başarıyla indirildi."
else
    echo "Hata: GitHub'daki dosyalar indirilemedi."
    exit 1
fi

# Klonlanan dosyaların içeriğini listele
echo "İndirilen dosyaların içeriği:"
ls -l indirilen_dosyalar

# Burada işlem tamamlandıktan sonra diğer işlemleri ekleyebilirsiniz.
