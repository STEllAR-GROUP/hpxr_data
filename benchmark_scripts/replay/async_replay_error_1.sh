#!/bin/bash

exec_times='200 500'
n_value='100'
cores='32 16 8'

for core in $cores
do
    for exec_time in $exec_times
    do
        for total in {1..10}
        do
            for error_rate in {3..10}
            do
                ../../../build/bin/async_replay_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replay/async_replay_${core}_${exec_time}_${total}.txt
                ../../../build/bin/async_replay_validate_benchmarks -t${core} --n-value=${n_value} --exec-time=${exec_time} --error-rate=${error_rate} >> async_replay/async_replay_${core}_${exec_time}_${total}.txt
                echo "done ${exec_time}_${core}_${error_rate}_${total}"
            done
        done
    done
done