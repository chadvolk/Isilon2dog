# Isilon2dog
A rspository that has scripts to pull and push data between Isilon OneFS API and datadog. 


## Metrics
1) Total disk percentage utilisation 
2) Disk percentage utilisation of each of the node pools with a cluster 
3) Remaining total actual usable disk space, in PiB and TB 
4) Current actual used disk space, in PiB and TB 
5) Growth in cluster utilisation (actuals) in last 24 hours, week and month 
6) Growth of the /ifs/genomics/inbound/by_date in last 24 hours, week and month 
7) Top 5 growing directories in last 24 hours, week and month besides /ifs/genomics/inbound/by_date 
8) Whether most recent SyncIQ jobs have completed successfully from P1 
9) Last created directory within /ifs/genomics/inbound/by_date in P2 Pod 1 
10) Current running Job Operations and their status message 
