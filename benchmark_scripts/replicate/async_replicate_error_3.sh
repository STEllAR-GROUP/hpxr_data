#!/bin/bash

n_values='3'
exec_times='0 200'
cores='1'

for n_value in $n_values
do
    for core in $cores
    do
        for exec_time in $exec_times
        do
            for total in {1..10}
            do
                for error_rate in $(seq 5 1 10)
                do
                    ../../../build/bin/async_replicate_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replicate/async_replicate_${core}_${exec_time}_${total}.txt
                    ../../../build/bin/async_replicate_validate_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replicate/async_replicate_${core}_${exec_time}_${total}.txt
                    ../../../build/bin/async_replicate_vote_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replicate/async_replicate_${core}_${exec_time}_${total}.txt
                    ../../../build/bin/async_replicate_vote_validate_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replicate/async_replicate_${core}_${exec_time}_${total}.txt
                    echo "done ${exec_time}_${core}_${error_rate}_${total}"
                done
            done
        done
    done
done
