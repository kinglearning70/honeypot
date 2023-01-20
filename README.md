# honeypot
installation honeypot
Untuk menjalankan instalasi, tempatkan script di folder home (umumnya folder yang
ada ketika baru masuk via SSH), kemudian jalankan sudo bash nama_script.sh.
Script ini akan melakukan instalasi Docker, MongoDB, EWS Poster dan membuat
image Docker honeypot.
Setelah proses instalasi selesai, login berikutnya ke SSH harus melalui port 22888. Hal
ini dikarenakan port 22 akan ditempati oleh honeypot SSH Cowrie

Jalankan pwd untuk mengetahui working directory saat ini. Kemudian cd ewsposter
untuk pindah ke ewsposter dan lakukan edit pada file ews.cfg dengan menggunakan
teks editor, misal sudo nano ews.cfg.
Di dalam file ews.cfg, pastikan pada file dibawah ini diubah sesuai dengan workdir sesuai perintah pwd 
main: homedir, spoldir, logdir (workdir)
ewsjson: jsondir (workdir)
cowrie: nodeid (sensorname)
dionaea: nodeid (sensorname)
gridpot: nodeid (sensorname)
elasticpot: modeid (sensorname)
rdpy: nodeid (sensorname)
honeytrapv2: nodeid (sensorname)

Pengujian dilakukan dengan melakukan simulasi serangan dari luar atau dari dalam
organisasi ke port-port honeypot yang sudah terbuka. Pengujian ini perlu untuk
memastikan honeypot dapat diakses dari luar atau dari dalam (tergantung dari
kebutuhan organisasi). Alat simulasi yang dibutuhkan bisa menggunakan nmap,
misalnya dengan menggunakan perintah: nmap <IP> -T5 -sV

Setiap data serangan yang masuk ke honeypot akan disimpan di dalam database
MongoDB lokal.
Setelah langkah nomor 6 berhasil, jalankan perintah berikut
cd
cd ewsposter
sudo python3 ews.py

Untuk melihat data yang sudah terkumpul dapat mengikuti cara sebagai berikut:
1. Akses langsung melalui database MongoDB lokal.
a. Di dalam terminal Linux, eksekusi perintah mongo untuk masuk ke dalam
terminal MongoDB.
b. Untuk melihat database yang tersedia, jalankan show dbs. Pastikan ada
database yang bernama ewsdb.
c. Untuk menggunakan database tersebut, jalankan perintah use ewsdb.
d. Untuk melihat semua collections yang tersedia, jalankan show
collections. Pastikan ada collection bernama honeypots
e. Data honeypot tersimpan di dalam collection honeypots. Untuk melihat
data, jalankan perintah:
i. db.honeypots.find().sort({time:-1}).limit(3)
f. Pastikan timestamp pada poin e tepat.
g. Untuk melakukan filtering, sorting, dan juga export data, silakan merujuk
kepada dokumentasi MongoDB

e. Data honeypot tersimpan di dalam collection honeypots. Untuk melihat
data, jalankan perintah:
i. db.honeypots.find().sort({time:-1}).limit(3)
f. Pastikan timestamp pada poin e tepat.
g. Untuk melakukan filtering, sorting, dan juga export data, silakan merujuk
kepada dokumentasi MongoDB yang dapat diakses melalui link ini.

Proses ini hanya dilakukan ketika poin 6 dan poin 7 sudah berhasil dijalankan tanpa
ada kendala.
1. Pindah ke folder ewsposter
2. sudo nohup python3 ews.py -l 60
3. ctrl+z
4. bg x -> dimana x adalah angka yang muncul di step 3

Berikutnya pindah ke folder dimana script sync_mongo_tenant.py berada
1. sudo nohup python3 sync_mongo_tenant.py
2. ctrl + z
3. bg x -> dimana x adalah angka yang muncul di step 3
