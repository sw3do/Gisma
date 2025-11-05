# Boyce-Codd 3.5NF or BCNF

# Deternent

# SQL Structure Query Language

## Core Functionality
 - Data Retriveal
 - Data Manipulation
 - Database Structure Managament

 ## Key SQL Commands
 
  - DDL = Data definition language // CREATE - DROP- ALTER - TRUNCATE - RENAME
  - DQL = Data Query Language // Most important thing // also SELECT
  - DML = Data Manipulation Language // INSERT - UPDATE - DELETE - CALL - LOCK
  - DCL = Data Data Control Language // GRANT - REVOKE 
  - TCL - Transaction Control Language // COMMIT - ROLLBACK - SAVEPOINT


# Data Types in MariaDB

 ## Numeric Data Types
 - INT
 - BIGINT
 - DECIMAL
 - FLOAT
 - DOUBLE


## String Data Types

 - CHAR
 - VARCHAR
 - TEXT
 - ENUM

 # Date Data Types
  - Date = YYYY-MM-DD
  - TIME
  - DATETIME
  - TIMESTAMP


  ## Boolean Data Types

   - BOOLEAN: Synonym TINYINT(1), used to represent true/false values

  ## Binary Data Types
   - BLOB
   - BINARY
   - VARBINARY

   ## JSON Data Type:
    - JSON

   ## Spatial Data Types

   - GEOMETRY
   - POINT
   - LINESTRING
   - POLYGON

   # SQL FUNCTIONS


Fonksiyon	Açıklama
COUNT	Satır sayısı
SUM	Toplam
AVG	Ortalama
MIN	En küçük değer
MAX	En büyük değer
GROUPING, GROUPING_ID (bazı DB’lerde)	Grup bilgisi

-------

ABS	Mutlak değer
CEILING / CEIL	Yukarı yuvarlama
FLOOR	Aşağı yuvarlama
ROUND	Yuvarlama
POWER	Üs alma
SQRT	Karekök
MOD	Mod alma
RANDOM / RAND	Rastgele sayı
EXP, LOG, LOG10, SIN, COS, TAN, vb.	Matematik işlemleri

----------


Fonksiyon	Açıklama
CONCAT	Birleştirme
LOWER / UPPER	Küçük / büyük harf
LENGTH / LEN	Karakter uzunluğu
TRIM / LTRIM / RTRIM	Boşluk temizleme
SUBSTRING, LEFT, RIGHT	Alt string
REPLACE	Metin değiştirme
POSITION / CHARINDEX	İndeks bulma
REVERSE	Ters çevirme
FORMAT
-------------

Fonksiyon	Açıklama
NOW, CURRENT_TIMESTAMP	Şu anki tarih-saat
DATE, TIME	Tarih / saat dönüşümü
DATEDIFF, DATEADD, DATE_SUB, DATE_ADD	Tarih işlem
EXTRACT, YEAR, MONTH, DAY	Bileşen ayırma
TO_DATE, TO_CHAR	Format dönüşümleri
SYSDATE (Oracle), GETDATE (SQL Server)	Sistem zamanı

-----------

Fonksiyon	Açıklama
CAST	Veri tipi dönüştürme
CONVERT	Formatlı dönüşüm
PARSE / TRY_PARSE	Metni sayıya dönüştürme (SQL Server)
TO_NUMBER, TO_CHAR	Oracle dönüştürme

------------

Fonksiyon	Açıklama
CASE	Koşula göre değer
NULLIF	İki değer eşitse NULL döner
COALESCE	İlk null olmayan değeri döner
IIF (SQL Server)	Kısa CASE yapısı
---------
Fonksiyon	Açıklama
ROW_NUMBER	Sıra numarası
RANK / DENSE_RANK	Sıralı grup numarası
LEAD / LAG	Önceki-sonraki kayıt
FIRST_VALUE / LAST_VALUE	Pencere içi ilk-son değer
NTILE	Gruplama
OVER()	Analitik sorgu bölümü

--------------

 ## SQL Keywords

 SELECT, INSERT, UPDATE, DELETE, MERGE, CALL, EXPLAIN, LOCK, CREATE, ALTER, DROP, TRUNCATE, RENAME, COMMENT, GRANT, REVOKE, COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION, WHERE, FROM, GROUP BY, HAVING, ORDER BY, DISTINCT, LIMIT, OFFSET, FETCH, TOP, BETWEEN, IN, LIKE, EXISTS, ANY, ALL, JOIN, INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, NATURAL JOIN, ON, USING, UNION, UNION ALL, INTERSECT, EXCEPT, MINUS, PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL, DEFAULT, INDEX, KEY, TABLE, VIEW, DATABASE, SCHEMA, SEQUENCE, TRIGGER, FUNCTION, PROCEDURE, CURSOR, VALUES, INTO, AS, CASE, WHEN, THEN, ELSE, END, CAST, CONVERT, IS, NULL, TRUE, FALSE, AND, OR, NOT, ORDER, ASC, DESC, LIKE, HAVING

-------

# DATABASE SYTNAX

 CREATE SCHEMA ecommerce_gisma_2

  USE ecommerce_gisma_2;

  SHOW tables;