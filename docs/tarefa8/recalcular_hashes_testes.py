#!/usr/bin/env python3
"""
Recalcula, de forma independente, os fingerprints SHA-256 das execuções
armazenadas em testes/ do artefato IoT-ID (sbrc26_fingerprint).

Para cada execução, lê fingerprint.json (bundle bruto), reconstrói a
CANON_STRING com o código ATUAL do artefato nas políticas "stable" e "rich",
e compara com o hash armazenado em fingerprint_sha256.txt.

Uso:
  git clone https://github.com/GT-IoTEdu/sbrc26_fingerprint.git
  python3 docs/tarefa8/recalcular_hashes_testes.py <caminho/sbrc26_fingerprint> saida.json

Commit do artefato usado na T8: 167f48792858630020a408147ade001e5c977f78
"""
import sys, json, os, re, hashlib, logging

art = sys.argv[1]
sys.path.insert(0, art)
from canonicalize_features import build_canon, dumps_canon  # noqa: E402

logging.disable(logging.CRITICAL)

rows = []
for d in sorted(os.listdir(os.path.join(art, "testes"))):
    p = os.path.join(art, "testes", d)
    if not os.path.isdir(p):
        continue
    bundle = json.load(open(os.path.join(p, "fingerprint.json"), encoding="utf-8"))
    stored = open(os.path.join(p, "fingerprint_sha256.txt")).read().strip()
    log = open(os.path.join(p, "fingerprint_pipeline.log"), encoding="utf-8").read()
    m = re.search(r"canon_policy=(\w+)", log)
    pol = m.group(1) if m else "?"
    canon_txt = open(os.path.join(p, "features_canon.txt"), encoding="utf-8").read().strip()
    h = {}
    for po in ("stable", "rich"):
        cs = dumps_canon(build_canon(bundle, policy=po))
        h[po] = hashlib.sha256(cs.encode("utf-8")).hexdigest()
    rows.append(dict(
        run=d, policy_log=pol, stored=stored,
        stable=h["stable"], rich=h["rich"],
        match_stable=h["stable"] == stored, match_rich=h["rich"] == stored,
        sha_of_stored_canon_matches=hashlib.sha256(canon_txt.encode()).hexdigest() == stored,
    ))

if len(sys.argv) > 2:
    json.dump(rows, open(sys.argv[2], "w"), indent=1)

for r in rows:
    s = "OK" if r["match_stable"] else r["stable"][:8]
    ri = "OK" if r["match_rich"] else r["rich"][:8]
    print(f"{r['run']:32} log={r['policy_log']:6} armazenado={r['stored'][:8]} "
          f"stable={s:8} rich={ri:8} sha(features_canon.txt)==armazenado:{r['sha_of_stored_canon_matches']}")
