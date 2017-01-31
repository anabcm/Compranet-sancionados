#!/usr/bin/env python
# -*- coding: utf-8 -*-
#viendo coincidencias entre archivos
import csv
import jellyfish as jl
import arrow
import datetime
def find_infile(file,busca,hechos):
    lista=[]
    flag=False
    with open(file,'rb') as csvfile:
        reader=csv.DictReader(csvfile)        
        for row in reader:     
            distance=jl.jaro_winkler(row['PROVEEDOR_CONTRATISTA'].decode(encoding='UTF-8',errors='strict'),busca.decode(encoding='UTF-8',errors='strict'))
            if (hechos.find(row["NUMERO_PROCEDIMIENTO"])!=-1) and distance>0.94:
                #print hechos.find(row['CODIGO_CONTRATO'])
                #print row['CODIGO_CONTRATO']
                #print hechos
                flag=True
                return row,flag
            else:
                
                if distance>0.95: 
                    lista.append(row)                
                #print "si esta"+ row['PROVEEDOR_CONTRATISTA']+ "   "+busca
    return lista,flag

def read_sancionados(file,files):
    f=csv.writer(open('sancionados_url.csv','wb+'))
    f2=csv.writer(open('sancionados_url_not_found.csv','wb+'))
    
    head=["GOBIERNO","SIGLAS","DEPENDENCIA","CLAVEUC","NOMBRE_DE_LA_UC","RESPONSABLE","CODIGO_EXPEDIENTE","TITULO_EXPEDIENTE","PLANTILLA_EXPEDIENTE","NUMERO_PROCEDIMIENTO",
"EXP_F_FALLO","PROC_F_PUBLICACION","FECHA_APERTURA_PROPOSICIONES","CARACTER","TIPO_CONTRATACION","TIPO_PROCEDIMIENTO","FORMA_PROCEDIMIENTO","CODIGO_CONTRATO",
"TITULO_CONTRATO","FECHA_INICIO","FECHA_FIN","IMPORTE_CONTRATO","MONEDA","ESTATUS_CONTRATO","ARCHIVADO","CONVENIO_MODIFICATORIO","RAMO","CLAVE_PROGRAMA",
"APORTACION_FEDERAL","FECHA_CELEBRACION","CONTRATO_MARCO","COMPRA_CONSOLIDADA","PLURIANUAL","CLAVE_CARTERA_SHCP","ESTRATIFICACION_MUC","FOLIO_RUPC",
"ESTRATIFICACION_MPC","SIGLAS_PAIS","ESTATUS_EMPRESA","CUENTA_ADMINISTRADA_POR","C_EXTERNO","ORGANISMO","ANUNCIO","PROVEEDOR_CONTRATISTA"]
    f.writerow(head)
        
    with open(file, 'rb') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            print row['Proveedor']
            todos=[]
            flag=False
            year=arrow.get(row['FechadeResolucion'],'YYYY-MM-DD').date().year
            anios_analiza=[]
            if year<2010: anios_analiza=files
            else: 
                if year<=2012: anios_analiza=files[:0]
                else:
                    if year==2013:  anios_analiza=files[:1]
                    else:
                        if year==2014:  anios_analiza=files[:2]
                        else:
                            if year==2015:  anios_analiza=files[:3]
                            else:
                                anios_analiza=files
                
            for i in anios_analiza:      
                #print row['Hechos']                
                lista,flag=find_infile(i, row['Proveedor'],row['Hechos'])                    
                if flag:                    
                    #f.writerow([row['Proveedor'],flag])
                    l=[]
                            #print k.keys()
                    for key in head:
                        l.append(k[key])
                    l.append(row['Proveedor'])
                    l.append(flag)
                    f.writerow(l)
                    break
                else:
                    todos.append(lista)
            if flag==False:
                #f.writerow([row['Proveedor'],flag])
                fa=False
                for i in todos:    
                    #print i
                   # f.writerows(i)
                   if len(i)>0:
                        for k in i:
                            l=[]
                            #print k.keys()
                            for key in head:
                                l.append(k[key])
                                                        
                            l.append(row['Proveedor'])
                            l.append(flag)
                        #print len(k)
                        #rint k.values()
                            #print l
                            f.writerow(l)
                            fa=True
                if fa==False:
                    f2.writerow([row['Proveedor'],flag])
                    
    #f.close()
    #f2.close()
              
contratistas="ProveedoresyContratistasSancionados_2.csv"    
files=["2010_2012.csv","2013.csv","2014.csv","2015.csv","2016.csv"]
output="Lista_datos_exacto"
outputl="Lista_datos_laxo"
read_sancionados(contratistas,files)


