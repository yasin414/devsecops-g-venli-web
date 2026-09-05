DevSecOps Güvenli Web Uygulaması
Bu proje, basit bir Python Flask web uygulamasının DevSecOps yaklaşımı kullanılarak geliştirilmesini ve güvenlik kontrollerinin CI/CD sürecine dahil edilmesini amaçlamaktadır.
Projenin Amacı
Uygulama geliştirme sürecinde güvenlik kontrollerinin otomatik olarak gerçekleştirilmesi hedeflenmiştir.
Pipeline içerisinde aşağıdaki güvenlik ve DevOps araçları kullanılmaktadır:
* GitHub Actions — CI/CD otomasyonu
* Semgrep — Kaynak kod güvenlik analizi (SAST)
* Docker — Uygulamanın container haline getirilmesi
* Trivy — Docker image güvenlik taraması
* OWASP ZAP — Web uygulaması güvenlik testi (DAST)
* GitHub Container Registry (GHCR) — Docker image saklama
Kullanılan Teknolojiler
* Python
* Flask
* Docker
* Git / GitHub
* GitHub Actions
* Semgrep
* Trivy
* OWASP ZAP
* GitHub Container Registry
CI/CD Güvenlik Akışı
Kod
 ↓
GitHub
 ↓
Semgrep
 ↓
Docker Build
 ↓
Trivy
 ↓
OWASP ZAP
 ↓
GHCR
Güvenlik Kontrolleri
1. Semgrep
Semgrep ile Python kaynak kodu güvenlik açısından analiz edilmektedir.
Projede ayrıca özel bir Semgrep kuralı oluşturulmuştur. Örneğin:
password = "admin123"
gibi sabit kodlanmış parola kullanımı özel Semgrep kuralı tarafından tespit edilmektedir.
2. Trivy
Trivy, oluşturulan Docker image içerisindeki güvenlik açıklarını taramaktadır.
Pipeline içerisinde CRITICAL ve HIGH seviyesindeki açıklar kontrol edilmektedir.
3. OWASP ZAP
OWASP ZAP, çalışan Flask web uygulamasını otomatik olarak tarayarak web uygulamasındaki güvenlik problemlerini kontrol etmektedir.
4. Docker
Uygulama Docker container içerisinde çalıştırılmaktadır.
Kullanılan port:
5000
Yerel kullanımda uygulamaya örneğin aşağıdaki adres üzerinden erişilebilir:
http://localhost:5001
Projenin Çalıştırılması
Docker image oluşturmak için:
docker build -t devsecops-web .
Container çalıştırmak için:
docker run -d -p 5001:5000 --name devsecops-container devsecops-web
Daha sonra tarayıcıdan:
http://localhost:5001
adresine gidilebilir.
Sonuç
Bu proje ile yazılım geliştirme sürecine güvenlik kontrolleri entegre edilmiştir.
Kaynak kod güvenliği, container güvenliği ve web uygulaması güvenliği otomatik CI/CD sürecinin bir parçası haline getirilmiştir.
Proje, DevSecOps yaklaşımının temel bir uygulamasını göstermektedir.
