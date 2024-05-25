#/bin/bash

carpeta=$1
rm datos$1.txt

for archivo in $(ls -1v "$carpeta"/*); do
	nombreArch=$(basename "$archivo")
	modelo=$(echo "$archivo" | awk -F'/' '{print $NF}' | awk -F'_' '{print $1}')
        scenario=$(echo "$archivo" | cut -d "_" -f 2)
        batch=$(echo "$archivo" | cut -d "_" -f 3)
	arg=$(echo "$archivo" | cut -d "_" -f 4 | cut -d "." -f 1)
	
	if [ "$scenario" == "Offline" ]; then
            timeNs=$(grep -oP -a 'result_samples_per_second: \K\d+\.\d+' "$archivo" | head -n 1)
	    valid=$(grep -a 'performance: result_samples_per_second:' "$archivo" | awk '{print $NF}')
	    latency=$(grep -a '99.90 percentile latency (ns)   :' "$archivo" | awk '{print $NF}')
            latencyS=$(echo "$latency" | awk '{print substr($0, 1, length($0)-9)}')
            #if [ "$valid" == "VALID" ]; then
	        #printf "%-10s%-15s%-5s%-10s%-10s%-10s%-10s\n" "$modelo" "$scenario" "$batch" "$arg" "$timeNs" "$valid" "$latencyS" >>datos$1.txt
            #fi

        elif [ "$scenario" == "Server" ]; then
            timeNs=$(grep -oP -a 'result_scheduled_samples_per_sec: \K\d+\.\d+' "$archivo" | head -n 1)
	    valid=$(grep -a 'performance: result_scheduled_samples_per_sec:' "$archivo" | awk '{print $NF}')
	    completed=$(grep -a 'Completed samples per second    :' "$archivo" |awk '{print $NF}')
	    latency=$(grep -a '99.90 percentile latency (ns)   :' "$archivo" |awk '{print $NF}')
#            if [ "$valid" == "VALID" ]; then
                printf "%-10s%-15s%-5s%-10s%-10s%-10s%-10s%-10s\n" "$modelo" "$scenario" "$batch" "$arg" "$timeNs" "$valid" "$latency" "$completed" >>datos$1.txt
#            fi
      
	else 
            timeNs=$(grep -oP -a 'result_90.00_percentile_latency_ns: \K\d+' "$archivo" | head -n 1)
	    valid=$(grep -a ' performance: result_90.00_percentile_latency_ns:' "$archivo" | awk '{print $NF}')
	    target=$(grep -a 'target_qps : ' "$archivo" | awk '{print $NF}')
            qps_w=$(grep -a 'QPS w/ loadgen overhead         :' "$archivo" | awk '{print $NF}')
	    qps_w_o=$(grep -a 'QPS w/o loadgen overhead        :' "$archivo" | awk '{print $NF}')
            printf "%-10s%-15s%-5s%-10s%-10s%-10s%-10s%-10s%-10s%-10s\n" "$modelo" "$scenario" "$batch" "$arg" "$timeNs" "$valid"  "$target"  "$qps_w " "$qps_w_o">>datos$1.txt

  
	 fi

	
done
