#!/usr/bin/env python
# -*- coding: utf-8 -*-
#viendo coincidencias entre archivos
import csv
import jellyfish as jl
import arrow
import datetime
def busca_repetidos_i(file,r):
    with open(file, 'rb') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row["ANUNCIO"]==r["ANUNCIO"]:
                return False
            
    return True
                        

def busca_rep(file):
    f=csv.writer(open("sancionados_clean_p1.csv",'wb+')) 
    head=["GOBIERNO","SIGLAS","DEPENDENCIA","CLAVEUC","NOMBRE_DE_LA_UC","RESPONSABLE","CODIGO_EXPEDIENTE","TITULO_EXPEDIENTE","PLANTILLA_EXPEDIENTE","NUMERO_PROCEDIMIENTO",
"EXP_F_FALLO","PROC_F_PUBLICACION","FECHA_APERTURA_PROPOSICIONES","CARACTER","TIPO_CONTRATACION","TIPO_PROCEDIMIENTO","FORMA_PROCEDIMIENTO","CODIGO_CONTRATO",
"TITULO_CONTRATO","FECHA_INICIO","FECHA_FIN","IMPORTE_CONTRATO","MONEDA","ESTATUS_CONTRATO","ARCHIVADO","CONVENIO_MODIFICATORIO","RAMO","CLAVE_PROGRAMA",
"APORTACION_FEDERAL","FECHA_CELEBRACION","CONTRATO_MARCO","COMPRA_CONSOLIDADA","PLURIANUAL","CLAVE_CARTERA_SHCP","ESTRATIFICACION_MUC","FOLIO_RUPC",
"ESTRATIFICACION_MPC","SIGLAS_PAIS","ESTATUS_EMPRESA","CUENTA_ADMINISTRADA_POR","C_EXTERNO","ORGANISMO","ANUNCIO","PROVEEDOR_CONTRATISTA","PROVEEDOR_DOS","ESTATUS","EXTRA"]
    f.writerow(head)
    with open(file, 'rb') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if busca_repetidos_i("sancionados_clean_p1.csv",row):
                l=[]
                            #print k.keys()
                for key in head:
                    l.append(row[key])
                f.writerow(l)
                                        
busca_rep("sancionados_url_p1.csv")