#!/usr/bin/env python3
"""Importa un CSV exportado desde Google Scholar sin scraping ni dependencias."""
import argparse,csv,datetime,json,pathlib,sys
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('docente',help='Identificador del docente en data.js')
p.add_argument('csv',type=pathlib.Path,help='CSV exportado por Google Scholar')
p.add_argument('--citas',type=int);p.add_argument('--h',type=int);p.add_argument('--i10',type=int)
p.add_argument('--fecha',help='Fecha de consulta de las métricas: AAAA-MM-DD')
a=p.parse_args();root=pathlib.Path(__file__).resolve().parents[1];dest=root/'data.js'
try:
 data=json.loads(dest.read_text(encoding='utf-8').removeprefix('window.PORTFOLIO = ').strip().removesuffix(';'))
 teacher=next((x for x in data['people'] if x['id']==a.docente),None)
 if teacher is None: raise ValueError('Docente no encontrado: '+a.docente)
 vals=[a.citas,a.h,a.i10]
 if any(x is not None for x in vals):
  if not all(x is not None and x>=0 for x in vals) or not a.fecha: raise ValueError('Indique --citas, --h, --i10 y --fecha juntos, con valores no negativos.')
  datetime.date.fromisoformat(a.fecha)
 if a.fecha and datetime.date.fromisoformat(a.fecha)>datetime.date.today(): raise ValueError('La fecha no puede ser futura.')
 with a.csv.open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f)
  if not reader.fieldnames or 'Title' not in reader.fieldnames: raise ValueError('CSV no reconocido: se requiere la columna Title de la exportación de Scholar.')
  publications=[]
  for row in reader:
   title=(row.get('Title') or '').strip()
   if not title: continue
   year=(row.get('Year') or '').strip()
   publications.append({'title':title,'authors':row.get('Authors',''),'year':int(year) if year.isdigit() else None,'venue':row.get('Publication',''),'doi':row.get('DOI',''),'citations':None,'source':f"https://scholar.google.com/citations?user={teacher['scholar']}" if teacher['scholar'] else '', 'note':'scholar-csv-export'})
 if not publications: raise ValueError('No se encontraron publicaciones; se conserva el archivo original.')
 teacher['publications']=publications
 if a.fecha and all(x is not None for x in vals): teacher['metrics']={'citations':a.citas,'h':a.h,'i10':a.i10,'date':a.fecha}
 data['updated']=datetime.date.today().isoformat()
 backup=dest.with_suffix('.js.bak');backup.write_bytes(dest.read_bytes())
 temp=dest.with_suffix('.js.tmp');temp.write_text('window.PORTFOLIO = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n',encoding='utf-8');temp.replace(dest)
 print(f'Importadas {len(publications)} publicaciones de {teacher["name"]}. Copia de seguridad: {backup.name}')
except (ValueError,OSError,csv.Error) as e:
 sys.exit(str(e))
