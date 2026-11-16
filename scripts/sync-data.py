"""Build the dashboard payload from the research outputs; no economic values in UI code."""
from pathlib import Path
import csv,json,shutil
root=Path(__file__).resolve().parents[2];app=Path(__file__).resolve().parents[1]
processed=root/'data/processed';out=app/'public/data';out.mkdir(parents=True,exist_ok=True)
snapshot=json.loads((processed/'dashboard-data.json').read_text())
series={}
for c in snapshot['coverage']:
 name=c['dataset'];rows=[]
 for r in csv.DictReader((processed/(name+'.csv')).open()):
  rows.append({k:(v if k=='period' else float(v) if v else None) for k,v in r.items()})
 series[name]=rows
series["fiscal_year_ends"]=[{k:(v if k=="period" else float(v) if v else None) for k,v in r.items()} for r in csv.DictReader((processed/"fiscal_year_ends.csv").open())]
provenance={}
for r in csv.DictReader((processed/'observations.csv').open()):
 provenance.setdefault(r['dataset'],{'url':r['source_url'],'unit':r['unit'],'source_file':r['source_file']})
provenance["fiscal_year_ends"]=provenance["fiscal"]
snapshot.update(series=series,provenance=provenance,validation=json.loads((processed/'validation.json').read_text()))
(out/'economy.json').write_text(json.dumps(snapshot,separators=(',',':'),allow_nan=False))
for name in ['coverage.csv','quality_issues.json','observations.csv']:
 shutil.copy2(processed/name,app/'public/downloads'/name)
shutil.copy2(root/'research/kenya-economy-analysis.html',app/'public/downloads/research.html')
shutil.copy2(root/'kenya-economy-research-2026-11-13.zip',app/'public/downloads/research-package.zip')
print('Synced',len(series),'dataset views from',snapshot['as_of'])
