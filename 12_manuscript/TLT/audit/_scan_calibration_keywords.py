import fitz,glob,os,re,csv,json
pat={
 'ECE':r'\bECE\b|expected calibration error',
 'calibration':r'\bcalibrat',
 'reliability_diagram':r'reliability (diagram|curve|plot)|calibration (curve|plot)',
 'Brier':r'\bBrier\b',
 'NLL_logloss':r'\bNLL\b|negative log[- ]likelihood|log[- ]loss|\blogloss\b',
}
rows=[];ctx=[]
for f in sorted(glob.glob(r'D:\TRINH\GraphSSL_KT_Survey\14_references\*.pdf')):
    d=fitz.open(f); t=' '.join(p.get_text() for p in d); n=len(d); d.close()
    t2=re.sub(r'\s+',' ',t)
    r={'pdf':os.path.basename(f),'pages':n,'chars':len(t2)}
    for k,p in pat.items():
        ms=list(re.finditer(p,t2,flags=re.I if k!='ECE' else 0))
        r[k]=len(ms)
        for m in ms[:3]:
            ctx.append((os.path.basename(f)[:40],k,t2[max(0,m.start()-80):m.end()+80]))
    rows.append(r)
json.dump({'rows':rows,'ctx':ctx},open('../supplementary/_calibration_keyword_scan_raw.json','w'),indent=1)
for r in rows: print(r['chars']>2000, r['pdf'][:55].ljust(55), r['pages'], *(r[k] for k in pat))
