Select ad,soyad,p.gorev,maas+maas as 'zm' FROM
(
select gorev,sum(maas)as 'tm',avg(maas)as 'am'
from personel GROUP by gorev
order by tm DESC
)x,personel as 'p'
where p.gorev=x.gorev and x.am > p.maas
--En düşük maaş alanın adı soyadı gorevi