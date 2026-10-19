# Saída bruta — teste isolado de hash da fixture TCL

**Data:** 19/10/2026  
**Ambiente:** Python 3.13.5; Linux x86_64  
**Escopo:** reprodução da lógica do script `verificar_hash_canonico_tcl.py` sobre a fixture nele definida. Não importa nem executa o código original do IoT-ID, não usa o arquivo de log histórico como entrada e não captura tráfego.

```text
policy=stable
length_chars=203
sha256=3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961
matches_expected=True
canonical={"nmap":{"manufacturer":"TCL","model_name":"Smart TV Pro"},"p0f":{"extracted":{"server_synack_raw_sig_set":["4:64+0:0:1460:65535,0:mss:df:0"]}},"pcap_syn":{"mss":"1460","ttl":"64","window_size":"65535"}}

policy=rich
length_chars=277
sha256=e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51
matches_expected=True
canonical={"nmap":{"manufacturer":"TCL","model_name":"Smart TV Pro","name":"Smart TV Pro","server":"UPnP/1.0, DLNADOC/1.50 Platinum/1.0.5.13"},"p0f":{"extracted":{"server_synack_raw_sig_set":["4:64+0:0:1460:65535,0:mss:df:0"]}},"pcap_syn":{"mss":"1460","ttl":"64","window_size":"65535"}}

exit_code=0
```

**Interpretação:** a serialização canônica e o SHA-256 calculados para as duas variantes da fixture coincidem com os valores esperados no script. Isso confirma somente o cálculo isolado da fixture. Não explica por que o log histórico rotula como `stable` uma representação que contém os campos `nmap.name` e `nmap.server`, nem demonstra reprodução ponta a ponta do artefato.
