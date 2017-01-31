#!/usr/bin/env python
# -*- coding: utf-8 -*-
#viendo coincidencias entre archivos
import csv
import jellyfish as jl
def find_infile(file,busca):
    lista=[]
    lista2=[]
    with open(file,'rb') as csvfile:
        reader=csv.DictReader(csvfile)
        
        for row in reader:
            comp=jl.jaro_winkler(row['PROVEEDOR_CONTRATISTA'].decode(encoding='UTF-8',errors='strict'),busca.decode(encoding='UTF-8',errors='strict'))
            if comp>0.96:                
                lista.append(row['ANUNCIO'])
                
            if comp>0.92:                
                lista2.append(row['ANUNCIO'])
                #print "si esta"+ row['PROVEEDOR_CONTRATISTA']+ "   "+busca
    return lista,lista2

def read_sancionados(file,files,outp,outp2):
    f=open(outp,'w')
    f2=open(outp2,'w')
    total_url1=0
    total_sin_url1=0
    total_con_url1=0
    total_url2=0
    total_sin_url2=0
    total_con_url2=0
    with open(file, 'rb') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            f.write(row['Proveedor']+"\n")
            f2.write(row['Proveedor']+"\n")
            for i in files:                
                lista,lista2=find_infile(i, row['Proveedor'])    
                if len(lista)>0:  
                    total_url1=total_url1+len(lista)
                    total_con_url1=total_con_url1+1
                    f.write(i[:4]+"\n")
                    for k in lista:
                        f.write(k+"\n")
                else:
                    total_sin_url1=total_sin_url1+1
                if len(lista2)>0:  
                    total_url2=total_url2+len(lista2)
                    total_con_url2=total_con_url2+1
                    f2.write(i[:4]+"\n")
                    for k in lista2:
                        f2.write(k+"\n")
                else:
                    total_sin_url2=total_sin_url2+1

    print "Total de url en el primer file: ",total_url1
    print "Cantidad de contratistas sancionados con url ",total_con_url1
    print "Sin url ",total_sin_url1
    print "Total de URL en el segundo archivo ",total_url2
    print "Total de contratistas sancionados con URL en el segundo file",total_con_url2
    print "Sin URL",total_sin_url2
    f.close()
    f2.close()
              
contratistas="ProveedoresyContratistasSancionados.csv"    
files=["2010_2012.csv","2013.csv","2014.csv","2015.csv","2016.csv"]
output="Lista_datos_exacto"
outputl="Lista_datos_laxo"
read_sancionados(contratistas,files,output,outputl)


