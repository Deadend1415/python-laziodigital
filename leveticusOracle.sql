--3.1
/* SELECT NOME,COGNOME,'per_mese' AS RICERCA
FROM DIPENDENTI 
WHERE EXTRACT(MONTH FROM DT_ASSUNZ) != '03'
UNION 
SELECT NOME, COGNOME,'per_anno'
FROM DIPENDENTI 
WHERE EXTRACT(YEAR FROM DT_ASSUNZ) ='2021'
ORDER BY RICERCA,COGNOME; */
--3.2
/* SELECT NOME,COGNOME,'prima del aumento' AS DESCRIZIONE,STIPENDIO + (STIPENDIO*0.1)
FROM DIPENDENTI 
WHERE RUOLO != 'Manager' AND COD_UFF = 'D21'
UNION 
SELECT NOME, COGNOME,'dopo del aumento',STIPENDIO * 0.1
FROM DIPENDENTI 
WHERE RUOLO != 'Manager' AND COD_UFF = 'D21'
ORDER BY COGNOME; */
--3.3
/* select '1' as TIPO, COD_UFF,'Ufficio' as INFO,NOME_UFFICIO  as NOME from uffici
where COD_UFF in ('A00','B01','C01')
UNION all
SELECT '2' as TIPO,COD_UFF,cod_prog as INFO,nome_prog as NOME from progetti
where COD_UFF in ('A00','B01','C01')
UNION all
SELECT'3' as TIPO,cod_uff,cod_dip as INFO,cognome as NOME from DIPENDENTI
where COD_UFF in ('A00','B01','C01'); */