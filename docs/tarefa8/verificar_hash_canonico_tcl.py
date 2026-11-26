#!/usr/bin/env python3
"""Verificação isolada dos hashes esperados para o exemplo TCL.

Este script usa uma fixture derivada dos registros públicos e replica as regras
stable/rich descritas no código atual. Não importa nem executa o pipeline IoT-ID
original e não captura tráfego de rede.
"""
import hashlib
import json

BASE = {
    "nmap": {
        "manufacturer": "TCL",
        "model_name": "Smart TV Pro",
        "name": "Smart TV Pro",
        "server": "UPnP/1.0, DLNADOC/1.50 Platinum/1.0.5.13",
    },
    "p0f": {
        "extracted": {
            "server_synack_raw_sig_set": ["4:64+0:0:1460:65535,0:mss:df:0"]
        }
    },
    "pcap_syn": {"mss": "1460", "ttl": "64", "window_size": "65535"},
}


def canonicalize(policy):
    nmap = {
        key: BASE["nmap"][key]
        for key in ("manufacturer", "model_name")
        if BASE["nmap"].get(key)
    }
    if policy == "rich":
        for key in ("name", "server"):
            if BASE["nmap"].get(key):
                nmap[key] = BASE["nmap"][key]

    obj = {
        "nmap": nmap,
        "p0f": BASE["p0f"],
        "pcap_syn": BASE["pcap_syn"],
    }
    canonical = json.dumps(
        obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return canonical, digest


def main():
    expected = {
        "stable": "3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961",
        "rich": "e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51",
    }
    for policy in ("stable", "rich"):
        canonical, digest = canonicalize(policy)
        print(f"policy={policy}")
        print(f"length_chars={len(canonical)}")
        print(f"sha256={digest}")
        print(f"matches_expected={digest == expected[policy]}")
        print(f"canonical={canonical}")
        print()


if __name__ == "__main__":
    main()
