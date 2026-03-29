# Tugas 2 PKPL : Authentication & Authorization

Website biodata kelompok dengan implementasi Google OAuth 2.0 dan Role-Based Access Control (RBAC) sederhana. 
Dibuat untuk memenuhi Tugas 2 mata kuliah Pengantar Keamanan Perangkat Lunak.

## Anggota Kelompok
* Andrew Sanjay Hasian Panjaitan - 2406403482
* Jarred Muhammad - 2406432425
* Farrel Faridzi Liwungang - 2406436240
* Riyaan Baihaqi - 2406358762
* Dery Andreas - 2406347380

## Fitur Keamanan yang Diimplementasikan
* **Authentication:** Menggunakan Google OAuth 2.0 (via `django-allauth`) untuk memastikan identitas pengguna.
* **Authorization:** Hanya pengguna dengan email yang terdaftar di konfigurasi sistem (anggota kelompok) yang memiliki hak akses untuk mengubah warna tema website. Pengguna lain yang login hanya diberikan akses *read-only*.