Detections
==================

This repository contains all public indicators identified by 401trg during the course of our investigations. It also includes relevant yara rules and IDS signatures to detect these indicators.

Our public PGP Key can be found [here](https://keybase.io/401trg/pgp_keys.asc?fingerprint=1c3e9c9719d6480f1446e4f1812dc5f3628952f9).

# Reports

| Directory | Link | Published    |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|  | [Building a Data Lake for Threat Research](https://401trg.pw/building-a-data-lake-for-threat-research/) | Apr 02, 2018 |
| [20180222_Analysis_of_Active_Satori_Botnet_Infections_indicators](https://github.com/401trg/detections/blob/master/ioc/20180222_Satori_Botnet_RCE_indicators.csv) <br> [20180222_Analysis_of_Active_Satori_Botnet_Infections__ids](https://github.com/401trg/detections/blob/master/ids/20180222_Satori_Botnet_RCE.rules)  | [Analysis of Active Satori Botnet Infections](https://401trg.pw/analysis-of-active-satori-botnet-infections/) | Feb 22, 2018 |
| [20171220_Introduction_to_SMB_pcaps](https://github.com/401trg/detections/tree/master/pcaps) <br> 
[20171220_Introduction_to_SMB_pdf](https://github.com/401trg/detections/blob/master/pdfs/20171220_An-Introduction-to-SMB-for-Network-Security-Analysts.pdf) | [An Introduction to SMB for Network Security Analysts](https://401trg.pw/an-introduction-to-smb-for-network-security-analysts/) | Dec 20, 2017 |
|  | [Triaging Large Packet Captures - Methods for Extracting & Analyzing Domains](https://401trg.pw/triaging-large-packet-captures-methods-for-extracting-analyzing-domains/) | Nov 28, 2017 |
|  | [Using Emerging Threats Suricata Ruleset to Scan PCAP](https://401trg.pw/using-emergingthreats-suricata-ruleset-to-scan-pcap/) | Nov 14, 2017 |
| [20171101_ExposingPhishing_indicators](https://github.com/401trg/detections/blob/master/ioc/20171101_ExposingPhishing_indicators.csv) <br> [20171101_ExposingPhishing_ids](https://github.com/401trg/detections/blob/master/ids/20171101_ExposingPhishing_ids.rules)  | [Exposing a Phishing Kit](https://401trg.pw/exposing-a-phishing-kit) | Nov 01, 2017 |
| [20171026_LargeScaleIRC_indicators](https://github.com/401trg/detections/blob/master/ioc/20171026_LargeScaleIRC_indicators.csv) <br> [20171026_LargeScaleIRC_ids](https://github.com/401trg/detections/blob/master/ids/20171026_LargeScaleIRC_ids.rules)| [Large Scale IRCbot Infection Attempts](https://401trg.pw/large_scale_ircbot_infection_attempts) | Oct 26, 2017 |
| [20171016_UpdateWinnti_indicators](https://github.com/401trg/detections/blob/master/ioc/20171016_UpdateWinnti_indicators.csv) <br> [20171016_UpdateWinnti_ids](https://github.com/401trg/detections/blob/master/ids/20171016_UpdateWinnti_ids.rules)| [An Update on Winnti](https://401trg.pw/an-update-on-winnti/) | Oct 16, 2017 |
| [20171010_TurlaWateringHole_indicators](https://github.com/401trg/detections/blob/master/ioc/20171010_TurlaWateringHole_indicators.csv) <br> [20171010_TurlaWateringHole_ids](https://github.com/401trg/detections/blob/master/ids/20171010_TurlaWateringHole_ids.rules) | [Turla Watering Hole Campaigns 2016/2017](https://401trg.pw/turla-watering-hole-campaigns-2016-2017/) | Oct 10, 2017 |
|  | [Identifying and Triaging DNS Traffic on Your Network](https://401trg.pw/identifying-and-triaging-dns-traffic-on-your-network/) | Oct 02, 2017 |
|  | [Triaging Large Packet Captures - 4 Key TShark Commands to Start Your Investigation](https://401trg.pw/triaging-large-packet-captures-4-key-tshark-commands-to-start-your-investigation/) | Sept 28, 2017 |
| [20170711_WinntiEvolution_indicators](https://github.com/401trg/detections/blob/master/ioc/20170711_WinntiEvolution_indicators.csv) | [Winnti (LEAD/APT17) Evolution - Going Open Source](https://401trg.pw/winnti-evolution-going-open-source/) | Jul 11, 2017 |

# IDS
This directory contains IDS signatures to detect these indicators located in the ioc directory. These signatures are compatible with Suricata v4.0.4.

# IOC
This directory contains IOCs from post at [401trg.pw](https://401trg.pw). The csv files follow the unified format described below. These indicators are not defanged and are considered malicious.

# PCAPS
This directory contains example pcaps for knowledge post from [401trg.pw](https://401trg.pw).

# PDF
This directory contains pdfs of 401TRG long-form post.

# Unified Format
All IOC files are csv and follow the following format:
`"Indicator","Type","Description","Reference"`

There are several types of indicators:
- `COOKIE`
- `CERT SHA1`
- `CODE SIGN CERT SERIAL`
- `DOMAIN`
- `EMAIL`
- `FILE MD5`
- `IP`
- `PHONE`
- `URL`

Example:
```
"Indicator","Type","Description","Reference"
"asdf.asdf.com","DOMAIN","This is a malicious domain","https://401trg.pw/this-post-does-not-exist"
```

The description field is left blank when there is no context to add to the indicator. The reference field will contain a link to the 401TRG post that disclosed the indicator. 

# License
All data is provided under Apache License, Version 2.0 which can be found [here](https://www.apache.org/licenses/LICENSE-2.0).
