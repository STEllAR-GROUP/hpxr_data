#!/bin/bash

iterations='8192'
n_value='30000'
cores='32'

for core in $cores
do
    for iteration in $iterations
    do
        for error_rate in {3..10}
        do
            for total in {1..10}
            do
                ../../../build/bin/1d_stencil_replay_benchmarks --n-value=${n_value} -t${core} --iteration=${iteration} --subdomain-width=8000 --subdomains=256 --steps-per-iteration=128 --error-rate=${error_rate} >> 1d_stencil/1d_stencil_${core}_8000_${total}.txt
                ../../../build/bin/1d_stencil_checksum_benchmarks --n-value=${n_value} -t${core} --iteration=${iteration} --subdomain-width=8000 --subdomains=256 --steps-per-iteration=128 --error-rate=${error_rate} >> 1d_stencil/1d_stencil_${core}_8000_${total}.txt
                echo "done 32000_${iteration}_${error_rate}_${core}_${total}"
            done
        done
    done
done
