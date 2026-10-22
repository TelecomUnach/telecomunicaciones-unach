#!/usr/bin/env python3
"""Importa JSON normalizado desde una exportación institucional autorizada.
No conecta con API, no autentica y no calcula Fingerprint de Elsevier.
"""
import argparse,datetime,json,pathlib,sys,urllib.parse
p=argparse.ArgumentParser(description=__doc__);p.add_argument('docente');p.add_argument('archivo',type=pathlib.Path);a=p.parse_args()
def web(value):
 if not isinstance(value,str) or urllib.parse.urlsplit(value).scheme!='https' or not urllib.parse.urlsplit(value).netloc:raise ValueError('Se requiere una URL HTTPS de fuente.')
 return value
def date(value):
 parsed=datetime.date.fromisoformat(value)
 if parsed>datetime.date.today():raise ValueError('La fecha no puede ser futura.')
 return value
try:
 root=pathlib.Path(__file__).resolve().parents[1];dest=root/'data.js';d=json.loads(dest.read_text(encoding='utf-8').removeprefix('window.PORTFOLIO = ').strip().removesuffix(';'));who=next((x for x in d['people'] if x['id']==a.docente),None)
 if who is None:raise ValueError('Docente desconocido.')
 payload=json.loads(a.archivo.read_text(encoding='utf-8-sig'));provider=payload.get('provider');src=web(payload.get('source'));review=date(payload.get('date'))
 if provider not in ['Pure','Scopus','Elsevier Fingerprint Engine','ORCID']:raise ValueError('Proveedor no reconocido.')
 if payload.get('orcid') and payload['orcid']!=who.get('orcid'):raise ValueError('ORCID distinto del perfil. Resuelva la identidad antes de importar.')
 # All validation precedes writeback.
 pubs=payload.get('publications')
 if pubs is not None:
  if not isinstance(pubs,list) or not pubs:raise ValueError('La lista de publicaciones debe contener registros; no se vacía la bibliografía.')
  checked=[]
  for rec in pubs:
   if not isinstance(rec.get('title'),str) or not rec['title'].strip():raise ValueError('Publicación sin título.')
   year=rec.get('year')
   if year is not None and (not isinstance(year,int) or year<1800 or year>datetime.date.today().year+1):raise ValueError('Año de publicación no válido.')
   citations=rec.get('citations')
   if citations is not None and (not isinstance(citations,int) or citations<0):raise ValueError('Citas no válidas.')
   checked.append({'title':rec['title'],'year':year,'authors':rec.get('authors',''),'venue':rec.get('venue',''),'doi':rec.get('doi',''),'citations':None,'providerCitations':citations,'provider':provider,'source':web(rec.get('source') or src),'sourceLabel':provider,'type':rec.get('type','article'),'note':'authorized-export','date':review})
  who['publications']=checked
 for field in ['scopus','pure']:
  if field in payload:who[field]=web(payload[field])
 if 'fingerprint' in payload:
  fp=payload['fingerprint']
  if provider not in ['Pure','Elsevier Fingerprint Engine'] or not isinstance(fp.get('terms'),list) or not fp['terms']:raise ValueError('Fingerprint debe proceder de una exportación de Pure o Elsevier Fingerprint Engine con términos.')
  for term in fp['terms']:
   if not isinstance(term.get('label'),str) or not term['label'].strip():raise ValueError('Término sin etiqueta.')
  who['fingerprint']={'provider':'Elsevier Fingerprint Engine','source':src,'date':review,'terms':fp['terms']}
 # Keep Scopus metrics separate from Google Scholar metrics.
 if 'metrics' in payload:
  m=payload['metrics']
  for key in ['citations','h']:
   if not isinstance(m.get(key),int) or m[key]<0:raise ValueError('Métricas no válidas.')
  who['externalMetrics']={'provider':provider,'source':src,'date':review,'citations':m['citations'],'h':m['h']}
 who.setdefault('sources',[]).append({'label':provider+' · exportación institucional autorizada · '+review,'url':src,'kind':'authorized-export'});who['reviewed']=review;d['updated']=review
 dest.with_suffix('.js.bak').write_bytes(dest.read_bytes());tmp=dest.with_suffix('.js.tmp');tmp.write_text('window.PORTFOLIO = '+json.dumps(d,ensure_ascii=False,indent=2)+';\n',encoding='utf-8');tmp.replace(dest)
 print('Exportación incorporada. Compruebe autorías y fuentes antes de publicar.')
except (ValueError,TypeError,OSError) as e:sys.exit(str(e))
