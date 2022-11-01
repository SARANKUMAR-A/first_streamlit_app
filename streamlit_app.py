create table MAX_OUTGOING.FOR_ACME.LOTSTOCKRETURN as
SELECT 
l.VIN
,y.MODYEARNAME
,m.MAKE_NAME
,v.DESC1
,v.DESC2
,v.DESC3
,BODYSTYLE
,ENGINE
,DRIVETYPE
,TRANS
,MPG
,MANUF_NAME
,COUNTRY
,VEHICLETYPE
,PLANTNAME
FROM ACME_DETROIT.ADU.LOTSTOCK l -- he joins Lottie's data from the INBOUND SHARE 
JOIN MAX_VIN.DECODE.WMITOMANUF w -- with all his data (he just tested)
    ON l.WMI=w.WMI
JOIN MAX_VIN.DECODE.MANUFTOMAKE m
    ON w.manuf_id=m.manuf_id
JOIN MAX_VIN.DECODE.MANUFPLANTS p
    ON l.plantcode=p.plantcode
    AND m.make_id=p.make_id
JOIN MAX_VIN.DECODE.MMVDS v
    ON v.vds=l.vds 
    and v.make_id = m.make_id
JOIN MAX_VIN.DECODE.MODELYEAR y
    ON l.modyearcode=y.modyearcode;
